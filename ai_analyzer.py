from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def ai(text):
    prompt = f"""
You are a professional iPhone repair technician.

Analyze this panic log and give:
- Problem
- Component
- Root Cause
- Fix Steps
- Probability

{text}
"""

    res = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role":"user","content":prompt}]
    )

    return res.choices[0].message.content