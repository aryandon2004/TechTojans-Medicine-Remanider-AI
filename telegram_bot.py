from telegram import Bot
import asyncio

TOKEN = '8195218120:AAG6fnCkS6I1XCdj06TbDheJJOxE3zXctKU'
CHAT_IDS = {
    'user123': 1282461888
}
bot = Bot(token=TOKEN)

async def send_telegram_reminder(user_id, medicine):
    chat_id = CHAT_IDS.get(user_id)
    if chat_id:
        await bot.send_message(chat_id=chat_id, text=f"Reminder: Take your {medicine} now!")