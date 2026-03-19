import os

def ai_analyze(text):
    try:
        from openai import OpenAI
        client = OpenAI()

        prompt = f"""
Analyze this iPhone panic log.

Give:
- Problem
- Component
- Fix
- Probability

{text}
"""

        res = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[{"role": "user", "content": prompt}]
        )

        return res.choices[0].message.content

    except:
        return "⚠️ AI failed or no API key"