from telegram import *
from telegram.ext import *

from analyzer import search, format_res
from ai_analyzer import ai
from database import save_log, get_logs

TOKEN = "PUT_TOKEN"

def menu():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🔍 Search Code", callback_data="search")],
        [InlineKeyboardButton("📄 Analyze Log", callback_data="analyze")],
        [InlineKeyboardButton("🤖 AI Analyze", callback_data="ai")],
        [InlineKeyboardButton("📜 My Logs", callback_data="logs")],
    ])

async def start(update: Update, context):
    await update.message.reply_text("👋 YCZ Panic Analyzer PRO", reply_markup=menu())

async def buttons(update: Update, context):
    q = update.callback_query
    await q.answer()

    if q.data == "search":
        context.user_data["mode"] = "search"
        await q.message.reply_text("Send code")

    elif q.data == "analyze":
        context.user_data["mode"] = "analyze"
        await q.message.reply_text("Send log")

    elif q.data == "ai":
        context.user_data["mode"] = "ai"
        await q.message.reply_text("Send log for AI")

    elif q.data == "logs":
        logs = get_logs(q.from_user.id)

        if not logs:
            await q.message.reply_text("No logs")
            return

        msg = ""
        for log, res, date in logs[-5:]:
            msg += f"{date}\n{log[:30]}...\n\n"

        await q.message.reply_text(msg[:4000])

async def text(update: Update, context):
    mode = context.user_data.get("mode", "search")
    t = update.message.text

    user_id = update.message.from_user.id
    username = update.message.from_user.username or "unknown"

    if mode in ["search", "analyze"]:
        r = search(t)
        msg = format_res(r)

        if msg:
            await update.message.reply_text(msg[:4000])
            save_log(user_id, username, t, msg, "basic")
        else:
            await update.message.reply_text("Not found")

    elif mode == "ai":
        result = ai(t)
        await update.message.reply_text(result[:4000])
        save_log(user_id, username, t, result, "ai")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(buttons))
app.add_handler(MessageHandler(filters.TEXT, text))

app.run_polling()