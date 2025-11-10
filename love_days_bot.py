import asyncio
from telegram import Bot
import schedule
import time
from datetime import datetime

# ====== Настройки ======
TOKEN = "8518469705:AAHV1w5IOYYER0eGp5cSMoA20UXMOCrWEP4"
CHANNEL_ID = -1003161684279
START_DATE = "2025-09-16"

bot = Bot(token=TOKEN)

async def send_days_passed():
    start = datetime.strptime(START_DATE, "%Y-%m-%d")
    today = datetime.now()
    days_passed = (today - start).days
    message = f"💞 Мы вместе уже {days_passed} дней 💞"
    await bot.send_message(chat_id=CHANNEL_ID, text=message)
    print(f"Отправлено сообщение: {message}")

# ====== Обёртка для синхронного schedule ======
def job():
    asyncio.run(send_days_passed())

# ====== Расписание ======
schedule.every().day.at("22:50").do(send_love_message)

print("✅ Бот запущен. Будет отправлять сообщение каждый день в 00:00...")

while True:
    schedule.run_pending()
    time.sleep(60)
