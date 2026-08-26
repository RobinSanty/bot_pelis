import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import os

TOKEN = os.getenv("BOT_TOKEN")

logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Hola! Soy Peliculas_AdrecBros_bot 🎬\n\n"
        "Escribe el nombre de una peli y te respondo.\n"
        "Ej: Rapidos y furiosos 5"
    )

async def responder(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = update.message.text
    await update.message.reply_text(f"🔍 Buscaste: {texto}\n\nYa estoy vivo! En el siguiente paso le ponemos buscador real de pelis.")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, responder))

print("Bot iniciado")
app.run_polling()
