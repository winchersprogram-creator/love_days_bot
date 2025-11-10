from telegram import Bot
import schedule
import time
from datetime import datetime

# 1️⃣ Настройки бота
TOKEN = "8518469705:AAHV1w5IOYYER0eGp5cSMoA20UXMOCrWEP4"
CHANNEL_ID = "-1003161684279"
START_DATE = datetime(2025, 9, 16)

bot = Bot(token=TOKEN)

# 2️⃣ Объявляем функцию отправки сообщения
def send_love_message():
    delta = datetime.now() - START_DATE
    message = f"💞 Мы вместе уже {delta.days} дней 💞"
    bot.send_message(chat_id=CHANNEL_ID, text=message)
    print("Сообщение отправлено!")

# 3️⃣ Отправка сообщения сразу при деплое (для проверки)
send_love_message()

# 4️⃣ Планируем ежедневную отправку в 22:50
schedule.every().day.at("23:05").do(send_love_message)

# 5️⃣ Цикл для работы schedule
while True:
    schedule.run_pending()
    time.sleep(60)
