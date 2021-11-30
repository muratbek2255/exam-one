import telebot

TOKEN = '2145100540:AAFFI8IdLuvQ2QMg-Kh9XpMN6nyh_CtoKhA'

bot = telebot.TeleBot(TOKEN)

count = 0
letters = ['a', 'u', 'y', '0']


@bot.message_handler(content_types=['text'])
def search_chars(text):
    for char in text:
        if char in letters:
            count=+1
        bot.send_message(text.chat.id, "vot glasnye:")
