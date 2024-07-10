import telebot
import webbrowser
from telebot import types

bot = telebot.TeleBot('6421031230:AAFcDsnmxbZn62h9UOL_h605amDSwOkMRRA')

# @bot.message_handler(commands=['start'])
# def start(message):
#     markup = types.ReplyKeyboardMarkup()
#     bt1 = types.KeyboardButton('Перейти на сайт')
#     markup.row(bt1)
#     bt2 = types.KeyboardButton('Удалить фото!')
#     markup.row(bt2)
#     bt3 = types.KeyboardButton('Изменить текст')
#     markup.row(bt3)
    # file = open('./photo.PNG', 'rb')
    # bot.send_photo(message.chat.id, file, reply_markup=markup)
#   bot.send_message(message.chat.id, 'Привет', reply_markup=markup)
#     bot.register_next_step_handler(message, on_click)
#
# def on_click(message):
#     if message.text() =='Перейти на сайт':
#         bot.send_message(message.chat.id, 'Web site is open')
#     elif message.text == 'Удалить фото':
#         bot.send_message(message.chat.id, 'Deleted')

@bot.message_handler(content_types=['photo'])
def get_photo(message):
    markup = types.InlineKeyboardMarkup()
    bt1 = types.InlineKeyboardButton('Перейти на сайт' , url='https://google.com')
    markup.row(bt1)
    bt2 = types.InlineKeyboardButton('Удалить фото!', callback_data='delete')
    markup.row(bt2)
    bt3 = types.InlineKeyboardButton('Изменить текст', callback_data='edit')
    markup.row(bt3)
    bot.reply_to(message, 'Какое красивое фото!', reply_markup=markup)

@bot.message_handler(commands=['site' , 'website'])
def site(message):
    webbrowser.open('https://vk.com/')

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, f'Привет,Я {message.from_user.first_name} {message.from_user.last_name} , \n\nВот список команд, нажми для выбора:'
                                      f'\n'
                                      f'\n/site - посетите наш сайт,'
                                      f'\n/phone_number - контактный номер телефона'
                                      f'\n/passport_details - паспортные данные')

@bot.message_handler(commands=['hello'])
def main(message):
    bot.send_message(message.chat.id, '<b>Hi</b>, <u>whatsapp!</u>', parse_mode='html')

@bot.message_handler(commands=['phone_number'])
def main(message):
    bot.send_message(message.chat.id, f'Кравченко Павел Юрьевич, вот 8-996-423-0663')

@bot.message_handler(commands=['passport_details'])
def main(message):
    bot.send_message(message.chat.id, f'Вот, серия: 0506'
                                      f'\nномер: 350290'
                                      f'\nвыдан: 08.07.2007 ОУФМС России по Приморскому краю в г. Уссурийске'
                                      f'\nкод подразделения: 250-018')

@bot.message_handler()
def info(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, f'Привет, Я {message.from_user.first_name} {message.from_user.last_name}')
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'ID: {message.from_user.id}')

@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'delete':
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
    elif callback.data == 'edit':
        bot.edit_message_text('Edit text', callback.message.chat.id, callback.message.message_id)

bot.polling(none_stop=True)

