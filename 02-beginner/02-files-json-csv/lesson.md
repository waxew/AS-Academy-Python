# File I/O، JSON و CSV

از `with open(...)` برای مدیریت امن resource استفاده کنید. Encoding محتوای فارسی را صریحاً UTF-8 قرار دهید.

```python
from pathlib import Path
path = Path("note.txt")
path.write_text("سلام Python", encoding="utf-8")
print(path.read_text(encoding="utf-8"))
```

JSON برای داده ساخت‌یافته و CSV برای داده جدولی ساده بررسی می‌شوند.
