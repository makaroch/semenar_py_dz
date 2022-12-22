import telebot
import random
import Compres

name = '5710747140:AAHeP_BCpDYTHkLXw-uDN81rUL9-_x7tJqs'
bot = telebot.TeleBot(name)

@bot.message_handler(commands=['start'])
def welcom(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item_1 = telebot.types.KeyboardButton('Рандомное число')
    item_2 = telebot.types.KeyboardButton('Cжать')
    item_3 = telebot.types.KeyboardButton("Расскажи анекдот")
    item_4 = telebot.types.KeyboardButton('узнать id')
    item_5 = telebot.types.KeyboardButton('Узнать id стикера')
    markup.add(item_1, item_2, item_3, item_4, item_5)
    hello = f'Привет, <b><i>{message.from_user.first_name}</i></b>'
    bot.send_message(message.chat.id, hello, reply_markup=markup, parse_mode='html')
    print(message.from_user.id)


@bot.message_handler(content_types=['text'])
def send_text(message):

    compres = message.text

    if message.text == "ку":
        bot.send_message(message.chat.id, 'кууку')
    elif message.text == "Рандомное число":
        bot.send_message(message.chat.id, str(random.randint(1, 100)))

    elif message.text == "Cжать":
        mesg = bot.send_message(message.chat.id, 'Введите строку которую хотите сжать')
        bot.register_next_step_handler(mesg, comrpes)


    elif message.text == 'узнать id':
        bot.send_message(message.chat.id, str(message.chat.id))

    elif message.text == 'Узнать id стикера':
        mesg = bot.send_message(message.chat.id, 'Кидай стик расскажу id)')
        bot.register_next_step_handler(mesg, give_sti_id)


    elif message.text == "Расскажи анекдот":
        with open("file.txt", 'r', encoding="utf-8") as file:
            list_str = file.read().split(';;')
        i = random.randint(0, len(list_str) - 1)
        bot.send_message(message.chat.id, list_str[i])

    else: 
        bot.send_message(message.chat.id, 'хз')


def comrpes(messeg):
   str = Compres.Compress(messeg.text)
   bot.send_message(messeg.chat.id, str)
   bot.send_sticker(messeg.chat.id, 'CAACAgIAAxkBAAEG73Vjo1mRgC9-dIS5kUjjdMG09qeodAACXwEAAhAabSLLoLkqsC4-oywE')
   bot.send_message(messeg.chat.id, 'для повторного сжатия снова нажмите на кнопку "Сжать"')


def give_sti_id(message):
    sticker_id = message.sticker.file_id
    bot.send_message(message.chat.id, sticker_id)






bot.polling(non_stop=True)