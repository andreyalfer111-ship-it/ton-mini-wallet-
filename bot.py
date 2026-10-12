import logging
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder

# Токен вашего бота от BotFather
TOKEN = "8679558042:AAHc9Rd2A1bmXic03L_BggnffQVX4dsWFvc"

# Ваш Telegram ID
MY_ID = 8790592838

# Ссылка на ваше Mini App
WEBAPP_URL = "https://t.me/Waltpaytg_bot/myapp"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("ton"))
async def cmd_ton(message: types.Message):
    if message.from_user.id != MY_ID:
        return

    args = message.text.split(maxsplit=1)
    if len(args) < 2:
        await message.answer("⚠️ Укажите сумму, например: `/ton 1.5`", parse_mode="Markdown")
        return

    amount = args[1]
    
    builder = InlineKeyboardBuilder()
    builder.button(
        text=f"💎 Оплатить {amount} TON",
        web_app=types.WebAppInfo(url=f"{WEBAPP_URL}?startapp=ton_{amount}")
    )
    
    await message.answer(
        f"💎 **Чек на оплату TON**\n\nСумма: `{amount} TON`",
        reply_markup=builder.as_markup(),
        parse_mode="Markdown"
    )

@dp.message(Command("stars"))
async def cmd_stars(message: types.Message):
    if message.from_user.id != MY_ID:
        return

    args = message.text.split(maxsplit=1)
    if len(args) < 2:
        await message.answer("⚠️ Укажите сумму, например: `/stars 50`", parse_mode="Markdown")
        return

    amount = args[1]
    
    builder = InlineKeyboardBuilder()
    builder.button(
        text=f"⭐ Оплатить {amount} Stars",
        web_app=types.WebAppInfo(url=f"{WEBAPP_URL}?startapp=stars_{amount}")
    )
    
    await message.answer(
        f"⭐ **Чек на оплату Stars**\n\nСумма: `{amount} ⭐`",
        reply_markup=builder.as_markup(),
        parse_mode="Markdown"
    )

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(dp.start_polling(bot))
