from panic_db import PANIC_DB

def analyze(text):
    text = text.upper()
    found = []

    for code, data in PANIC_DB.items():
        if code in text:
            found.append((code, data))

    if not found:
        return None

    msg = "🔍 Result:\n\n"

    for code, d in found:
        msg += f"📌 {code}\n{d['issue']}\n"
        for f in d["fix"]:
            msg += f"- {f}\n"
        msg += "\n"

    return msg