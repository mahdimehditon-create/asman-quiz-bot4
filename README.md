# Asman Quiz Bot (Render Edition)

ربات تلگرامی مبتنی بر Aiogram و OpenAI برای ساخت سوال از فایل‌های PDF و DOCX

## نصب و اجرا روی Render

1. پروژه را در GitHub قرار دهید.
2. در Render یک سرویس جدید Web Service بسازید.
3. تنظیمات زیر را قرار دهید:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `./start.sh`
4. Environment Variables مورد نیاز:
   - `API_TOKEN`: توکن ربات تلگرام
   - `OPENAI_API_KEY`: کلید هوش مصنوعی
   - `RENDER_EXTERNAL_URL`: آدرس پروژه بعد از Deploy
   - `PORT`: عدد 10000
5. بعد از Deploy:
   تنظیم Webhook در BotFather:
   ```bash
   /setwebhook https://your-service-name.onrender.com
   ```

ربات آماده است ✅