from panic_db import PANIC_DB

def detect_type(text):
    t = text.lower()
    if "aop panic" in t:
        return "AOP PANIC"
    elif "watchdog" in t:
        return "WATCHDOG"
    elif "baseband" in t:
        return "BASEBAND"
    return "UNKNOWN"

def analyze_basic(text):
    text_up = text.upper()
    found = []

    for key in PANIC_DB:
        if key in text_up:
            found.append((key, PANIC_DB[key]))

    if not found:
        return None

    result = f"🔍 Panic Type: {detect_type(text)}\n\n"

    for code, data in found:
        result += f"📌 {code}\n"
        result += f"🔧 {data['issue']}\n"
        result += f"🛠 {data['fix']}\n\n"

    return result