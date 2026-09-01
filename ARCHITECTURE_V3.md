# AS Academy Python — Architecture V3

## Dependency direction

```text
AS-Academy-Python
  ├─ consumes content from -> AS-Academy-MainCourse/courses/python/course
  ├─ consumes UI from      -> AS-Academy-MainUi
  └─ consumes runtime from -> AS-Academy-Core

AS-Academy-MainUi -> uses contracts/runtime from AS-Academy-Core
AS-Academy-MainCourse -> stores content only
```

## Ownership

### MainCourse
Owns Python lessons, levels, chapters, exercises, quizzes, assessments, projects, review data, glossary, learning map, outcomes, completion and progression metadata.

### MainUi
Owns common Academy screens/components, navigation presentation, lesson renderer UI, cards, lists, search UI, progress UI, quiz/exercise UI and responsive visual behavior.

### Core
Owns shared models, schema contracts, parsing/loading, persistence, progress state, search engine, bookmarks, notes, achievements and other reusable application logic.

### Python repository
Owns Python identity, compatibility metadata, course-specific capability declarations, migration history and integration verification only.

## Migration rule

The 2.7.0 `course-package/` is the migration source used to seed MainCourse. Once `courses/python/course/` is verified, all future educational edits must be performed there.

No new educational content should be authored in the legacy local course directories.
