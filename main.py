import os
import logging
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder,ContextTypes,MessageHandler,filters
from chatbot import chat

# Load .env to get Telegram token
load_dotenv()
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

# Logging for debug
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# 📩 Handle incoming messages
async def handle_message(update:Update,context:ContextTypes.DEFAULT_TYPE):
    user_input = update.message.text
    reply =await chat(user_input)   # Call chatbot logic
    await update.message.reply_text(reply)

# 🚀 Start the Telegram bot
if __name__ == "__main__":
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("🤖 G-One is now running on Telegram... (Press Ctrl+C to stop)")
    app.run_polling()