import math
import telebot
import time
from time import *
from telebot import *
from datetime import *
import os
from sys import *
from aiogram.client.session.aiohttp import AiohttpSession
apihelper.proxy = {'http':'http://10.10.1.10:3128'}
bot = TeleBot('6417715356:AAE3fSAIO_M6_TN8lX2kYb1V6DXDCw_z1Dk')
# bot = TeleBot('7355802592:AAHQwrC1DoNHEOj93jQngTuX1MoWp_kSwWs')  #TestVersion
print('Started')
users_adm = set()


# file_admins = open('C:/Users/Mikhail/Desktop/Telebot/admins.txt')
# admins = [int(i) for i in file_admins]
print(admins)


group_id = -1002119559432
# bot.send_message(group_id, 'Бот запущен, проверить /check')
client_name = contacts = client_adress = date_time_problem = client_problem = ''
final_message_to_send = ''
answers = []
start_calls = 0
start_time = [int(i) for i in (str(datetime.today())[11:-10]).split(':')]
start_time[0] += 3
start_time = ':'.join([str(i) for i in start_time])
start_date = str(datetime.today())[:10]


@bot.message_handler(commands=["stop"])
def full_stop(message):
    global admins
    if message.from_user.id not in admins:
        bot.send_message(message.chat.id, 'Данная функция доступна только администраторам.')
    else:
        bot.send_message(message.chat.id, 'Соединение закрыто.')
        os.abort()
#
# @bot.message_handler(content_types=["text"])
# def clear(message):
#     pass
@bot.message_handler(commands=['answer'])
def send_answer(message):
    global admins
    if message.from_user.id not in admins:
        bot.send_message(message.chat.id, 'Данная функция доступна только администраторам.')
    else:
        command = message.text.split(' ', 2)
        user_id = command[1]
        answer_text = command[2]
        bot.send_message(chat_id=user_id, text=answer_text)
        bot.send_message(message.chat.id, 'Ответ отправлен!')

@bot.message_handler(commands=["check"])
def check_status(message):
    bot.send_message(message.chat.id, 'В сети (ФЕРМА)')

@bot.message_handler(commands=["start"])
def start(m, res=False):
    global start_calls, users_adm
    bot.send_message(m.chat.id, 'Обслуживание, ремонт, монтаж любой сложности' + '\n'
                     + 'Подъездный IP-домофон (Умный домофон)'
                     + '\n' + 'Домашний и подъездный домофон, квартирные переговорные устройства' + '\n' +
    'Видеонаблюдение, шлагбаумы, калитки.' + '\n' + 'Доступна новая функция - Бесключевое открытие домофона' + '\n' +
                     'Инструкция для пользователей: https://smartsputnik.notion.site/5daae8df993248a78847d5203f4b5112')
    site(m)
    start_calls += 1
    users_adm.add(m.from_user.id)


@bot.message_handler(commands=["admin"])
def admin(message):
    global start_calls, start_time, start_date, admins
    if message.from_user.id not in admins:
        bot.send_message(message.chat.id, 'Данная функция доступна только администраторам.')
    else:
        bot.send_message(message.chat.id, 'Дата и время запуска бота: ' + start_time + ' ' + 'МСК ' + start_date + '\n' + 'Запусков через /start: ' + str(start_calls)
    + '\n' + 'Список пользователей: ' + str(users_adm))

@bot.message_handler(commands=["check"])
def check_status(message):
    bot.send_message(message.chat.id, 'В сети (PythonAnywhere)')

@bot.message_handler(content_types=["text"])
def get_name1(message):
    global client_name, contacts, client_adress, date_time_problem, client_problem, final_message_to_send, answers
    client_name = contacts = client_adress = date_time_problem = client_problem = final_message_to_send = ''
    bot.send_message(message.chat.id, 'Если есть вопросы - представьтесь (ФИО), пожалуйста.')
    bot.register_next_step_handler(message, get_name2_get_contacts1)



@bot.message_handler(content_types=["text"])
def get_name2_get_contacts1(message):
    global client_name, contacts, client_adress, date_time_problem, client_problem, final_message_to_send, answers
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Очистить форму")
    markup.add(btn1)
    if message.text == 'Очистить форму':
        bot.send_message(message.chat.id, 'Заявка очищена.')
        bot.send_message(message.chat.id, 'Новая заявка.')
        get_name1(message)
    elif message.text == '/check':
        check_status(message)
    elif message.text == '/admin':
        admin(message)
    elif message.text == '/admin_commands':
        admin_commands(message)
    else:
        answers.append(message.text + '#' + str(message.from_user.id) + '#' + 'na')

        bot.send_message(message.chat.id, 'Предоставьте, пожалуйста, вашу контактную информацию (телефон/эл.почта). '
                                          'В случае её недостоверности обратная связь исключена.', reply_markup=markup)

        bot.register_next_step_handler(message, get_contacts2_get_adress1)
@bot.message_handler(content_types=["text"])



def get_contacts2_get_adress1(message):
    global client_name, contacts, client_adress, date_time_problem, client_problem, final_message_to_send, answers
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Очистить форму")
    markup.add(btn1)
    if message.text == 'Очистить форму':
        bot.send_message(message.chat.id, 'Заявка очищена')
        bot.send_message(message.chat.id, 'Новая заявка')
        get_name1(message)
    else:
        answers.append(message.text + '#' + str(message.from_user.id) + '#' + 'co')
        bot.send_message(message.chat.id, 'Какой Ваш адрес? Укажите улицу, номер дома и подъезд.', reply_markup=markup)
        bot.register_next_step_handler(message, get_adress2_get_date_time_problem1)



@bot.message_handler(content_types=["text"])
def get_adress2_get_date_time_problem1(message):
    global client_name, contacts, client_adress, date_time_problem, client_problem, final_message_to_send, answers
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Очистить форму")
    markup.add(btn1)
    if message.text == 'Очистить форму':
        bot.send_message(message.chat.id, 'Заявка очищена.')
        bot.send_message(message.chat.id, 'Новая заявка.')
        get_name1(message)
    else:
        answers.append(message.text + '#' + str(message.from_user.id) + '#' + 'ad')
        bot.send_message(message.chat.id, 'Пожалуйста, укажите номер квартиры, это очень важно для нас.')
        bot.register_next_step_handler(message, get_flat)
        # flat = message.from_user.text
        # answers.append(flat + '#' + str(message.from_user.id) + '#' + 'fl')
        # bot.send_message(message.chat.id, 'Опишите подробно, пожалуйста, возникший вопрос.', reply_markup=markup)
        # # bot.register_next_step_handler(message, get_date_time_problem2_get_message1)
        # bot.register_next_step_handler(message, get_message2)



@bot.message_handler(content_types=["text"])
def get_flat(message):
    global client_name, contacts, client_adress, date_time_problem, client_problem, final_message_to_send, answers, x
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Очистить форму")
    markup.add(btn1)
    if message.text == 'Очистить форму':
        bot.send_message(message.chat.id, 'Заявка очищена.')
        bot.send_message(message.chat.id, 'Новая заявка.')
        get_name1(message)
    else:
        answers.append(message.text + '#' + str(message.from_user.id) + '#' + 'fl')
        bot.send_message(message.chat.id, 'Опишите подробно, пожалуйста, возникший вопрос.', reply_markup=markup)
        x = message.from_user.id
        bot.register_next_step_handler(message, get_problem)

@bot.message_handler(content_types=["text"])
def get_problem(message):
    global client_name, contacts, client_adress, date_time_problem, client_problem, final_message_to_send, answers, x
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Очистить форму")
    markup.add(btn1)
    if message.text == 'Очистить форму':
        bot.send_message(message.chat.id, 'Заявка очищена.')
        bot.send_message(message.chat.id, 'Новая заявка.')
        get_name1(message)
    else:
        answers.append(message.text.replace('_', '-') + '#' + str(message.from_user.id) + '#' + 'qu')
        get_message2(message)


@bot.message_handler(commands=["check"])
def check_status(message):
    bot.send_message(message.chat.id, 'В сети (PythonAnywhere)')

# @bot.message_handler(content_types=["text"])
# def site(message):
#     markup = types.InlineKeyboardMarkup()
#     button1 = types.InlineKeyboardButton("Перейти на сайт", url='https://alekseyelcha.github.io')
#     markup.add(button1)
#     bot.send_message(message.chat.id, "*НАШ ВЕБ-САЙТ*", reply_markup=markup, parse_mode='Markdown')
#     get_name1(message)

@bot.message_handler(content_types=["text"])
def site(message):
    markup = types.InlineKeyboardMarkup()
    web_info = types.WebAppInfo('https://alekseyelcha.github.io')
    button_wa = types.InlineKeyboardButton("*Открыть в ТГ*", web_app=web_info, parse_mode='Markdown')
    button_web = types.InlineKeyboardButton("Открыть в Браузере", url='https://alekseyelcha.github.io')
    markup.add(button_wa, button_web)
    bot.send_message(message.chat.id, "На сайте теперь можно отправить обращение через Google Forms (Гугл Формы)!" + '\n' + "*Наш сайт:*",
                         reply_markup=markup, parse_mode='Markdown')
    get_name1(message)

# @bot.message_handler(content_types=["text"])
# def get_date_time_problem2_get_message1(message):
#     global client_name, contacts, client_adress, date_time_problem, client_problem, final_message_to_send
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     btn1 = types.KeyboardButton("Очистить форму")
#     markup.add(btn1)
#     if message.text == 'Очистить форму':
#         bot.send_message(message.chat.id, 'Заявка очищена.')
#         bot.send_message(message.chat.id, 'Новая заявка.')
#         get_name1(message)
#     else:
#         date_time_problem = message.text
#         bot.send_message(message.chat.id , 'Опишите, пожалуйста,'
#                                           ' возникший вопрос подробно.', reply_markup=markup)
#         bot.register_next_step_handler(message, get_message2)

@bot.message_handler(content_types=["text"])
def get_message2(message):
    global client_name, contacts, client_adress, date_time_problem, client_problem, final_message_to_send, x, answers
    send_q(message)

@bot.message_handler(content_types=["text"])
def send_q(message):
    bot.send_message(message.chat.id, '*Текст Вашего обращения, которое будет отправлено в компанию:* ' + '\n' +
    '*ФИО: *' + ' '.join([i.split('#')[0] for i in answers if str(message.from_user.id) in i and 'na' in i.split('#')]) + '\n' +
    '*Контактная информация: *' + ' '.join([i.split('#')[0] for i in answers if str(message.from_user.id) in i and 'co' in i.split('#')]) + '\n' +
    '*Адрес: *' + ' '.join([i.split('#')[0] for i in answers if str(message.from_user.id) in i and 'ad' in i.split('#')]) + '\n' +
    '*Вопрос: *' + ' '.join([i.split('#')[0] for i in answers if str(message.from_user.id) in i and 'qu' in i.split('#')]) + '\n', parse_mode='Markdown')

    bot.register_next_step_handler(message, send_qq)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Да")
    btn2 = types.KeyboardButton("Нет, полностью удалить форму.")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, '*Подтвердить отправку обращения?*', reply_markup=markup, parse_mode='Markdown')
@bot.message_handler(content_types=["text"])
def send_qq(message):

    if message.text == 'Да':
        create_text(message)
    else:
        bot.send_message(message.chat.id, 'Ваше обращение полностью очищено!')
        renew(message)


@bot.message_handler(content_types=["text"])
def create_text(message):
    global client_name, contacts, client_adress, date_time_problem, client_problem, final_message_to_send, x, answers
    time = [int(i) for i in str(datetime.today())[11:-10].split(':')]
    time[0] += 3
    time = (':'.join([str(i) for i in time]))
    date = str(datetime.today())
    date = '.'.join(list(reversed(date[:10].split('-'))))
    # final_message_to_send = ('ФИО: ' + client_name + '\n' + 'Контактная информация: ' + contacts + '\n'
    #                          + 'Адрес: ' + client_adress + '\n' + 'Дата проблемы: ' + date_time_problem + '\n'
    #                          + 'Проблема: ' + client_problem)
    group = -1002119559432
    user_nickname = message.from_user.username
    user_id = message.from_user.id
    print(answers)
    bot.send_message(group, '*Новая заявка: * ' + '\n' + '*Никнейм пользователя: *' + str(user_nickname) + '\n' + 'ID: '
    + str(user_id) + '\n' +
    '*Дата и время: *' + str(date) + ' ' + str(time) + '\n' + '*ФИО: *' + ' '.join(i.split('#')[0] for i in answers if str(message.from_user.id) in i and 'na' in i.split('#')) + '\n' + '*Контактная информация: *' + ' '.join(i.split('#')[0] for i in answers if str(message.from_user.id) in i and 'co' in i.split('#')) + '\n' + '*Адрес: *'
    + ' '.join(i.split('#')[0] for i in answers if str(message.from_user.id) in i and 'ad' in i.split('#')) + '\n' + '*Квартира: *' + ' '.join(i.split('#')[0] for i in answers if str(message.from_user.id) in i and 'fl' in i.split('#')) + '\n' + '*Вопрос: *' + ' '.join(i.split('#')[0] for i in answers if str(message.from_user.id) in i and 'qu' in i.split('#')), parse_mode='Markdown')
    answers = [i for i in answers if str(user_id) not in i]
    print(x)
    print(message.from_user.username)
    bot.send_message(message.chat.id, '*Ваша заявка отправлена!*', parse_mode='Markdown')
    clear(message)
    renew(message)

@bot.message_handler(content_types=['text'])
def clear(message):
    for index in range(10):
        bot.delete_message(chat_id=message.chat.id, message_id=message.message_id-index)

@bot.message_handler(content_types=["text"])
def renew(message):
    bot.send_message(message.chat.id, 'Для создания нового обращения нажмите /start ')

# bot.polling(none_stop=True, interval=0)
bot.infinity_polling(none_stop=True, timeout=240)

