import sqlite3

conn = sqlite3.connect("logs.db", check_same_thread=False)
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    username TEXT,
    log_text TEXT,
    result TEXT,
    type TEXT,
    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

conn.commit()

def save_log(user_id, username, log_text, result, log_type):
    cur.execute(
        "INSERT INTO logs (user_id, username, log_text, result, type) VALUES (?, ?, ?, ?, ?)",
        (user_id, username, log_text, result, log_type)
    )
    conn.commit()

def get_logs(user_id):
    cur.execute("SELECT log_text, result, date FROM logs WHERE user_id=?", (user_id,))
    return cur.fetchall()