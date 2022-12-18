import telebot
from telebot import types
import emoji
bot = telebot.TeleBot('5860039737:AAGXauKD8ws81SOMcRaMMzz2-w9KonY_DIM')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, emoji.emojize('Добрый день, Евгений!Отправляю Вам гороскоп... :red_heart:'))
    key_f = types.InlineKeyboardMarkup()
    key_day = types.InlineKeyboardButton(text='На день', callback_data='day')
    key_week = types.InlineKeyboardButton(text='На неделю', callback_data='week')
    key_month = types.InlineKeyboardButton(text='На месяц', callback_data='month')
    key_f.add(key_day, key_week, key_month)
    bot.send_message(message.chat.id, 'Какой гороскоп Вы хотите?', reply_markup=key_f)

@bot.callback_query_handler(func = lambda call: True)
def callback(call):
    if call.data == 'day':
            message = 'https://horo.mail.ru/prediction/pisces/today/'
            bot.send_message(call.message.chat.id, message)
    if call.data == 'week':
            message = 'https://horo.mail.ru/prediction/pisces/week/'
            bot.send_message(call.message.chat.id, message)
    if call.data == 'month':
            message = 'https://horo.mail.ru/prediction/pisces/month/'
            bot.send_message(call.message.chat.id, message)

bot.polling(none_stop=True)
