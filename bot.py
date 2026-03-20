from telegram import *
from telegram.ext import *

from config import TOKEN, ADMIN_ID
from analyzer import analyze
from ai_analyzer import ai_analyze
from database import *

# ===== MENU =====
def menu():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🔍 Analyze", callback_data="analyze")],
        [InlineKeyboardButton("🤖 AI", callback_data="ai")],
        [InlineKeyboardButton("📜 Logs", callback_data="logs")],
        [InlineKeyboardButton("💎 Upgrade", callback_data="vip")]
    ])

def admin_menu():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("➕ Add VIP", callback_data="addvip")]
    ])

# ===== START =====
async def start(update: Update, context):
    user = update.effective_user
    add_user(user.id, user.username)

    await update.message.reply_text(
        "👋 YCZ Panic Analyzer PRO",
        reply_markup=menu()
    )

# ===== BUTTONS =====
async def buttons(update: Update, context):
    q = update.callback_query
    await q.answer()

    uid = q.from_user.id

    if q.data == "analyze":
        context.user_data["mode"] = "analyze"
        await q.message.reply_text("Send panic log")

    elif q.data == "ai":
        context.user_data["mode"] = "ai"
        await q.message.reply_text("Send log for AI")

    elif q.data == "logs":
        logs = get_logs(uid)
        if not logs:
            await q.message.reply_text("No logs")
            return

        msg = ""
        for l, r, d in logs:
            msg += f"{d}\n{l[:30]}...\n\n"

        await q.message.reply_text(msg)

    elif q.data == "vip":
        await q.message.reply_text("💎 Contact admin to upgrade")

    elif q.data == "addvip" and uid == ADMIN_ID:
        context.user_data["mode"] = "addvip"
        await q.message.reply_text("Send user_id days")

# ===== TEXT =====
async def text(update: Update, context):
    uid = update.effective_user.id
    t = update.message.text
    mode = context.user_data.get("mode")

    # ADMIN
    if mode == "addvip" and uid == ADMIN_ID:
        try:
            user_id, days = t.split()
            set_vip(int(user_id), int(days))
            await update.message.reply_text("✅ VIP added")
        except:
            await update.message.reply_text("Format: user_id days")
        return

    # NORMAL
    if mode == "analyze":
        res = analyze(t)
        if res:
            await update.message.reply_text(res)
            save_log(uid, t, res, "basic")
        else:
            await update.message.reply_text("Not found")

    elif mode == "ai":
        res = ai_analyze(t)
        await update.message.reply_text(res[:4000])
        save_log(uid, t, res, "ai")

# ===== RUN =====
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(buttons))
app.add_handler(MessageHandler(filters.TEXT, text))

app.run_polling()