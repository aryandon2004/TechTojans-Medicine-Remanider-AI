from telegram_bot import send_telegram_reminder
import asyncio

asyncio.run(send_telegram_reminder("user123", "✅ Test message from your AI assistant!"))
