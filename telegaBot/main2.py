import telebot
from telebot import types
import random

TOKEN = '6421031230:AAFcDsnmxbZn62h9UOL_h605amDSwOkMRRA'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, f'Привет,Я {message.from_user.first_name} {message.from_user.last_name}'
                                      f'\n'
                                      f'\nнажмите - /start')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Рандомное число')
    item2 = types.KeyboardButton('Курсы валют')
    item3 = types.KeyboardButton('Информация')
    item4 = types.KeyboardButton('Другое')

    markup.add(item1, item2, item3, item4)

    bot.send_message(message.chat.id, f'Привет, Я {message.from_user.first_name} {message.from_user.last_name}', reply_markup=markup)

@bot.message_handler(content_types = ['text'])
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == 'Рандомное число':
            bot.send_message(message.chat.id, 'Ваше число: ' + str(random.randint(0, 50)))
        elif message.text == 'Курсы валют':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('us Курс доллара')
            item2 = types.KeyboardButton('eu Курс евро')
            back = types.KeyboardButton('Назад')
            markup.add(item1, item2, back)

            bot.send_message(message.chat.id, 'Курсы валют', reply_markup=markup)

        elif message.text == 'Информация':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('О боте')
            item2 = types.KeyboardButton('Что в коробке')
            back = types.KeyboardButton('Назад')
            markup.add(item1, item2, back)

            bot.send_message(message.chat.id, 'Информация', reply_markup=markup)

        elif message.text == 'Другое':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Настройки')
            item2 = types.KeyboardButton('Подписка')
            item3 = types.KeyboardButton('Стикер')
            back = types.KeyboardButton('Назад')
            markup.add(item1, item2, item3, back)

            bot.send_message(message.chat.id, 'Другое', reply_markup=markup)


        elif message.text == 'Назад':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Рандомное число')
            item2 = types.KeyboardButton('Курсы валют')
            item3 = types.KeyboardButton('Информация')
            back = types.KeyboardButton('Другое')
            markup.add(item1, item2, item3, back)

            bot.send_message(message.chat.id, 'Назад', reply_markup=markup)

bot.polling(non_stop = True)