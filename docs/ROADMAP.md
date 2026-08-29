# Roadmap — AS Academy Python

## نسخه‌های تکمیل‌شده
- v1.0 — معماری اولیه دوره، مثال‌ها، تست و metadata
- v1.1 — Course Package سازگار با AS Academy Core
- v1.2 — گسترش Lesson/Exercise/Quiz/Project و Specialist tracks
- v1.3 — تکمیل عمیق Fundamentals و Beginner همراه پروژه هدایت‌شده
- v1.4 — تکمیل Intermediate و Advanced
- v1.5 — گسترش Specialist و Production Capstone
- v2.0 — مسیر شش‌سطحی کامل، آزمون نهایی و graduation metadata
- v2.1 — Stabilization، حذف محتوای duplicate و Validator سراسری
- v2.2 — Deep Learning، PyTorch، TensorFlow/Keras، NLP، Computer Vision و AI production
- v2.3 — Database/Backend/GUI/Automation/Bot/Networking/Security/DevOps expansion

## فاز جاری — v2.4 Assessment & Portfolio Hardening
- افزایش Exercise Bank از 15 به 30 تمرین
- افزایش Quiz Bank از 14 به 30 سؤال
- رجیستری واحد برای projectIdهای درسی و Portfolio
- Validation خودکار Exercise/Quiz/Project/Completion در CI
- هماهنگ‌سازی مستندات با وضعیت واقعی دوره

## فاز بعد
- پروژه‌های Guided چندمرحله‌ای برای Trackهای اصلی
- Rubric و Acceptance Criteria برای Portfolio
- افزایش سناریوهای آزمون جامع و Review/Spaced Practice
- Release Candidate و QA نهایی Course Package

## اصل معماری
منطق مشترک اپلیکیشن، Navigation، Progress، Quiz Engine، Exercise Engine، Search، Bookmark و Content Engine در `AS-Academy-Core` نگهداری می‌شود. این مخزن فقط محتوای Python و metadata اختصاصی دوره را نگهداری می‌کند.
