from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def ai_analyze(text):
    try:
        res = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role":"system","content":"You are iPhone repair expert"},
                {"role":"user","content":text}
            ]
        )
        return res.choices[0].message.content

    except Exception as e:
        return f"⚠️ AI Error: {str(e)}"