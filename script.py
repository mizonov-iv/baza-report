# Подключаем модуль для Телеграма
import telebot
# Указываем токен
bot = telebot.TeleBot('7090072301:AAFZZHhY5SjBLOlud-efko5Z6GovjDWdyU0')
# Импортируем типы из модуля, чтобы создавать кнопки
from telebot import types

# Метод, который получает сообщения и обрабатывает их
@bot.message_handler(commands=['start'])
def start(message):
    # Готовим кнопки
    keyboard = types.InlineKeyboardMarkup()
    key_call = types.InlineKeyboardButton(text='Отчет по назначениям', callback_data='call')
    # keyboard.row(key_call)
    key_day = types.InlineKeyboardButton(text='Отчет за день', callback_data='day')
    keyboard.row(key_call, key_day)
    # Показываем все кнопки сразу и пишем сообщение о выборе
    bot.send_message(message.from_user.id, text='Выбери отчет', reply_markup=keyboard)
    
# Обработчик нажатий на кнопки
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "call":
        keyboard = types.InlineKeyboardMarkup()
        btn_1 = types.InlineKeyboardButton(text='One', callback_data='call')
        btn_2 = types.InlineKeyboardButton(text='Two', callback_data='call')
        btn_3 = types.InlineKeyboardButton(text='Three', callback_data='call')
        keyboard.row(btn_1, btn_2, btn_3)
        
        msg = 'Сколько качественных назначений?'
        bot.send_message(call.message.chat.id, msg, reply_markup=keyboard)

    elif call.data == 'day':
        msg = 'Отчет за день'
        bot.send_message(call.message.chat.id, msg)
# Запускаем постоянный опрос бота в Телеграме
bot.polling(none_stop=True, interval=0)