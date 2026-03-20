from panic_db import PANIC_DB

def search(text):
    text = text.upper()
    res = []

    for code, data in PANIC_DB.items():
        if code in text:
            res.append((code, data))

    return res

def format_res(res):
    if not res:
        return None

    msg = "🔍 Diagnosis:\n\n"

    for code, d in res:
        msg += f"📌 {code}\n"
        msg += f"📂 {d['cat']}\n"
        msg += f"🔧 {d['issue']}\n"
        msg += f"⚠️ {d['p']}\n"
        msg += "🛠 Fix:\n"

        for f in d["fix"]:
            msg += f" - {f}\n"

        msg += "\n"

    return msg