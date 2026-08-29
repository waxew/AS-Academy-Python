"""Integrity checks for the app-facing AS Academy Python Course Package."""

from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "course-package"
LESSONS = PACKAGE / "lessons"

VALID_BLOCK_TYPES = {
    "TITLE", "PARAGRAPH", "LIST", "TABLE", "CODE", "OUTPUT", "TIP",
    "WARNING", "NOTE", "IMPORTANT", "EXERCISE", "QUIZ", "PROJECT",
    "DIAGRAM", "REFERENCE",
}
VALID_LEVEL_TYPES = {
    "FUNDAMENTALS", "BEGINNER", "INTERMEDIATE", "ADVANCED", "SPECIALIST", "PROJECT_BASED"
}


def load_json(path: Path):
    """Load UTF-8 JSON so malformed course content fails CI immediately."""
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def lesson_files() -> list[Path]:
    """Return all active lesson bundles; every JSON file in this directory is runtime content."""
    return sorted(LESSONS.glob("*.json"))


def all_lessons() -> list[dict]:
    """Flatten lesson bundles into one collection for cross-file validation."""
    lessons: list[dict] = []
    for path in lesson_files():
        payload = load_json(path)
        assert isinstance(payload, list), f"{path.name} must contain a JSON array"
        lessons.extend(payload)
    return lessons


def test_all_course_json_is_valid() -> None:
    """Every JSON artifact under course-package must parse successfully."""
    for path in sorted(PACKAGE.rglob("*.json")):
        load_json(path)


def test_lesson_ids_are_unique() -> None:
    """A lesson ID is a persistent runtime identity and cannot be reused."""
    ids = [lesson["id"] for lesson in all_lessons()]
    duplicates = sorted(key for key, count in Counter(ids).items() if count > 1)
    assert not duplicates, f"duplicate lesson ids: {duplicates}"


def test_lessons_reference_existing_chapters() -> None:
    """Prevent lessons from becoming unreachable because of a bad chapter reference."""
    chapter_ids = {chapter["id"] for chapter in load_json(PACKAGE / "chapters.json")}
    invalid = sorted(
        (lesson["id"], lesson.get("chapterId"))
        for lesson in all_lessons()
        if lesson.get("chapterId") not in chapter_ids
    )
    assert not invalid, f"invalid chapter references: {invalid}"


def test_chapters_reference_existing_levels() -> None:
    """All chapters must belong to one of the Core-aligned course levels."""
    level_ids = {level["id"] for level in load_json(PACKAGE / "levels.json")}
    invalid = sorted(
        (chapter["id"], chapter.get("levelId"))
        for chapter in load_json(PACKAGE / "chapters.json")
        if chapter.get("levelId") not in level_ids
    )
    assert not invalid, f"invalid level references: {invalid}"


def test_block_types_match_core_contract() -> None:
    """Only block types supported by the shared Core Content Engine are allowed."""
    invalid: list[tuple[str, str]] = []
    for lesson in all_lessons():
        for block in lesson.get("blocks", []):
            if block.get("type") not in VALID_BLOCK_TYPES:
                invalid.append((lesson["id"], str(block.get("type"))))
    assert not invalid, f"unsupported block types: {invalid}"


def test_lesson_required_fields_and_block_ids() -> None:
    """Validate minimum runtime shape and unique block identity inside each lesson."""
    required = {"id", "chapterId", "title", "summary", "order", "estimatedMinutes", "blocks"}
    for lesson in all_lessons():
        missing = required - lesson.keys()
        assert not missing, f"{lesson.get('id')} missing fields: {sorted(missing)}"
        assert lesson["title"].strip()
        assert lesson["estimatedMinutes"] > 0
        block_ids = [block["id"] for block in lesson["blocks"]]
        assert len(block_ids) == len(set(block_ids)), f"duplicate block ids in {lesson['id']}"


def test_project_references_are_registered() -> None:
    """Every PROJECT block must point to a stable project identity in the registry."""
    registry = load_json(PACKAGE / "projects/registry.json")
    registered = {project["id"] for project in registry}
    duplicates = sorted(key for key, count in Counter(p["id"] for p in registry).items() if count > 1)
    assert not duplicates, f"duplicate project registry ids: {duplicates}"

    invalid: list[tuple[str, str]] = []
    for lesson in all_lessons():
        for block in lesson.get("blocks", []):
            if block.get("type") != "PROJECT":
                continue
            project_id = block.get("metadata", {}).get("projectId")
            if not project_id or project_id not in registered:
                invalid.append((lesson["id"], str(project_id)))
    assert not invalid, f"unregistered project references: {invalid}"


def test_all_project_collections_are_registered() -> None:
    """Catalog, portfolio and completion references must use canonical project identities."""
    registered = {project["id"] for project in load_json(PACKAGE / "projects/registry.json")}
    catalog_ids = {project["id"] for project in load_json(PACKAGE / "projects/catalog.json")}
    final_ids = {project["id"] for project in load_json(PACKAGE / "projects/final-projects.json")}
    recommended = set(load_json(PACKAGE / "completion.json")["recommendedPortfolio"])
    assert catalog_ids <= registered, f"catalog projects missing from registry: {sorted(catalog_ids - registered)}"
    assert final_ids <= registered, f"final projects missing from registry: {sorted(final_ids - registered)}"
    assert recommended <= registered, f"recommended projects missing from registry: {sorted(recommended - registered)}"


def test_exercise_and_quiz_banks_are_well_formed() -> None:
    """Assessment banks need stable unique IDs and valid answer contracts."""
    exercises = load_json(PACKAGE / "exercises/bank.json")
    quizzes = load_json(PACKAGE / "quizzes/bank.json")
    exercise_ids = [item["id"] for item in exercises]
    quiz_ids = [item["id"] for item in quizzes]
    assert len(exercise_ids) == len(set(exercise_ids))
    assert len(quiz_ids) == len(set(quiz_ids))
    assert all(item["level"] in VALID_LEVEL_TYPES for item in exercises)
    for quiz in quizzes:
        assert len(quiz["choices"]) >= 2
        assert quiz["answer"] in quiz["choices"], f"invalid answer in {quiz['id']}"


def test_completion_path_matches_levels() -> None:
    """Graduation path must reference every real level exactly once and no unknown level."""
    level_ids = [level["id"] for level in load_json(PACKAGE / "levels.json")]
    required_path = load_json(PACKAGE / "completion.json")["requiredPath"]
    assert len(required_path) == len(set(required_path))
    assert set(required_path) == set(level_ids)


def test_completion_version_matches_manifest() -> None:
    """Graduation rules must describe the same content release as the manifest."""
    manifest_version = load_json(PACKAGE / "manifest.json")["version"]
    completion_version = load_json(PACKAGE / "completion.json")["courseVersion"]
    assert completion_version == manifest_version


def test_manifest_and_python_package_versions_match() -> None:
    """Release metadata must not drift between content and the Python helper package."""
    manifest_version = load_json(PACKAGE / "manifest.json")["version"]
    pyproject = (ROOT / "pyproject.toml").read_text(encoding="utf-8")
    init_file = (ROOT / "src/as_academy_python/__init__.py").read_text(encoding="utf-8")
    assert f'version = "{manifest_version}"' in pyproject
    assert f'__version__ = "{manifest_version}"' in init_file
