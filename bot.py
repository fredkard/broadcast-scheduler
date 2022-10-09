import requests
import telebot

bot_token = "219733257:AAGRa2tbXiUYNPU0seB4R52K7kasHIlFmi8"
bot = telebot.TeleBot(bot_token)

@bot.route('/start')
def sending(message):
    bot.send_message(
        chat_id = message['chat']['id'],
        text = f"""
        Id : {message['chat']['id']}
        Name : {message['chat']['first_name']}
        """
    )
    f = open('user_list.txt','a')
    f.write("%s,%s\n"%(message['chat']['id'],message['chat']['first_name']))
    f.close()

if __name__ == '__main__':
        bot.config['api_key'] = bot_token
        bot.poll(debug=True)