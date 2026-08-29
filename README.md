# AS Academy Python

دوره جامع و پروژه‌محور Python در AS Academy؛ از اولین خط کد تا طراحی، تست و استقرار سیستم‌های Production.

> محتوای اختصاصی Python در این repository نگهداری می‌شود. زیرساخت مشترک برنامه آموزشی شامل Navigation، Design System، Progress، Quiz/Exercise Engine، Search، Bookmark، Settings و Content Runtime در `AS-Academy-Core` قرار دارد.

## نسخه دوره

Current curriculum: **2.5.x → Final Curriculum hardening**

منبع اصلی محتوای قابل مصرف توسط برنامه: `course-package/`

## مسیر شش‌سطحی

### 1. Fundamentals — مبانی
Python و نصب محیط، Syntax، متغیر و Type، I/O، String، Operator، Condition، Loop، Collection و Function.

### 2. Beginner — مقدماتی
Module/Package، venv/pip، pathlib، File I/O، JSON/CSV/XML، Exception، Debugging/Logging و Comprehension.

### 3. Intermediate — متوسط
OOP، Composition/Inheritance، Dataclass، Value Object، Type Hints، Protocol/Generic، Iterator، Generator و Domain Modeling.

### 4. Advanced — پیشرفته
Decorator، Closure، Context Manager، Object/Memory Model، Standard Library حرفه‌ای، Threading/Lock/Queue، Multiprocessing، AsyncIO، Testing، Packaging، Profiling، Complexity و Algorithmic Thinking.

### 5. Specialist — تخصصی
- Database: SQLite، PostgreSQL، MySQL، SQL Server، SQLAlchemy، ORM، Migration، Transaction و Index
- Backend: HTTP/REST، Flask، FastAPI، Django/DRF، Validation، OAuth2/JWT/RBAC، WebSocket
- Desktop: Tkinter، CustomTkinter، PySide/PyQt و معماری UI
- Automation: Requests، BeautifulSoup، Selenium، Playwright و resilient automation
- Bots: Telegram و Discord، command/event/state architecture
- Data: NumPy، Pandas، Matplotlib، data cleaning و analysis
- ML: scikit-learn، feature engineering، leakage، evaluation
- Deep Learning: PyTorch، TensorFlow/Keras
- NLP/AI: Transformers/Hugging Face، LLM، Embedding، Vector DB، RAG، AI Agents و evaluation
- Vision: OpenCV و image inference
- Network/Security: Socket، TCP/UDP، TLS، validation، secret management و secure coding
- Production: Linux/SSH، Uvicorn/Gunicorn، Nginx، Docker/Compose، CI/CD، Cloud/VPS، Observability، Backup/Restore و Rollback

### 6. Project-Based — پروژه‌محور
پروژه‌های مرحله‌ای، Guided Projects، Portfolio، Final Exam و Production Capstone.

## سیستم یادگیری

```text
Level
  -> Chapter
    -> Lesson
      -> Code Example
      -> Exercise
      -> Quiz
    -> Review Checkpoint
  -> Level Project
-> Final Exam
-> Guided Portfolio
-> Production Capstone
```

دوره علاوه بر درس از Exercise Bank، Quiz Bank، Final Exam، Guided Project Rubrics و Spaced Practice استفاده می‌کند.

## پروژه‌ها

پروژه‌ها از ماشین‌حساب، Todo و مدیریت نمره شروع می‌شوند و تا Library/Inventory، Desktop CRM، Billing API، Django، Automation، Bots، Data Dashboard، ML، PyTorch، RAG و Production Capstone ادامه دارند.

Guided Projectها دارای Milestone، Acceptance Criteria، زمان تقریبی و Rubric صد امتیازی هستند.

## ساختار اصلی

```text
AS-Academy-Python/
├── course-package/
│   ├── manifest.json
│   ├── levels.json
│   ├── chapters.json
│   ├── lessons/
│   ├── exercises/
│   ├── quizzes/
│   ├── assessment/
│   ├── projects/
│   ├── review/
│   ├── glossary.json
│   └── completion.json
├── src/
├── tests/
├── docs/
├── exercises/
├── projects/
├── cheatsheets/
├── pyproject.toml
└── README.md
```

## کیفیت محتوا

CI صحت JSON، شناسه درس‌ها، Chapter/Level references، Core block types، Project Registry، Assessment Bank، Completion Path، Version Alignment و قرارداد Guided Projectها را کنترل می‌کند.

معیار نهایی دوره در `docs/FINAL_QUALITY_GATE.md` تعریف شده است.

## هدف نهایی

فارغ‌التحصیل مسیر کامل باید بتواند مسئله را تحلیل کند، Python تمیز بنویسد، داده و دیتابیس را مدیریت کند، تست بنویسد، API یا برنامه کاربردی بسازد، امنیت پایه را رعایت کند، سیستم را containerize/deploy کند و حداقل یک پروژه Production قابل دفاع در Portfolio داشته باشد.
