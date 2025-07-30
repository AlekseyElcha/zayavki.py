import datetime
from telebot import *
import math
import time
from time import *
from datetime import *
import os
from sys import *
from telebot.types import InlineKeyboardMarkup
bot = TeleBot('7355802592:AAHQwrC1DoNHEOj93jQngTuX1MoWp_kSwWs') # TG TEST VERSION
# bot = TeleBot('6417715356:AAE3fSAIO_M6_TN8lX2kYb1V6DXDCw_z1Dk') # TG MAIN VERSION
file_admins = open('/home/aleshus2007eu/admins.txt')
admins = [int(i) for i in file_admins]
count_users = 0
CLIENT_DATA = []
RESERVE = []
pressed_buttons = set()
group_id = -4253143897  # TEST GROUP
# group_id = -1002119559432  # MAIN GROUP
start_time_data = (str(datetime.today())[:-7] + ' UTC')
print('Started')
symbols = ['_', '*', '[', ']', '(', ')', '~', '`', '>', '#', '+', '-', '=', '|', '{', '}', '.', '!', '₽', '$', '#', '%']
def replace_decode(s):
    try:
        t = [i for i in s]
        for i in t:
            if i in symbols:
                i = i.replace(i, '-')
        return ''.join(t)
    except:
        x = 'Неподдерживаемый символ'
        return x

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


@bot.message_handler(commands=["admin"])
def admin(message):
    global start_calls, start_time, start_date, admins
    if message.from_user.id not in admins:
        bot.send_message(message.chat.id, 'Данная функция доступна только администраторам.')
    else:
        bot.send_message(message.chat.id, 'Дата и время запуска бота: ' + start_time + ' ' + 'МСК ' + start_date + '\n' + 'Пользователей: ' + str(count_users))

@bot.message_handler(commands=["check"])
def check_status(message):
    bot.send_message(message.chat.id, 'В сети (PythonAnywhere)')

@bot.message_handler(content_types=["text"])
def site(message):
    markup = types.InlineKeyboardMarkup()
    web_info = types.WebAppInfo('https://domofon-servis-odi.ru')
    button_wa = types.InlineKeyboardButton("Открыть здесь", web_app=web_info)
    button_web = types.InlineKeyboardButton("Открыть в Браузере", url='https://domofon-servis-odi.ru')
    markup.add(button_wa, button_web)
    bot.send_message(message.chat.id, 'Где открыть наш обновлённый сайт? https://domofon-servis-odi.ru', reply_markup=markup)
    redirect(message)


# @bot.message_handler(content_types=["text"])
# def site(message):
#     markup = types.InlineKeyboardMarkup()
#     btn1 = types.InlineKeyboardButton("Наш сайт", url='https://alekseyelcha.github.io/')
#     markup.add(btn1)
#     bot.send_message(message.chat.id, 'ОТКРЫТЬ САЙТ', reply_markup=markup)
#     redirect(message)

@bot.message_handler(content_types=["text"])
def questions_tg_bot1(message):
    global group_id
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Назад")
    markup.add(btn1)
    bot.send_message(message.chat.id, 'Оставьте здесь своё сообщение разработчику или вернитесь по кнопке "Назад"', reply_markup=markup)
    bot.register_next_step_handler(message, questions_tg_bot2)


@bot.message_handler(content_types=["text"])
def questions_tg_bot2(message):
    global group_id
    msg1 = message.text
    if msg1 == 'Назад':
        redirect(message)
    else:
        msg = 'Сообщение: ' + msg1
        bot.send_message(group_id, 'ID пользователя: ' + str(message.from_user.id) + '\n' + msg)
        bot.send_message(message.chat.id, 'Сообщение отправлено!', reply_markup=types.ReplyKeyboardRemove())
        redirect(message)

@bot.message_handler(commands=['start'])
def start(m, res=False):
    global count_users
    markup = types.ReplyKeyboardMarkup(resize_keyboard=False)
    btn1 = types.KeyboardButton("Наш веб-сайт")
    btn2 = types.KeyboardButton("Оплата/погашение задолжности")
    btn3 = types.KeyboardButton("Вопрос технического или иного характера")
    btn4 = types.KeyboardButton("Вопросы/предложения по работе этого Телеграм-бота")
    # btn5 = types.KeyboardButton("История запросов")
    markup.add(btn1)
    markup.add(btn2)
    markup.add(btn3)
    markup.add(btn4)
    # markup.add(btn5)
    bot.send_message(m.chat.id, 'Приветствуем Вас в нашем ТГ-боте!' + '\n' + '#########################' + '\n' + '\n' + 'Это обновленная версия нашего бота, в случае некорректной работы, пожалуйста, '
     'пишите на эл.почту aleshus2007@gmail.com, это поможет нам оперативно найти и пофиксить баги.' + '\n' +
        '#########################' + '\n' + '\n' +'Выберите характер интересующего Вас вопроса, '
                                                   'нажав на соответствующую кнопку. Если кнопок не видно, скройте клавиатуру или нажмите на '
                                                   '"квадратик с кнопками" в строке набора текста', reply_markup=markup)
    count_users += 1
    bot.register_next_step_handler(m, get_quest_type)

@bot.message_handler(content_types=["text"])
def admin_panel_open(message):
    global admins
    us_id = message.from_user.id
    if us_id not in admins:
        bot.send_message(message.chat.id, 'Данная функция доступна только администраторам. Выберите другой режим.')
        redirect(message)
    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=False)
        btn1 = types.KeyboardButton("Ответить на обращение")
        btn2 = types.KeyboardButton("Системная информация")
        btn3 = types.KeyboardButton("Назад")
        markup.add(btn1)
        markup.add(btn2)
        markup.add(btn3)
        bot.send_message(message.chat.id, 'Выберите нужную функцию при помощи кнопок', reply_markup=markup)
        bot.register_next_step_handler(message, admin_panel)

@bot.message_handler(content_types=["text"])
def admin_panel(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=False)
    btn1 = types.KeyboardButton("Ответить на обращение")
    btn2 = types.KeyboardButton("Системная информация")
    btn3 = types.KeyboardButton("Назад")
    markup.add(btn1)
    markup.add(btn2)
    markup.add(btn3)
    if message.text == 'Ответить на обращение':
        reply_id1(message)
    elif message.text == 'Системная информация':
       system_info(message)
    else:
        redirect(message)

@bot.message_handler(content_types=["text"])
def reply_id1(message):
    global group_id
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Назад")
    markup.add(btn1)
    bot.send_message(message.chat.id, 'Отправьте ответ в формате "ID <пробел> текст" или вернитесь по кнопке "Назад"', reply_markup=markup)
    bot.register_next_step_handler(message, reply_id2)

@bot.message_handler(content_types=["text"])
def reply_id2(message):
    global group_id
    msg1 = message.text
    if msg1 == 'Назад':
        admin_panel_open(message)
        return
    else:
        data = msg1
        try:
            user_id = data.split()[0]
            answer_text = data.split()[1]
            bot.send_message(chat_id=user_id, text=answer_text)
            bot.send_message(message.chat.id, 'Ответ отправлен!')
            admin_panel_open(message)
        except:
            bot.send_message(message.chat.id, 'Ошибка при отправке сообщения или неверный формат записи')
            admin_panel_open(message)



@bot.message_handler(content_types=["text"])
def system_info(message):
    global RESERVE, start_time_data, group_id
    client_data = '\n'.join(RESERVE)
    sys_info = 'Дата запуска: ' + start_time_data + '\n' + 'ID группы Телеграм: ' + str(group_id) + '\n' + 'CLIENT_DATA list\n' + client_data
    bot.send_message(message.chat.id, sys_info)
    admin_panel_open(message)

@bot.message_handler(content_types=["text"])
def history(message):
    us_id = message.from_user.id
    print(us_id)
    f = open('/home/aleshus2007eu/data.txt', encoding='utf-8')
    msgs = f.readlines()
    res = []
    for i in msgs:
        if int(i.split('&')[2]) == us_id:
            res.append(i)
    if not res:
        bot.send_message(message.chat.id, 'История пуста.')
        redirect(message)
    else:
        reply = []
        for i in res:
            line = i.split('&')[2:]
            date = line[0]
            time = line[1]
            question = line[-2]
            status = line.strip()[-1]
            joined = ('\n' + 'Дата: ' + date + '\n' + 'Время: ' + time + '\n' + 'Вопрос: ' + question  + '\n' + 'Статус: ' + status + '\n')
            reply.append(joined)
        bot.send_message(message.chat.id, '\n############################\n'.join(reply))
        redirect(message)


def redirect(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=False, one_time_keyboard=True)
    btn1 = types.KeyboardButton("Наш веб-сайт")
    btn2 = types.KeyboardButton("Оплата/погашение задолжности")
    btn3 = types.KeyboardButton("Вопрос технического или иного характера")
    btn4 = types.KeyboardButton("Вопросы/предложения по работе этого Телеграм-бота")
    btn5 = types.KeyboardButton("Админ-панель")
    markup.add(btn1)
    markup.add(btn2)
    markup.add(btn3)
    markup.add(btn4)
    markup.add(btn5)
    bot.send_message(message.chat.id, 'Выберите характер интересующего Вас вопроса, нажав на соответствующую кнопку.', reply_markup=markup)
    bot.register_next_step_handler(message, get_quest_type)

@bot.message_handler(content_types=["text"])
def get_quest_type(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=False, one_time_keyboard=True)
    btn1 = types.KeyboardButton("Наш веб-сайт")
    btn2 = types.KeyboardButton("Оплата/погашение задолжности")
    btn3 = types.KeyboardButton("Вопрос технического или иного характера")
    btn4 = types.KeyboardButton("Вопросы/предложения по работе этого Телеграм-бота")
    btn5 = types.KeyboardButton("Админ-панель")
    markup.add(btn1)
    markup.add(btn2)
    markup.add(btn3)
    markup.add(btn4)
    markup.add(btn5)
    if message.text == 'Оплата/погашение задолжности':
        bot.send_message(message.chat.id, 'По данному вопросу, пожалуйста обратитесь напрямую в Диспетчерскую по тел. +7(495)596-16-03, эл.почта 5961603@mail.ru' + '\n' +
        'ВНИМАНИЕ! Если вы были заблокированы в приложении Спутник "Наш Дом", скорее всего, у Вас есть задолженность по оплате наших услуг. Обратитесь в Диспетчерскую.', reply_markup=markup)
        redirect(message)
    elif message.text == 'Вопрос технического или иного характера':
        bot.send_message(message.chat.id, 'Ответьте на все вопросы, мы постараемся помочь Вам.')
        get_name1(message)
    elif message.text == 'Наш веб-сайт':
        site(message)
    elif message.text == 'Вопросы/предложения по работе этого Телеграм-бота':
        questions_tg_bot1(message)
    elif message.text == 'Админ-панель':
        admin_panel_open(message)
    else:
        bot.send_message(message.chat.id, 'Ошибка! Повторите попытку.')
        redirect(message)

@bot.message_handler(content_types=["text"])
def get_name1(message):
    markup = types.ReplyKeyboardRemove()
    bot.send_message(message.chat.id, 'Представьтесь (ФИО), пожалуйста. При желании, остановить диалог по данному'
                                      ' вопросу можно будет по кнопке "Очистить форму".', reply_markup=markup)
    bot.register_next_step_handler(message, get_name2_get_contacts1)


@bot.message_handler(content_types=["text"])
def get_name2_get_contacts1(message):
    global CLIENT_DATA
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    btn1 = types.KeyboardButton("Очистить форму")
    markup.add(btn1)
    if message.text == 'Очистить форму':
        CLIENT_DATA = [i for i in CLIENT_DATA if str(message.from_user.id) not in i]
        redirect(message)
    elif message.text == '/check':
        check_status(message)
    elif message.text == '/admin':
        admin(message)
    else:
        CLIENT_DATA.append(replace_decode(message.text) + '#' + str(message.from_user.id) + '#' + 'na')

        bot.send_message(message.chat.id, 'Предоставьте, пожалуйста, вашу контактную информацию (телефон/эл.почта). '
                                          'В случае её недостоверности обратная связь будет невозможна.', reply_markup=markup)

        bot.register_next_step_handler(message, get_contacts2_get_adress1)

@bot.message_handler(content_types=["text"])
def get_contacts2_get_adress1(message):
    global CLIENT_DATA
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    btn1 = types.KeyboardButton("Очистить форму")
    markup.add(btn1)
    if message.text == 'Очистить форму':
        CLIENT_DATA = [i for i in CLIENT_DATA if str(message.from_user.id) not in i]
        redirect(message)
    else:
        CLIENT_DATA.append(replace_decode(message.text) + '#' + str(message.from_user.id) + '#' + 'co')
        bot.send_message(message.chat.id, 'Укажите улицу, номер дома и подъезд.', reply_markup=markup)
        bot.register_next_step_handler(message, get_adress2_get_date_time_problem1)

@bot.message_handler(content_types=["text"])
def get_adress2_get_date_time_problem1(message):
    global CLIENT_DATA
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    btn1 = types.KeyboardButton("Очистить форму")
    markup.add(btn1)
    if message.text == 'Очистить форму':
        CLIENT_DATA = [i for i in CLIENT_DATA if str(message.from_user.id) not in i]
        redirect(message)
    else:
        CLIENT_DATA.append(replace_decode(message.text) + '#' + str(message.from_user.id) + '#' + 'ad')
        bot.send_message(message.chat.id, 'Пожалуйста, укажите номер квартиры, это очень важно для нас.', reply_markup=markup)
        bot.register_next_step_handler(message, get_flat)

@bot.message_handler(content_types=["text"])
def get_flat(message):
    global CLIENT_DATA
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    btn1 = types.KeyboardButton("Очистить форму")
    markup.add(btn1)
    if message.text == 'Очистить форму':
        CLIENT_DATA = [i for i in CLIENT_DATA if str(message.from_user.id) not in i]
        redirect(message)
    else:
        CLIENT_DATA.append(replace_decode(message.text) + '#' + str(message.from_user.id) + '#' + 'fl')
        bot.send_message(message.chat.id, 'Пожалуйста, подробно опишите Ваш вопрос. После этого бот автоматически '
                                          'отправит Ваше обращение нам.', reply_markup=markup)
        us_id = message.from_user.id
        bot.register_next_step_handler(message, get_problem)

@bot.message_handler(content_types=["text"])
def get_problem(message):
    global CLIENT_DATA
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    btn1 = types.KeyboardButton("Очистить форму")
    markup.add(btn1)
    if message.text == 'Очистить форму':
        CLIENT_DATA = [i for i in CLIENT_DATA if str(message.from_user.id) not in i]
        redirect(message)
    else:
        CLIENT_DATA.append(replace_decode(message.text) + '#' + str(message.from_user.id) + '#' + 'qu')
        get_message2(message)

@bot.message_handler(content_types=["text"])
def get_message2(message):
    create_text(message)

# @bot.message_handler(content_types=["text"])
# def send_q(message):
#     bot.send_message(message.chat.id, 'Текст Вашего обращения, которое будет отправлено в компанию: ' + '\n' +
#     'ФИО: ' + ' '.join([i.split('#')[0] for i in CLIENT_DATA if str(message.from_user.id) in i and 'na' in i.split('#')]) + '\n' +
#     'Контактная информация: ' + ' '.join([i.split('#')[0] for i in CLIENT_DATA if str(message.from_user.id) in i and 'co' in i.split('#')]) + '\n' +
#     'Адрес: ' + ' '.join([i.split('#')[0] for i in CLIENT_DATA if str(message.from_user.id) in i and 'ad' in i.split('#')]) + '\n' +
#     'Вопрос: ' + ' '.join([i.split('#')[0] for i in CLIENT_DATA if str(message.from_user.id) in i and 'qu' in i.split('#')]))
#     bot.register_next_step_handler(message, send_qq)
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     btn1 = types.KeyboardButton("Да")
#     btn2 = types.KeyboardButton("Нет, полностью удалить форму.")
#     markup.add(btn1, btn2)
#     bot.send_message(message.chat.id, 'Подтвердить отправку обращения?', reply_markup=markup)
#     return

# @bot.message_handler(content_types=["text"])
# def send_qq(message):
#     if message.text == 'Да':
#         create_text(message)
#     else:
#         bot.send_message(message.chat.id, 'Ваше обращение полностью очищено!')
#         renew(message)

@bot.message_handler(content_types=["text"])
def create_text(message):
    global CLIENT_DATA, RESERVE, counter, group_id
    time = [int(i) for i in str(datetime.today())[11:-10].split(':')]
    time[0] += 3
    time = (':'.join([str(i) for i in time]))
    date = str(datetime.today())
    date = '.'.join(list(reversed(date[:10].split('-'))))
    user_nickname = message.from_user.username
    user_id = message.from_user.id
    print(CLIENT_DATA)

    bot.send_message(group_id, '*Новая заявка:  ' + '\n' 'ID запроса: ' + str(counter) + '\n' + '*Никнейм пользователя: ' + str(user_nickname) + '\n' + '*ID: '
                     + str(user_id) + '\n' +
                     '*Дата и время: ' + str(date) + ' ' + str(time) + '\n' + '*ФИО: *' + ' '.join(
        i.split('#')[0] for i in CLIENT_DATA if
        str(message.from_user.id) in i and 'na' in i.split('#')) + '\n' + '*Контактная информация: ' + ' '.join(
        i.split('#')[0] for i in CLIENT_DATA if
        str(message.from_user.id) in i and 'co' in i.split('#')) + '\n' + '*Адрес: '
                     + ' '.join(i.split('#')[0] for i in CLIENT_DATA if str(message.from_user.id) in i and 'ad' in i.split(
        '#')) + '\n' + '*Квартира: ' + ' '.join(i.split('#')[0] for i in CLIENT_DATA if
                                                 str(message.from_user.id) in i and 'fl' in i.split(
                                                     '#')) + '\n' + '*Вопрос: *' + ' '.join(
        i.split('#')[0] for i in CLIENT_DATA if str(message.from_user.id) in i and 'qu' in i.split('#')))


    for_file = str(user_nickname) + '&' + str(user_id) + '&' + str(date) + '&' + str(time) + '&' + ''.join(
        i.split('#')[0] for i in CLIENT_DATA if
        str(message.from_user.id) in i and 'na' in i.split('#')) + '&' + ' '.join(
        i.split('#')[0] for i in CLIENT_DATA if
        str(message.from_user.id) in i and 'co' in i.split('#')) + '&' + ' '.join(i.split('#')[0]
        for i in CLIENT_DATA if str(message.from_user.id) in i and 'ad' in i.split(
        '#')) + '&' + ' '.join(i.split('#')[0] for i in CLIENT_DATA if
        str(message.from_user.id) in i and 'fl' in i.split(
                                                     '#')) + '&' + ' '.join(
        i.split('#')[0] for i in CLIENT_DATA if str(message.from_user.id) in i and 'qu' in i.split('#'))

    with open('/home/aleshus2007eu/data.txt', 'a+', encoding='utf-8') as f:
        f.write(for_file + '\n')
        f.close()

    RESERVE += CLIENT_DATA
    CLIENT_DATA = [i for i in CLIENT_DATA if str(user_id) not in i]
    print(user_id)
    print(message.from_user.username)
    markup = types.ReplyKeyboardRemove()
    bot.send_message(message.chat.id, 'Ваше сообшение успешно отправлено! Благодарим за обращение!', reply_markup=markup)
    renew(message)


@bot.message_handler(content_types=["text"])
def renew(message):
    bot.send_message(message.chat.id, 'Для перехода в меню /start ')

if __name__ == "__main__":
    bot.infinity_polling()
