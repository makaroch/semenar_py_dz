import telebot
import Compres


bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def welcom(message):
    send_mess = f'<b> Привет <i>{message.from_user.first_name}</i></b>, как оно?'
    bot.send_message(message.chat.id, send_mess, parse_mode='html')
@bot.message_handler(commands=['websait'])
def go_web(message):
    marc = telebot.types.InlineKeyboardMarkup()
    marc.add(telebot.types.InlineKeyboardButton('перейти на сайт', url='https://www.youtube.com/watch?v=QoJ_yvPttlc'))
    # marc.add(telebot.types.InlineKeyboardButton('нет не хочу'))
    send_message = f'Отлично, вперед!'
    bot.send_message(message.chat.id, send_message, parse_mode='html', reply_markup=marc)













bot.polling(non_stop=True)
