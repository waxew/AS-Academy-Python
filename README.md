# AS Academy Python

دوره Python در معماری جدید AS Academy.

## معماری رسمی

از این نسخه، مسئولیت‌ها بین سه لایه مشترک و ریپوی دوره تقسیم شده‌اند:

- `AS-Academy-Core`: هسته پردازش، مدل‌ها، Content Runtime، Progress، Search، Quiz/Exercise Engine، Bookmark، Settings و منطق مشترک.
- `AS-Academy-MainUi`: رابط کاربری و Design System مشترک همه برنامه‌های Academy.
- `AS-Academy-MainCourse`: منبع واحد همه درس‌ها، فصل‌ها، تمرین‌ها، Quizها، آزمون‌ها، پروژه‌ها، Capstone و metadata آموزشی.
- `AS-Academy-Python`: هویت و سازگاری اختصاصی Python و نقطه اتصال این دوره به معماری مشترک.

## منبع اصلی محتوای Python

Source of Truth جدید:

`AS-Academy-MainCourse/courses/python/course/`

محتوای موجود در `course-package/` این ریپو Snapshot سازگاری/مهاجرت نسخه 2.7.0 است و از این پس محتوای آموزشی جدید مستقیماً در MainCourse نگهداری می‌شود.

## مسیر آموزشی

Python همچنان شش سطح رسمی دارد:

1. Fundamentals — مبانی
2. Beginner — مقدماتی
3. Intermediate — متوسط
4. Advanced — پیشرفته
5. Specialist — تخصصی
6. Project-Based — پروژه‌محور

مسیر کامل شامل Lesson، Code Example، Exercise، Quiz، Review Checkpoint، Level Project، Final Exam، Guided Portfolio و Production Capstone است.

## وضعیت نسخه

آخرین Snapshot تثبیت‌شده دوره: **2.7.0 Stable**.

محتوای آن شامل مسیر کامل Python از Syntax و OOP تا Database، Backend، Desktop، Automation، Bot، Data Science، Machine Learning، Deep Learning، RAG/Agents، Network/Security، Testing و Deployment است.

## قانون توسعه از اینجا به بعد

- تغییر محتوای آموزشی → فقط `AS-Academy-MainCourse/courses/python/course/`
- تغییر UI مشترک → فقط `AS-Academy-MainUi`
- تغییر منطق/Runtime مشترک → فقط `AS-Academy-Core`
- تغییر Branding/Capability/Integration اختصاصی Python → `AS-Academy-Python`

نباید Lesson، Quiz، Exercise یا منطق UI مشترک جدید به‌صورت مستقل و تکراری داخل این ریپو ایجاد شود.

## وضعیت legacy

دایرکتوری‌های قدیمی و `course-package/` فعلاً حذف نشده‌اند تا migration بدون از دست رفتن داده و با امکان مقایسه/rollback انجام شود. پس از تأیید کامل MainCourse، می‌توان آن‌ها را Archive یا حذف کرد.
