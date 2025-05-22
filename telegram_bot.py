from telegram import Bot
from config import 7764776672:AAG77dSGvj9GQAQ65qTeablUymI3M0NdWPE, 6086012346

bot = Bot(token=7764776672:AAG77dSGvj9GQAQ65qTeablUymI3M0NdWPE)

def send_message(text):
    try:
        print("Отправляю сообщение в Telegram...")
        bot.send_message(chat_id=6086012346, text=text)
    except Exception as e:
        print(f"[Ошибка при отправке сообщения]: {e}")
