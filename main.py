# Works with python3.10

from telegram.ext import ApplicationBuilder, CommandHandler
from config import TOKEN
from telegram_functions import *
from database import init_db

init_db()

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("enter", enter))
app.add_handler(CommandHandler("exit", exit))

app.run_polling()


