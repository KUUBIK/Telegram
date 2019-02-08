import telebot
from telebot import types
import datetime
import bs4
import requests
import re

token = '603482894:AAHhXpXoM8PQrqRUHaC4Bh5K3FC_-5ITug0'
bot = telebot.TeleBot(token)

thunderstorm = u'\U0001F4A8'    # Code: 200's, 900, 901, 902, 905
breeze = u'\U0001F4A8'
drizzle = u'\U0001F601'         # Code: 300's
rain = u'\U00002614'            # Code: 500's
snowflake = u'\U00002744'       # Code: 600's snowflake
snowman = u'\U000026C4'         # Code: 600's snowman, 903, 906
atmosphere = u'\U0001F301'      # Code: 700's foogy
clearSky = u'\U00002600'        # Code: 800 clear sky
fewClouds = u'\U000026C5'       # Code: 801 sun behind clouds
clouds = u'\U00002601'          # Code: 802-803-804 clouds general
hot = u'\U0001F525'             # Code: 904
defaultEmoji = u'\U0001F300' # default emojis

response = requests.get('https://yandex.ru/pogoda/astana?from=serp_title')

responseNew = response.text
dom = bs4.BeautifulSoup(response.text)

def parsingSite():

    data = dom.findAll("div", 'fact__temp-wrap') #температура сейчас
    # print(data)
    # print(type(responseNew))
    data = str(data)
    lookfor = r">[−1.\d,%]+"
    parce = re.findall(lookfor, data)
    parce = str(parce)
    lookfor2 = r"(?!,)[−1.\d,%]+"

    parce = re.findall(lookfor2, parce)
    # print(parce)





    return parce

def parsingData():

    data = dom.findAll("div", 'fact__props fact__props_position_middle') #температура сейчас
    # print(data)
    data = str(data)
    lookfor = r">[−1.\d,%]+"
    parce = re.findall(lookfor, data)
    # print(parce)
    lookfor2 = r"(?!,)[−1.\d,%]+"
    parce = str(parce)
    parce = re.findall(lookfor2, parce)
    # print(parce)
    del(parce[2])
    return parce

@bot.message_handler(commands=['data'])
def handle_start_help(message):
    listMonth = ['января','февраля','марта','апреля','мая','июня','июля','августа','сентября','октября','ноября','декабря']
    now = datetime.datetime.now()
    day = now.day
    month = now.month
    month = listMonth[month - 1]
    hour = now.hour
    minute = now.minute
    year = now.year
    minute = now.minute
    # print(len(str(minute)))
    if len(str(minute)) == 1:

        retrn = str(day) + ' ' + month.strip()+ ' ' + str(year) + ' года'+ ' ' + str(hour) + ':'+ '0' + str(minute) + drizzle
        bot.send_message(message.chat.id, retrn)
    else:
        retrn = str(day) + ' ' + month.strip()+ ' ' + str(year) + ' года'+ ' ' + str(hour) + ':' + str(minute)+ drizzle
        # print(retrn)
        bot.send_message(message.chat.id, retrn)



@bot.message_handler(commands=['weather'])
def weather(message):
    parce = parsingSite()
    data = parsingData()
    bot.send_message(message.chat.id, '-' * 25 + '\n'
                     'Температура за окном ' + str(parce[0]) + str('°C') + '\n'
                     'Скорость ветра ' + str(data[0]) + ' м/c' + breeze  +  '\n'
                     'Влажность воздуха ' + str(data[1])
                        )


@bot.message_handler(func=lambda message: True,commands=['reverse'])
def reverseMessage(message):
    bot.send_message(message.chat.id, message.text)




@bot.message_handler(func=lambda message: True,commands=['time'])
def time(message):
    # listZvonok = ['8:00','9:05' ,'10:10' ,'11:15' ,'12:20' ,'13:25' ,'14:30', '15:35', '16:40', '17:45', '18:50' ]

    listZvonok = ['8:50','9:55' ,'11:10' ,'12:05' ,'13:10' ,'14:15' ,'15:20', '16:25', '17:30', '18:35', '19:40' ]
    nowHour = datetime.datetime.now()
    Hours = nowHour.hour
    # print(Hours)
    Hours = Hours - 8
    try:
        minute = listZvonok[Hours]
        minute = 'Пара заканчиваться в ' + str(minute)
        bot.send_message(message.chat.id, minute)
    except IndexError:
        bot.send_message(message.chat.id, 'Time is not difined!')


@bot.message_handler(func=lambda message: True,content_types=['text'])
def echo_msg(message):
    bot.send_message(message.chat.id, message.text) # здесь он отправляеть сообщение (What??) на наш телеграмм бот
    # print(message.text)
    markup = types.ReplyKeyboardRemove(True)
    bot.send_message(message.chat.id, "Choose one letter:" + str(message.text), reply_markup=markup)



if __name__ == '__main__':
    bot.polling(none_stop=True)


