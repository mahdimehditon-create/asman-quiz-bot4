import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_questions(text: str, count: int = 5) -> list:
    prompt = f"""
    از متن زیر {count} سؤال تستی چهارگزینه‌ای بساز.
    گزینه‌ها منطقی باشند و جواب درست را با علامت (*) مشخص کن.

    متن:
    {text}
    """

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "شما سازنده‌ی سوالات آموزشی هستید."},
            {"role": "user", "content": prompt}
        ]
    )
    result = completion.choices[0].message.content
    questions = result.split("

")
    return [q.strip() for q in questions if q.strip()]
