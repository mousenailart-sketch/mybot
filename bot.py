import asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8968909917:AAGoIN0H6iH5skp3Qc64wFacQDwmHzHSx30"
LINK_УРОКА = "https://t.me/maniac_nails"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    nombre = update.effective_user.first_name
    mensaje = (
        f"¡Hola, {nombre}! 👋\n\n"
        "Soy Maria Bondar — instructora de manicura rápida "
        "y maestra con 14 años de experiencia. 💅\n\n"
        "Mi récord personal: corrección completa en solo *45 minutos*. ⚡\n\n"
        "Hoy quiero regalarte mi lección:\n"
        "*«Corrección de almendra larga en 55 minutos»*\n\n"
        "✅ Retirar el gel en 3–7 min sin usar lima\n"
        "✅ Manicura combinada en 10–15 min\n"
        "✅ Aplicar la base en 5 min\n"
        "✅ Reforzar uñas por 4 dedos a la vez 🔥\n"
        "✅ Mi esquema de limado en 7 minutos\n\n"
        "⏳ ¡Tienes 10 minutos para ver la lección!"
    )
    кнопка = InlineKeyboardMarkup([
        [InlineKeyboardButton("👉 Ver la lección gratis", url=LINK_УРОКА)]
    ])
    await update.message.reply_text(mensaje, parse_mode="Markdown", reply_markup=кнопка)

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("✅ Бот запущен!")
    app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()