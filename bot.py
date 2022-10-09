import telegram.ext
import requests
import schedule
import telebot
import time

from telegram import chat

bot = telebot.TeleBot("Your token")
@bot.route('/start')
def sending(message, cmd):
    bot.send_message(
        chat_id = message.chat.id,
        text = f"""
        Id : {message.from_user.id}
        Name : {message.from_user.first_name}
        """
    )

def remind():
    bot_token = "219733257:AAGRa2tbXiUYNPU0seB4R52K7kasHIlFmi8"
    bot_chatID = str(id(chat))
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + \
                '&parse_mode=HTML&text=' + "time is 11:31"
    response = requests.get(send_text)
    return response.json()

schedule.every().day.at("11:31").do(remind)

while True:
    schedule.run_pending()
    time.sleep(1)