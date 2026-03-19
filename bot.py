from telegram import Update
from telegram.ext import *
from analyzer import analyze_basic
from ai_analyzer import ai_analyze

import os

TOKEN = os.getenv("TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 iPhone Panic Analyzer Bot\n\nSend panic log or file."
    )

async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    basic = analyze_basic(text)

    if basic:
        await update.message.reply_text(basic[:4000])
    else:
        ai = ai_analyze(text)
        await update.message.reply_text("🤖 AI Analysis:\n\n" + ai[:4000])

async def handle_file(update: Update, context: ContextTypes.DEFAULT_TYPE):
    file = await update.message.document.get_file()
    content = await file.download_as_bytearray()
    text = content.decode("utf-8", errors="ignore")

    basic = analyze_basic(text)

    if basic:
        await update.message.reply_text(basic[:4000])
    else:
        ai = ai_analyze(text)
        await update.message.reply_text("🤖 AI Analysis:\n\n" + ai[:4000])

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT, handle_text))
app.add_handler(MessageHandler(filters.Document.ALL, handle_file))

app.run_polling()