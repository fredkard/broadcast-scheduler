import schedule, time, requests

bot_token = "219733257:AAGRa2tbXiUYNPU0seB4R52K7kasHIlFmi8"

def remind():
    bot_token = "219733257:AAGRa2tbXiUYNPU0seB4R52K7kasHIlFmi8"
    f = open('user_list.txt','r')
    file = f.read().split("\n")
    f.close()
    for l in file:
        chatID = l.split(',')[0]
        try:
            send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + chatID + \
                        '&parse_mode=HTML&text=' + "Hello " + l.split(",")[1]+" \ntime is 11:31"
        except:
            print(l)
        requests.get(send_text)
        
schedule.every().day.at("22:55").do(remind)

while True:
    schedule.run_pending()
    time.sleep(1)