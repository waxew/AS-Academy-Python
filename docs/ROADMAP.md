# Roadmap — AS Academy Python

## نسخه‌های تکمیل‌شده
- v1.x — پایه دوره، Course Package، Fundamentals تا Specialist و Capstone
- v2.0 — مسیر شش‌سطحی و graduation metadata
- v2.1 — Stabilization و Validator سراسری
- v2.2 — Deep Learning، NLP، Computer Vision و AI production
- v2.3 — Database/Backend/GUI/Automation/Bot/Network/Security/DevOps expansion
- v2.4 — 30 Exercise، 30 Quiz و Project Registry مرکزی
- v2.5 — Guided Projects، Acceptance Criteria و Rubric صد امتیازی
- v2.6 — Algorithms/Stdlib/Memory/Descriptors، Hugging Face، Agents، Cloud، Backup و Spaced Practice
- v2.7 — Final Exam چهل‌سؤالی، Learning Map ماشین‌خوان، Guided Portfolio گسترده، QA سخت‌گیرانه و Stable Course Package

## وضعیت Stable 2.7.0
مسیر آموزشی از FUNDAMENTALS تا PROJECT_BASED تعریف شده و graduation شامل درس‌های اجباری، تمرین و Quiz، پروژه‌های سطحی، Review Checkpoint، Final Exam و Production Capstone است.

`course-package/` منبع حقیقت محتوای قابل مصرف توسط اپ است. `learning-map.json` اتصال deterministic سطح‌ها به Exercise، Quiz، Project و Review را مشخص می‌کند. `projects/registry.json` مرجع canonical شناسه پروژه‌ها است.

## توسعه‌های بعد از Stable
نسخه‌های بعدی فقط در صورت نیاز واقعی آموزشی منتشر می‌شوند: افزودن مسئله‌های بیشتر، به‌روزرسانی کتابخانه‌ها/فریم‌ورک‌ها، پروژه‌های تخصصی جدید، یا تغییر قرارداد Core. این موارد مانع Stable بودن v2.7 نیستند.

## اصل معماری
منطق مشترک اپلیکیشن، Navigation، Progress، Quiz Engine، Exercise Engine، Search، Bookmark و Content Engine در `AS-Academy-Core` نگهداری می‌شود. این مخزن فقط محتوای Python و metadata اختصاصی دوره را نگهداری می‌کند.
