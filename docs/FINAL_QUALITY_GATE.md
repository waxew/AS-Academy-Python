# AS Academy Python — Final Quality Gate

این سند معیار خروج دوره از حالت توسعه محتوایی و ورود به Release Candidate را مشخص می‌کند.

## 1. Coverage Gate

دوره باید مسیرهای Fundamentals، Beginner، Intermediate، Advanced، Specialist و Project-Based را پوشش دهد. هر موضوع کلیدی باید حداقل یک محتوای آموزشی و در موضوعات مهارتی حداقل یک فعالیت عملی داشته باشد.

## 2. Lesson Gate

هر درس runtime باید شناسه پایدار، chapter معتبر، عنوان، خلاصه، زمان تقریبی و blockهای معتبر Core داشته باشد. درس تخصصی باید فقط تعریف نباشد و حداقل یکی از Code، Exercise، Quiz، Project، Diagram یا عملیاتی مشابه داشته باشد.

## 3. Assessment Gate

- Exercise Bank برای تمرین مستقل
- Quiz Bank برای بازیابی سریع دانش
- Final Exam برای ارزیابی پایان دوره
- Guided Projects برای ارزیابی مهارت ترکیبی
- Spaced Practice برای مرور پس از عبور از سطح
- حداقل نمره checkpoint: 80%
- حداقل نمره آزمون نهایی: 70%

## 4. Project Gate

Guided Project باید milestones، acceptance criteria، estimated effort و rubric صد امتیازی داشته باشد. Capstone باید domain، database، API یا interface، security، tests، deployment/CI و documentation را در یک محصول قابل دفاع ترکیب کند.

## 5. Production Skills Gate

دانشجو قبل از پایان دوره باید با این مفاهیم کار کرده باشد: Git، testing، debugging، logging، database transaction، authentication/authorization، secret management، Docker، deployment، healthcheck، observability، backup/restore و rollback.

## 6. AI/Data Gate

مسیر تخصصی داده و AI باید Data Cleaning، Visualization، ML Evaluation، Deep Learning، NLP/Transformers، Computer Vision، RAG، AI Evaluation و Agent/Tool Safety را پوشش دهد.

## 7. Integrity Gate

CI باید JSONها، IDها، referenceها، project registry، assessment bank، completion path، version alignment و guided project rubrics را بررسی کند. Release Candidate فقط زمانی معتبر است که HEAD branch در CI سبز باشد.

## 8. Source of Truth

`course-package/` منبع app-facing دوره Python است. قابلیت‌های عمومی UI، navigation، progress، quiz engine، exercise engine، search، bookmark، settings و content runtime در `AS-Academy-Core` قرار می‌گیرند و نباید در این repository تکرار شوند.

## 9. Definition of Done

دوره از نظر curriculum زمانی Final محسوب می‌شود که:

1. تمام سطح‌ها مسیر آموزشی پیوسته داشته باشند.
2. هیچ lesson/chapter/project reference شکسته وجود نداشته باشد.
3. assessment و projectها فقط نمایشی نباشند و معیار قبولی داشته باشند.
4. مباحث تخصصی مهم به تمرین یا پروژه متصل باشند.
5. CI روی HEAD سبز باشد.
6. README و اسناد وضعیت با ساختار واقعی Course Package همگام باشند.
7. توسعه بعدی عمدتاً بهبود/به‌روزرسانی باشد، نه پر کردن شکاف بنیادی curriculum.
