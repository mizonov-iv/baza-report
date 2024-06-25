# Подключаем модуль для Телеграма
import telebot
# Указываем токен
bot = telebot.TeleBot('7090072301:AAFZZHhY5SjBLOlud-efko5Z6GovjDWdyU0')
# Импортируем типы из модуля, чтобы создавать кнопки
from telebot import types
# Метод, который получает сообщения и обрабатывает их
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "/help":
        # Готовим кнопки
        keyboard = types.InlineKeyboardMarkup()
        # По очереди готовим текст и обработчик для каждого знака зодиака
        key_call = types.InlineKeyboardButton(text='Отчет по назначениям', callback_data='call')
        keyboard.add(key_call)
        key_day = types.InlineKeyboardButton(text='Отчет за день', callback_data='day')
        keyboard.add(key_day)
        # Показываем все кнопки сразу и пишем сообщение о выборе
        bot.send_message(message.from_user.id, text='Выбери отчет', reply_markup=keyboard)
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")
# Обработчик нажатий на кнопки
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "call":
        msg = 'Отчет по назначениям'
        bot.send_message(call.message.chat.id, msg)
    elif call.data == 'day':
        msg = 'Отчет за день'
        bot.send_message(call.message.chat.id, msg)
# Запускаем постоянный опрос бота в Телеграме
bot.polling(none_stop=True, interval=0)