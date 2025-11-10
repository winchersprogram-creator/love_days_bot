import asyncio
from telegram import Bot
import schedule
import time
from datetime import datetime

TOKEN = "8518469705:AAHV1w5IOYYER0eGp5cSMoA20UXMOCrWEP4"
CHANNEL_ID = "-1003161684279"
START_DATE = datetime(2025, 9, 16)

bot = Bot(token=TOKEN)

# Асинхронная функция отправки сообщения
async def send_love_message():
    delta = datetime.now() - START_DATE
    message = f"💞 Мы вместе уже {delta.days} дней 💞"
    await bot.send_message(chat_id=CHANNEL_ID, text=message)
    print("Сообщение отправлено!")

# Функция для синхронного вызова из schedule
def schedule_message():
    asyncio.run(send_love_message())

# Отправка сразу при старте
schedule_message()

# Планирование на 22:50
schedule.every().day.at("23:10").do(schedule_message)

# Цикл для работы schedule
while True:
    schedule.run_pending()
    time.sleep(60)
