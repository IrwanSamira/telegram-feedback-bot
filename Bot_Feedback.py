from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
import os

TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")

async def feedback_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    message = update.message.text

    await update.message.reply_text(f"Terima kasih {user.first_name}, feedback kamu sudah dikirim ke admin!")
    feedback_text = f"**Feedback Baru!**\n\nDari: {user.first_name} (@{user.username or 'tanpa username'})\n\nIsi:\n{message}"
    await context.bot.send_message(chat_id=CHANNEL_ID, text=feedback_text, parse_mode='Markdown')

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, feedback_handler))

app.run_polling()