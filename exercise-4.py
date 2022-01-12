import telebot

TOKEN = '2145100540:AAFFI8IdLuvQ2QMg-Kh9XpMN6nyh_CtoKhA'

bot = telebot.TeleBot(TOKEN)

count = 0
letters = ['A', 'E', 'I', 'O', 'U', 'Y']


@bot.message_handler(func=lambda message: True)
def search_char(message):
    message_text = message.text
    letters = 0

    for char in message_text:
        if char.lower() in letters:
            letters+=1

    bot.reply_to(message,f'Количество гласных букв; {letters}')


bot.infinity_polling()
