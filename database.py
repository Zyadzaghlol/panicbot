import sqlite3

conn = sqlite3.connect("bot.db", check_same_thread=False)
cur = conn.cursor()

# users
cur.execute("""
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    username TEXT,
    plan TEXT DEFAULT 'free',
    expire_date TEXT
)
""")

# logs
cur.execute("""
CREATE TABLE IF NOT EXISTS logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    log TEXT,
    result TEXT,
    type TEXT,
    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

conn.commit()

# ===== USERS =====
def add_user(user_id, username):
    cur.execute("INSERT OR IGNORE INTO users (user_id, username) VALUES (?, ?)", (user_id, username))
    conn.commit()

def get_user(user_id):
    cur.execute("SELECT plan, expire_date FROM users WHERE user_id=?", (user_id,))
    return cur.fetchone()

def set_vip(user_id, days):
    cur.execute(
        "UPDATE users SET plan='vip', expire_date=datetime('now', ? || ' days') WHERE user_id=?",
        (days, user_id)
    )
    conn.commit()

# ===== LOGS =====
def save_log(user_id, log, result, t):
    cur.execute(
        "INSERT INTO logs (user_id, log, result, type) VALUES (?, ?, ?, ?)",
        (user_id, log, result, t)
    )
    conn.commit()

def get_logs(user_id):
    cur.execute("SELECT log, result, date FROM logs WHERE user_id=? ORDER BY id DESC LIMIT 5", (user_id,))
    return cur.fetchall()