import telebot
import json
import requests

f = open('bot_creds.txt')
bot_token = f.readline()



bot  = telebot.TeleBot("")

bank_api = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode=EUR&date=20221212&json"

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привіт!")


@bot.message_handler(content_types=["text"])
def send_welcome2(message):
    if message.text == "Привіт":
        bot.reply_to(message, "Привіт!")
    if message.text == "EUR":

        r = requests.get(url = bank_api)
        data = r.json()
        value = data[0]["rate"]



        bot.reply_to(message, f"Привіт, курс Євро на сьогодні: {value}")



bot.infinity_polling(none_stop=True, interval=0)
