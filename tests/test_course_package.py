"""Integrity checks for the app-facing AS Academy Python Course Package."""

from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "course-package"
LESSONS = PACKAGE / "lessons"
VALID_BLOCK_TYPES = {"TITLE","PARAGRAPH","LIST","TABLE","CODE","OUTPUT","TIP","WARNING","NOTE","IMPORTANT","EXERCISE","QUIZ","PROJECT","DIAGRAM","REFERENCE"}
VALID_LEVEL_TYPES = {"FUNDAMENTALS","BEGINNER","INTERMEDIATE","ADVANCED","SPECIALIST","PROJECT_BASED"}


def load_json(path: Path):
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def lesson_files() -> list[Path]: return sorted(LESSONS.glob("*.json"))


def all_lessons() -> list[dict]:
    lessons=[]
    for path in lesson_files():
        payload=load_json(path); assert isinstance(payload,list), f"{path.name} must contain a JSON array"; lessons.extend(payload)
    return lessons


def test_all_course_json_is_valid():
    for path in sorted(PACKAGE.rglob("*.json")): load_json(path)


def test_lesson_ids_are_unique():
    ids=[x["id"] for x in all_lessons()]; assert not [k for k,v in Counter(ids).items() if v>1]


def test_lessons_reference_existing_chapters():
    chapters={x["id"] for x in load_json(PACKAGE/"chapters.json")}; assert not [(x["id"],x.get("chapterId")) for x in all_lessons() if x.get("chapterId") not in chapters]


def test_chapters_reference_existing_levels():
    levels={x["id"] for x in load_json(PACKAGE/"levels.json")}; assert not [(x["id"],x.get("levelId")) for x in load_json(PACKAGE/"chapters.json") if x.get("levelId") not in levels]


def test_block_types_match_core_contract():
    invalid=[]
    for lesson in all_lessons():
        for block in lesson.get("blocks",[]):
            if block.get("type") not in VALID_BLOCK_TYPES: invalid.append((lesson["id"],block.get("type")))
    assert not invalid


def test_lesson_required_fields_and_block_ids():
    required={"id","chapterId","title","summary","order","estimatedMinutes","blocks"}
    for lesson in all_lessons():
        assert not required-lesson.keys(); assert lesson["title"].strip() and lesson["estimatedMinutes"]>0
        ids=[b["id"] for b in lesson["blocks"]]; assert len(ids)==len(set(ids))


def test_lesson_orders_are_unique_within_chapters():
    grouped={}
    for lesson in all_lessons(): grouped.setdefault(lesson["chapterId"],[]).append(lesson["order"])
    for chapter,orders in grouped.items(): assert len(orders)==len(set(orders)), f"duplicate lesson order in {chapter}"


def test_project_references_are_registered():
    registry=load_json(PACKAGE/"projects/registry.json"); registered={p["id"] for p in registry}; assert len(registered)==len(registry); invalid=[]
    for lesson in all_lessons():
        for block in lesson.get("blocks",[]):
            if block.get("type")=="PROJECT":
                pid=block.get("metadata",{}).get("projectId")
                if pid not in registered: invalid.append((lesson["id"],pid))
    assert not invalid


def test_all_project_collections_are_registered():
    registered={p["id"] for p in load_json(PACKAGE/"projects/registry.json")}
    assert {p["id"] for p in load_json(PACKAGE/"projects/catalog.json")} <= registered
    assert {p["id"] for p in load_json(PACKAGE/"projects/final-projects.json")} <= registered
    assert set(load_json(PACKAGE/"completion.json")["recommendedPortfolio"]) <= registered


def test_guided_projects_have_complete_learning_contracts():
    registered={p["id"] for p in load_json(PACKAGE/"projects/registry.json")}; guides=load_json(PACKAGE/"projects/guided/portfolio-guides.json"); ids=[g["projectId"] for g in guides]; assert len(ids)==len(set(ids))
    for g in guides:
        assert g["projectId"] in registered and g["level"] in VALID_LEVEL_TYPES
        assert g["estimatedHours"]>0 and len(g["milestones"])>=4 and len(g["acceptanceCriteria"])>=4
        assert sum(g["rubric"].values())==100


def test_exercise_and_quiz_banks_are_well_formed():
    exercises=load_json(PACKAGE/"exercises/bank.json"); quizzes=load_json(PACKAGE/"quizzes/bank.json")
    assert len({x["id"] for x in exercises})==len(exercises); assert len({x["id"] for x in quizzes})==len(quizzes); assert all(x["level"] in VALID_LEVEL_TYPES for x in exercises)
    for q in quizzes: assert len(q["choices"])>=2 and q["answer"] in q["choices"]


def test_assessment_depth_is_release_ready():
    assert len(load_json(PACKAGE/"exercises/bank.json"))>=30; assert len(load_json(PACKAGE/"quizzes/bank.json"))>=30
    final_exam=load_json(PACKAGE/"assessment/final-exam.json"); questions=final_exam["questions"]
    assert 0<=final_exam["passingPercent"]<=100; assert len(questions)>=40; assert len({q["id"] for q in questions})==len(questions); assert len({q["category"] for q in questions})>=10; assert all(len(q["choices"])>=2 and q["answer"] in q["choices"] for q in questions)


def test_spaced_practice_contract():
    practice=load_json(PACKAGE/"review/spaced-practice.json"); assert practice["minimumMasteryPercent"]>=80; assert practice["scheduleDays"]==sorted(set(practice["scheduleDays"])); assert len(practice["reviewSets"])>=6


def test_learning_map_references_are_valid():
    learning_map=load_json(PACKAGE/"learning-map.json"); levels={x["id"] for x in load_json(PACKAGE/"levels.json")}; exercises={x["id"] for x in load_json(PACKAGE/"exercises/bank.json")}; quizzes={x["id"] for x in load_json(PACKAGE/"quizzes/bank.json")}; projects={x["id"] for x in load_json(PACKAGE/"projects/registry.json")}; reviews=set(load_json(PACKAGE/"review/spaced-practice.json")["checkpoints"])
    assert {x["levelId"] for x in learning_map["levels"]}==levels
    for entry in learning_map["levels"]:
        assert set(entry["exerciseIds"])<=exercises; assert set(entry["quizIds"])<=quizzes; assert set(entry["projectIds"])<=projects; assert entry["reviewCheckpointId"] in reviews


def test_learning_outcomes_cover_every_level_and_valid_prerequisites():
    outcomes=load_json(PACKAGE/"outcomes.json"); levels=[x["id"] for x in load_json(PACKAGE/"levels.json")]; entries=outcomes["levels"]
    assert [x["levelId"] for x in entries]==levels
    seen=set()
    for entry in entries:
        assert len(entry["outcomes"])>=5 and len(entry["evidence"])>=3
        assert set(entry["prerequisites"])<=seen
        assert all(item.strip() for item in entry["outcomes"])
        seen.add(entry["levelId"])


def test_completion_path_matches_levels():
    level_ids=[x["id"] for x in load_json(PACKAGE/"levels.json")]; path=load_json(PACKAGE/"completion.json")["requiredPath"]; assert len(path)==len(set(path)) and set(path)==set(level_ids)


def test_completion_version_matches_manifest(): assert load_json(PACKAGE/"completion.json")["courseVersion"]==load_json(PACKAGE/"manifest.json")["version"]


def test_manifest_and_python_package_versions_match():
    version=load_json(PACKAGE/"manifest.json")["version"]; assert f'version = "{version}"' in (ROOT/"pyproject.toml").read_text(encoding="utf-8"); assert f'__version__ = "{version}"' in (ROOT/"src/as_academy_python/__init__.py").read_text(encoding="utf-8")


def test_release_candidate_declares_required_quality_gates():
    rc=load_json(PACKAGE/"release-candidate.json"); assert rc["status"] in {"release-candidate","stable"}; assert rc["courseId"]=="python"; assert all(rc["qualityGates"].values()); assert set(rc["curriculumCoverage"])=={"fundamentals","beginner","intermediate","advanced","specialist","project-based"}
