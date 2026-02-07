from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
import os

TOKEN = os.getenv("TELEGRAM_TOKEN")

MAIN_KEYBOARD = ReplyKeyboardMarkup(
    [
        ["🍽 Меню", "☕ Напитки"],
        ["🎁 Акции", "📍 Адрес и часы"],
        ["🚕 Такси"],
        ["💬 Задать вопрос"]
    ],
    resize_keyboard=True
)

MENU_KEYBOARD = ReplyKeyboardMarkup(
    [
        ["🥓 Savory Waffles", "🍓 Sweet Waffles"],
        ["🧇 Bases & Extras"],
        ["⬅️ Назад"]
    ],
    resize_keyboard=True
)

BACK_KEYBOARD = ReplyKeyboardMarkup([["⬅️ Назад"]], resize_keyboard=True)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Добро пожаловать в cafe “FRAU WAFFLE” 🧇\nВыберите, что вас интересует 👇",
        reply_markup=MAIN_KEYBOARD
    )

async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "🍽 Меню":
        await update.message.reply_text(
            "Наши вафли 🧇\nВыберите категорию:",
            reply_markup=MENU_KEYBOARD
        )

    elif text == "🥓 Savory Waffles":
        await update.message.reply_text(
            "🥓 Savory Waffles\n\n"
            "• Bacon & Cheese — 39\n"
            "• Salmon — 79\n"
            "• Caesar — S/L 39 / 69\n"
            "• Vegetarian — S/L 39 / 59\n"
            "• Chicken & Mushroom — S/L 39 / 69\n"
            "• Cheeseburger — 99\n"
            "• Shrimp — 119",
            reply_markup=BACK_KEYBOARD
        )

    elif text == "🍓 Sweet Waffles":
        await update.message.reply_text(
            "🍓 Sweet Waffles\n\n"
            "• Matcha Strawberry — 89 / 110\n"
            "• Banoffee — 79 / 99\n"
            "• Tropicana — 79 / 99\n"
            "• Snickers — 119 / 129\n"
            "• Sweet Dragon — 79 / 99\n"
            "• Clockwork Orange — 79 / 99",
            reply_markup=BACK_KEYBOARD
        )

    elif text == "🧇 Bases & Extras":
        await update.message.reply_text(
            "🧇 Waffle Bases — 29\n"
            "Classic / Spinach / Sweet / Cheese\n\n"
            "➕ Extras — 19\n"
            "Strawberry jam\nChocolate topping\nIce cream\nSalted caramel",
            reply_markup=BACK_KEYBOARD
        )

    elif text == "☕ Напитки":
        await update.message.reply_text(
            "☕ Coffee\n"
            "Espresso — 39\nAmericano — 39\n"
            "Cappuccino — 59\nLatte — 59\nFlat White — 59\n"
            "Raf — 65\nMochaccino — 69\n\n"
            "🍫 Cocoa\nCocoa — 39\nViennese Cocoa — 49\n\n"
            "🥤 Cold & Special\nVietnamese Coffee — 59\nBumble Fresh — 79\n"
            "Matcha — 59\nMatcha with Salted Cream — 69\n\n"
            "🍹 Lemonades & Soda\nSoda — 20\nLemonades — 35",
            reply_markup=BACK_KEYBOARD
        )

    elif text == "🎁 Акции":
        await update.message.reply_text(
            "🎁 Акции сегодня\n"
            "• Вафля + кофе — выгодно\n"
            "• Сладкая вафля + напиток — специальная цена",
            reply_markup=BACK_KEYBOARD
        )

    elif text == "📍 Адрес и часы":
        chat_id = update.effective_chat.id

        latitude = 12.2525
        longitude = 109.1967

        await context.bot.send_location(
            chat_id=chat_id,
            latitude=latitude,
            longitude=longitude
        )

        await context.bot.send_message(
            chat_id=chat_id,
            text=(
                "📍 cafe “FRAU WAFFLE”\n"
                "Nha Trang, Vietnam\n\n"
                "🗺 Google Maps:\n"
                "https://www.google.com/maps/search/?api=1&query=Frau+Waffle+Nha+Trang\n\n"
                "⏰ Часы работы: 09:00–19:00"
            ),
            reply_markup=BACK_KEYBOARD
        )

    elif text == "🚕 Такси":
        await update.message.reply_text(
            "🚕 Заказать такси до cafe “FRAU WAFFLE”\n\n"
            "Grab:\nhttps://www.grab.com\n\n"
            "Gojek:\nhttps://www.gojek.com\n\n"
            "Maxim:\nhttps://taximaxim.com",
            reply_markup=BACK_KEYBOARD
        )

    elif text == "💬 Задать вопрос":
        await update.message.reply_text(
            "Напишите вопрос 👇\n(ответ от AI подключим следующим шагом)",
            reply_markup=BACK_KEYBOARD
        )

    elif text == "⬅️ Назад":
        await update.message.reply_text(
            "Вы в главном меню 👇",
            reply_markup=MAIN_KEYBOARD
        )

    else:
        await update.message.reply_text(
            "🤖 (AI ответ будет здесь)",
            reply_markup=BACK_KEYBOARD
        )

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle))
app.run_polling() 
