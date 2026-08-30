# AS Academy Python 2.7.0 — Stable

## Release scope
این نسخه Course Package پایتون را از Release Candidate به Stable ارتقا می‌دهد.

### تکمیل آموزشی
- مسیر شش‌سطحی از مبانی تا Project-based
- 30 Exercise و 30 Quiz مستقل
- Final Exam جامع 40 سؤالی با پوشش بیش از 10 حوزه
- Spaced Practice و Review Checkpoint
- Guided Portfolio با milestone، acceptance criteria و rubric
- Production Capstone با معماری، دیتابیس، API، امنیت، تست، deployment، observability و rollback

### App integration
- اضافه شدن `learning-map.json` برای جریان deterministic یادگیری
- `projects/registry.json` مرجع canonical شناسه پروژه‌ها
- `course-package/` منبع حقیقت محتوای Python
- runtime و featureهای مشترک همچنان متعلق به `AS-Academy-Core` هستند

### Quality
Validator و CI موارد زیر را کنترل می‌کنند:
JSON validity، unique lesson IDs/orders، chapter/level references، Core block types، project references، assessment banks، Final Exam، Guided Project rubrics، Learning Map، Completion Path و version alignment.

## Graduation
دانشجو برای تکمیل دوره باید مسیر الزامی را طی کند، پروژه‌های لازم را انجام دهد، Review Checkpointها را با mastery تعیین‌شده پاس کند، حداقل 70٪ Final Exam بگیرد و Production Capstone را تکمیل کند.
