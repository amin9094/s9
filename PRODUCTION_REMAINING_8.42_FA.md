# مرحلهٔ باقی‌ماندهٔ انتشار نهایی

تأییدهای واقعی هنوز لازم‌اند؛ این راهنما به‌تنهایی گواهی نیست.

1. lockها با ابزار موجود و toolchain اعلام‌شده روی CPython 3.12 تولید شوند؛ نصب تمیز و کنترل hash مستقل لازم است. در فایل فعلی این کار تأیید نشده است.
2. Full Ruff/Mypy/Bandit و پوشش ۴۰٪ کلی / ۸۵٪ حساس باید موفق شوند؛ محدودیت‌ها در گزارش اصلی‌اند.
3. image واقعی ساخته و digest دقیق آن در SENTINEL_IMAGE_DIGEST ثبت شود. alias قبلی SENTINEL_DOCKER_IMAGE_DIGEST نیز پشتیبانی می‌شود؛ دو مقدار متعارض رد می‌شوند.
4. TEST_DATABASE_URL، TEST_REDIS_URL و TEST_BOT_TOKEN باید سرویس‌های جدا از production باشند. TEST_PUBLIC_CHANNEL_ID و TEST_PRIVATE_CHANNEL_ID باید دو کانال آزمایشی مجزا با مجوز کامل مدیر باشند. برنامهٔ production acceptance می‌تواند در همین کانال‌های آزمایشی پیام بفرستد و پاک کند؛ آن را فقط با این هدف و تنظیمات اجرا کنید.
5. `python scripts/production_acceptance.py --base-url https://YOUR_DEPLOYMENT` باید بدون skip و با همهٔ checks موفق شود. گزارش به source SHA و image digest متصل است و تا ۲۴ ساعت معتبر است. خروجی فعلی چنین قبولی ندارد.
6. کانکتور در MetaEditor رسمی کامپایل و روی حساب demo، اتصال، احراز هویت، محدودیت ریسک، همگام‌سازی سیگنال و بازیابی قطع ارتباط آزموده شود. شاهد اپراتور در quality-artifacts/mt5_demo_acceptance.json ثبت می‌شود؛ نمونهٔ فاقد قبولی در mt5_demo_acceptance.example.json است. این سند نمی‌تواند اجرای واقعی MetaEditor را انجام دهد یا صحت شاهد اپراتور را مستقلاً اثبات کند.
7. /start، دکمه‌ها، Back، تکرار پرداخت، CRM، پاداش‌ها و مینی‌اپ روی image واقعی بررسی و حداقل ۲۴ ساعت پایش شوند.

برای پذیرش production، `quality_gate.py --release-channel production` و سپس release gate سخت‌گیر لازم‌اند. گزینه‌های candidate نباید به‌عنوان قبولی production معرفی شوند.
