# وضعیت محتوای AS Academy Python — Stable v2.7.0

## مسیر آموزشی
- 6 سطح استاندارد Core: Fundamentals، Beginner، Intermediate، Advanced، Specialist و Project-based
- پوشش مبانی زبان، ساختمان داده، تابع، فایل و داده ساخت‌یافته، خطا و debugging
- OOP، typing/Protocol/Generic، iterator/generator، decorator، context manager
- concurrency/threading/Lock، asyncio، testing، packaging، profiling و Big-O
- Database/SQL/ORM/Migration/Transaction و PostgreSQL/MySQL/SQL Server
- FastAPI، Flask، Django/DRF، Auth/OAuth2/RBAC و WebSocket
- Tkinter/CustomTkinter/PySide، Automation/Scraping و Telegram/Discord Bot
- NumPy/Pandas/Visualization، ML، PyTorch، TensorFlow/Keras، NLP، CV، Transformers/Hugging Face، RAG و AI Agents
- Socket/HTTP/TLS، secure coding، Docker/Compose، Linux/SSH، Uvicorn/Gunicorn/Nginx، CI/CD، Observability، Cloud، Backup/Restore/RPO/RTO
- Portfolio و Production Capstone

## Assessment
- Exercise Bank: 30 تمرین مستقل
- Quiz Bank: 30 سؤال مستقل
- Final Exam: 40 سؤال دسته‌بندی‌شده با حدنصاب 70٪
- Spaced Practice: شش Review Checkpoint با mastery حداقل 80٪
- Guided Portfolio: پروژه‌های چندمرحله‌ای با Acceptance Criteria و Rubric مجموع 100 امتیاز

## App-facing Contract
- `course-package/manifest.json`: نسخه Stable 2.7.0
- `course-package/learning-map.json`: نگاشت سطح → تمرین → Quiz → Project → Review
- `course-package/projects/registry.json`: مرجع canonical projectId
- `course-package/completion.json`: قرارداد graduation/certificate
- `course-package/release-candidate.json`: وضعیت release برابر stable

## Quality Gate
CI اعتبار JSON، یکتایی Lesson ID و order، Chapter/Level reference، Block Type، Project reference، Exercise/Quiz، Final Exam، Guided Rubric، Learning Map، Completion Path و Version Alignment را کنترل می‌کند.

این مخزن Course Package پایتون است. Runtime و قابلیت‌های مشترک اپ در `AS-Academy-Core` باقی می‌مانند تا منطق مشترک بین دوره‌ها تکرار نشود.
