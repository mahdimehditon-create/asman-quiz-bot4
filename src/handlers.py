from aiogram import Router, F
from aiogram.types import Message
from aiogram.enums import ParseMode
import os
from .extractor import extract_text_from_pdf, extract_text_from_docx
from .ai_generator import generate_questions

router = Router()

@router.message(F.document)
async def handle_file(message: Message):
    file = message.document
    file_name = file.file_name
    file_path = f"./downloads/{file_name}"
    await message.bot.download(file, destination=file_path)

    if file_name.lower().endswith(".pdf"):
        text = extract_text_from_pdf(file_path)
    elif file_name.lower().endswith(".docx"):
        text = extract_text_from_docx(file_path)
    else:
        await message.reply("فرمت فایل پشتیبانی نمی‌شود ❌")
        return

    questions = generate_questions(text)
    result = "

".join(questions)
    await message.reply(f"✅ سؤالات ساخته شد:

<pre>{result}</pre>", parse_mode=ParseMode.HTML)
