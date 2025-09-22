import datetime
from telebot import *
import math
import time
from time import *
from datetime import *
import os
from sys import *
from telebot.types import InlineKeyboardMarkup
bot = telebot.TeleBot('token1', skip_pending=True)  # TG TEST
# bot = telebot.TeleBot('token2', skip_pending=True)  # TG MAIN
file_admins = open(r'C:\Users\alesh\OneDrive\Desktop\botTG\admins.txt')
# file_admins = open('/home/aleshus2007eu/admins.txt')
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
    t = [i for i in s if i not in symbols]
    return ''.join(t)

@bot.message_handler(content_types=['photo'])
def photo_assign(message):
    # fileID = message.photo[-1].file_id
    # date = str(datetime.now())[:-4]
    # date1 = '_'.join(str(date).split())
    # date_name = '^'.join(i for i in str(date1).split(':'))
    # file_info = bot.get_file(fileID)
    # capt = str(message.caption)

    # downloaded_file = bot.download_file(file_info.file_path)
    # addr = "image_" + str(user_id) + "_" + str(date_name) + ".jpg"
    # with open(addr, 'wb') as new_file:
    #     new_file.write(downloaded_file)
    #     new_file.close()
    # CLIENT_DATA.append(str(user_id) + '#photo#' + addr)
    # CLIENT_DATA.append(str(user_id) + '#captphoto#' + capt)
    # print(CLIENT_DATA)
    # file_info = bot.get_file(message.video.file_id)
    #     # date = str(datetime.now())[:-4]
    #     # date1 = '_'.join(str(date).split())
    #     # date_name = '^'.join(i for i in str(date1).split(':'))
    #     # downloaded_file = bot.download_file(file_info.file_path)
    #     # user_id = message.from_user.id
    global CLIENT_DATA
    file_path = bot.get_file(message.photo[-1].file_id).file_path
    file_id = bot.get_file(message.photo[-1].file_id).file_id
    file_info = bot.get_file(message.photo[-1].file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    media_link = f'http://api.telegram.org/file/bot7355802592:AAHQwrC1DoNHEOj93jQngTuX1MoWp_kSwWs/{file_path}'
    print(f'http://api.telegram.org/file/bot7355802592:AAHQwrC1DoNHEOj93jQngTuX1MoWp_kSwWs/{file_path}')
    user_id = message.from_user.id
    capt = str(message.caption)
    date = str(datetime.now())[:-4]
    date1 = '_'.join(str(date).split())
    date_name = '^'.join(i for i in str(date1).split(':'))
    src = str(user_id) + str(date_name) + '.jpg'
    with open(src, 'wb') as new_file:
        new_file.write(downloaded_file)
        new_file.close()
    print(capt)
    CLIENT_DATA.append(str(user_id) + '#photo#' + str(media_link))
    CLIENT_DATA.append(str(user_id) + '#captphot#' + capt)
    return

@bot.message_handler(content_types=['video'])
def video_assign(message):
    # file_path = bot.get_file(message.video.file_id).file_path
    # file_id = bot.get_file(message.video.file_id).file_id
    # print(f'http://api.telegram.org/file/bot7355802592:AAHQwrC1DoNHEOj93jQngTuX1MoWp_kSwWs/{file_path}')
    # # file_info = bot.get_file(message.video.file_id)
    # # date = str(datetime.now())[:-4]
    # # date1 = '_'.join(str(date).split())
    # # date_name = '^'.join(i for i in str(date1).split(':'))
    # # downloaded_file = bot.download_file(file_info.file_path)
    # # user_id = message.from_user.id
    # capt = str(message.caption)
    # print(capt)
    # # with open(addr, 'wb') as new_file:
    # #     new_file.write(downloaded_file)
    # #     new_file.close()
    # # CLIENT_DATA.append(str(user_id) + '#video#' + addr)
    # # CLIENT_DATA.append(str(user_id) + '#captvid#' + capt)
    # # print(CLIENT_DATA)
    # return
    global CLIENT_DATA
    file_path = bot.get_file(message.video.file_id).file_path
    file_id = bot.get_file(message.video.file_id).file_id
    file_info = bot.get_file(message.video.file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    media_link = f'http://api.telegram.org/file/bot7355802592:AAHQwrC1DoNHEOj93jQngTuX1MoWp_kSwWs/{file_path}'
    print(f'http://api.telegram.org/file/bot7355802592:AAHQwrC1DoNHEOj93jQngTuX1MoWp_kSwWs/{file_path}')
    user_id = message.from_user.id
    capt = str(message.caption)
    date = str(datetime.now())[:-4]
    date1 = '_'.join(str(date).split())
    date_name = '^'.join(i for i in str(date1).split(':'))
    src = str(user_id) + str(date_name)+ '.mp4'
    with open(src, 'wb') as new_file:
        new_file.write(downloaded_file)
        new_file.close()
    print(capt)
    CLIENT_DATA.append(str(user_id) + '#video#' + str(media_link))
    CLIENT_DATA.append(str(user_id) + '#captvid#' + capt)
    return

@bot.message_handler(content_types=['document'])
def documents_assign(message):
    global CLIENT_DATA
    file_path = bot.get_file(message.document.file_id).file_path
    file_id = bot.get_file(message.document.file_id).file_id
    file_info = bot.get_file(message.document.file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    media_link = f'http://api.telegram.org/file/bot7355802592:AAHQwrC1DoNHEOj93jQngTuX1MoWp_kSwWs/{file_path}'
    print(f'http://api.telegram.org/file/bot7355802592:AAHQwrC1DoNHEOj93jQngTuX1MoWp_kSwWs/{file_path}')
    user_id = message.from_user.id
    capt = str(message.caption)
    date = str(datetime.now())[:-4]
    date1 = '_'.join(str(date).split())
    date_name = '^'.join(i for i in str(date1).split(':'))
    file_name = message.document.file_name.split('.')
    file_ext = file_name[1]
    src = str(user_id) + str(date_name) + '.' + str(file_ext)
    with open(src, 'wb') as new_file:
        new_file.write(downloaded_file)
        new_file.close()
    print(capt)
    CLIENT_DATA.append(str(user_id) + '#documents#' + str(media_link))
    CLIENT_DATA.append(str(user_id) + '#docs#' + capt)

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
    button_wa = types.InlineKeyboardButton("Открыть в ТГ", web_app=web_info)
    button_web = types.InlineKeyboardButton("Открыть в Браузере", url='https://domofon-servis-odi.ru')
    markup.add(button_wa, button_web)
    bot.send_message(message.chat.id, 'ВНИМАНИЕ!!!\n'
                                      '   - За последнее время были зафиксированы случаи мошенничества на обслуживаемых нами адресах!\n'
            '   - Если Вы получили сообщение/звонок о некой замене домофона и необходимости заказать и оплатить новые ключи - это могут быть мошенники!\n'
            '   - Всегда проверяйте информацию по доверенным источникам - по контактам, указанным в этом Телеграм-боте и на нашем сайте\n'
                                      '    Будьте бдительны!\n'
                                      '----------------------------------------------------------------------\n'
                                      '* Тел. +7 (495) 596-16-03\n'
                                      '* E-mail: 5961603@mail.ru\n'
                                      '* Адрес: г. Одинцово, ул. Маршала Жукова д.34 п.3\n'
                                      '* Время работы: пн-пт 9:00-18:00, перерыв 13:00-14:00\n'
                                      '* Наш сайт: https://domofon-servis-odi.ru', reply_markup=markup)
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
    global group_id, CLIENT_DATA
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Назад")
    if message.content_type in ['photo', 'video', 'document']:
        if message.content_type == 'photo':
            print(message)
            photo_assign(message)
            print('фото прикреплено')
            bot.send_message(message.chat.id, 'Медиа успешно прикреплены!')
            bot.send_message(message.chat.id,
                             'Оставьте здесь своё сообщение разработчику или вернитесь по кнопке "Назад"',
                             reply_markup=markup)
            bot.register_next_step_handler(message, questions_tg_bot2)
        elif message.content_type == 'video':
            video_assign(message)
            print('видео прикреплено')
            bot.send_message(message.chat.id, 'Медиа успешно прикреплены!')
            questions_tg_bot1(message)
        elif message.content_type == 'document':
            documents_assign(message)
            print('документы прикреплено')
            bot.send_message(message.chat.id, 'Медиа успешно прикреплены!')
            questions_tg_bot1(message)
    else:
        msg1 = message.text
        if msg1 == 'Назад':
            redirect(message)
        else:
            msg = 'Сообщение: ' + msg1
            user_id = message.from_user.id
            bot.send_message(group_id, 'ID пользователя: ' + str(message.from_user.id) + '\n' + msg)
            print(CLIENT_DATA)
            MEDIA = [i.split('#')[-1] for i in CLIENT_DATA if
                     str(message.from_user.id) in i and 'photo' in i or 'video' in i]
            CAPTIONS = [i.split('#')[-1] for i in CLIENT_DATA if
                        str(message.from_user.id) in i and 'captphot' in i or 'captvid' in i]
            if MEDIA:
                bot.send_message(group_id,
                                 'Медиа: \n' + '\n\n'.join(MEDIA) + '\nПодписи к медиа:\n' + '\n\n'.join(CAPTIONS))
            bot.send_message(message.chat.id, 'Сообщение отправляется...')
            bot.send_message(message.chat.id, 'Сообщение отправлено!', reply_markup=types.ReplyKeyboardRemove())
            CLIENT_DATA = [i for i in CLIENT_DATA if str(user_id) not in i]
            redirect(message)

@bot.message_handler(commands=['start'])
def start(m, res=False):
    global count_users
    markup = types.ReplyKeyboardMarkup(resize_keyboard=False)
    btn1 = types.KeyboardButton("Полезная информация о нас")
    btn2 = types.KeyboardButton("Оплата/погашение задолженности")
    btn3 = types.KeyboardButton("Вопрос технического или иного характера")
    btn4 = types.KeyboardButton("Вопросы/предложения по работе этого Телеграм-бота")
    btn5 = types.KeyboardButton("Админ-панель")
    markup.add(btn1)
    markup.add(btn2)
    markup.add(btn3)
    markup.add(btn4)
    markup.add(btn5)
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
        btn3 = types.KeyboardButton("Отправить файл")
        btn4 = types.KeyboardButton("Назад")
        markup.add(btn1)
        markup.add(btn2)
        markup.add(btn3)
        markup.add(btn4)
        bot.send_message(message.chat.id, 'Выберите нужную функцию при помощи кнопок', reply_markup=markup)
        bot.register_next_step_handler(message, admin_panel)

@bot.message_handler(content_types=['text'])
def send_file_1(message):
    bot.send_message(message.chat.id, 'Введите ID.')
    bot.register_next_step_handler(message, send_file_2)

@bot.message_handler(content_types=['text'])
def send_file_2(message):
    user_id_answ = message.caption
    file_id = message.document.file_id
    bot.send_document(user_id_answ, file_id)
    bot.send_message(message.chat.id, 'Файл отправлен!')
    redirect(message)
    return


@bot.message_handler(content_types=["text"])
def admin_panel(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=False)
    btn1 = types.KeyboardButton("Ответить на обращение")
    btn2 = types.KeyboardButton("Системная информация")
    btn3 = types.KeyboardButton("Отправить файл")
    btn4 = types.KeyboardButton("Назад")
    markup.add(btn1)
    markup.add(btn2)
    markup.add(btn3)
    markup.add(btn4)
    if message.text == 'Ответить на обращение':
        reply_id1(message)
    elif message.text == 'Системная информация':
       system_info(message)
    elif message.text == 'Отправить файл':
        send_file_1(message)
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

# @bot.message_handler(content_types=["text"])
# def history(message):
#     us_id = message.from_user.id
#     print(us_id)
#     f = open('/home/aleshus2007eu/data.txt', encoding='utf-8')
#     msgs = f.readlines()
#     res = []
#     for i in msgs:
#         if int(i.split('&')[2]) == us_id:
#             res.append(i)
#     if not res:
#         bot.send_message(message.chat.id, 'История пуста.')
#         redirect(message)
#     else:
#         reply = []
#         for i in res:
#             line = i.split('&')[2:]
#             date = line[0]
#             time = line[1]
#             question = line[-2]
#             status = line.strip()[-1]
#             joined = ('\n' + 'Дата: ' + date + '\n' + 'Время: ' + time + '\n' + 'Вопрос: ' + question  + '\n' + 'Статус: ' + status + '\n')
#             reply.append(joined)
#         bot.send_message(message.chat.id, '\n############################\n'.join(reply))
#         redirect(message)


def redirect(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=False, one_time_keyboard=True)
    btn1 = types.KeyboardButton("Полезная информация о нас")
    btn2 = types.KeyboardButton("Оплата/погашение задолженности")
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
    btn1 = types.KeyboardButton("Полезная информация о нас")
    btn2 = types.KeyboardButton("Оплата/погашение задолженности")
    btn3 = types.KeyboardButton("Вопрос технического или иного характера")
    btn4 = types.KeyboardButton("Вопросы/предложения по работе этого Телеграм-бота")
    btn5 = types.KeyboardButton("Админ-панель")
    markup.add(btn1)
    markup.add(btn2)
    markup.add(btn3)
    markup.add(btn4)
    markup.add(btn5)
    if message.text == 'Оплата/погашение задолженности':
        bot.send_message(message.chat.id, 'По данному вопросу, пожалуйста обратитесь напрямую в Диспетчерскую по тел. +7(495)596-16-03 пн-пт 9:00-18:00, эл.почта 5961603@mail.ru' + '\n' +
        'ВНИМАНИЕ! Если вы были заблокированы в приложении Спутник "Наш Дом", скорее всего, у Вас есть задолженность по оплате наших услуг. Обратитесь в Диспетчерскую.', reply_markup=markup)
        redirect(message)
    elif message.text == 'Вопрос технического или иного характера':
        bot.send_message(message.chat.id, 'Ответьте на все вопросы, мы постараемся помочь Вам.')
        get_name1(message)
    elif message.text == 'Полезная информация о нас':
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
                                      ' вопросу можно будет по кнопке "Очистить форму" начиная со следующего вопроса.', reply_markup=markup)
    bot.register_next_step_handler(message, get_name2_get_contacts1)


@bot.message_handler(content_types=["text"])
def get_name2_get_contacts1(message):
    global CLIENT_DATA
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    btn1 = types.KeyboardButton("Очистить форму")
    markup.add(btn1)
    if message.content_type in ['photo', 'video', 'document']:
        if message.content_type == 'photo':
            print(message)
            photo_assign(message)
            print('фото прикреплено')
            bot.send_message(message.chat.id, 'Медиа успешно прикреплены!')
            get_name1(message)
        elif message.content_type == 'video':
            video_assign(message)
            print('видео прикреплено')
            bot.send_message(message.chat.id, 'Медиа успешно прикреплены!')
            get_name1(message)
        elif message.content_type == 'document':
            documents_assign(message)
            print('docs прикреплено')
            bot.send_message(message.chat.id, 'Медиа успешно прикреплены!')
            get_name1(message)
    else:
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
    if message.content_type in ['photo', 'video', 'document']:
        if message.content_type == 'photo':
            photo_assign(message)
            print('фото прикреплено')
            bot.send_message(message.chat.id, 'Медиа успешно прикреплены!')
            bot.send_message(message.chat.id,
                             'Предоставьте, пожалуйста, вашу контактную информацию (телефон/эл.почта). '
                             'В случае её недостоверности обратная связь будет невозможна.', reply_markup=markup)
            bot.register_next_step_handler(message, get_contacts2_get_adress1)
        elif message.content_type == 'video':
            video_assign(message)
            print('видео прикреплено')
            bot.send_message(message.chat.id, 'Медиа успешно прикреплены!')
            bot.send_message(message.chat.id,
                             'Предоставьте, пожалуйста, вашу контактную информацию (телефон/эл.почта). '
                             'В случае её недостоверности обратная связь будет невозможна.', reply_markup=markup)
            bot.register_next_step_handler(message, get_contacts2_get_adress1)
        elif message.content_type == 'document':
            documents_assign(message)
            print('docs прикреплено')
            bot.send_message(message.chat.id, 'Медиа успешно прикреплены!')
            bot.send_message(message.chat.id,
                             'Предоставьте, пожалуйста, вашу контактную информацию (телефон/эл.почта). '
                             'В случае её недостоверности обратная связь будет невозможна.', reply_markup=markup)
            bot.register_next_step_handler(message, get_contacts2_get_adress1)
    else:
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
    if message.content_type in ['photo', 'video', 'document']:
        if message.content_type == 'photo':
            photo_assign(message)
            print('фото прикреплено')
            bot.send_message(message.chat.id, 'Медиа успешно прикреплены!')
            bot.send_message(message.chat.id, 'Укажите улицу, номер дома и подъезд.', reply_markup=markup)
            bot.register_next_step_handler(message, get_adress2_get_date_time_problem1)
        elif message.content_type == 'video':
            video_assign(message)
            print('видео прикреплено')
            bot.send_message(message.chat.id, 'Медиа успешно прикреплены!')
            bot.send_message(message.chat.id, 'Укажите улицу, номер дома и подъезд.', reply_markup=markup)
            bot.register_next_step_handler(message, get_adress2_get_date_time_problem1)
        elif message.content_type == 'document':
            documents_assign(message)
            print('docs прикреплено')
            bot.send_message(message.chat.id, 'Медиа успешно прикреплены!')
            bot.send_message(message.chat.id, 'Укажите улицу, номер дома и подъезд.', reply_markup=markup)
            bot.register_next_step_handler(message, get_adress2_get_date_time_problem1)
    else:
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
    if message.content_type in ['photo', 'video', 'document']:
        if message.content_type == 'photo':
            photo_assign(message)
            print('фото прикреплено')
            bot.send_message(message.chat.id, 'Фото успешно прикреплено!')
            bot.send_message(message.chat.id, 'Пожалуйста, укажите номер квартиры, это очень важно для нас.',
                             reply_markup=markup)
            bot.register_next_step_handler(message, get_flat)
        elif message.content_type == 'video':
            video_assign(message)
            print('видео прикреплено')
            bot.send_message(message.chat.id, 'Видео успешно прикреплено!')
            bot.send_message(message.chat.id, 'Пожалуйста, укажите номер квартиры, это очень важно для нас.',
                             reply_markup=markup)
            bot.register_next_step_handler(message, get_flat)
        elif message.content_type == 'document':
            documents_assign(message)
            print('docs прикреплено')
            bot.send_message(message.chat.id, 'Медиа успешно прикреплены!')
            bot.send_message(message.chat.id, 'Пожалуйста, укажите номер квартиры, это очень важно для нас.',
                             reply_markup=markup)
            bot.register_next_step_handler(message, get_flat)
    else:
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
    if message.content_type in ['photo', 'video', 'document']:
        if message.content_type == 'photo':
            photo_assign(message)
            print('фото прикреплено')
            bot.send_message(message.chat.id, 'Медиа успешно прикреплены!')
            bot.send_message(message.chat.id, 'Пожалуйста, подробно опишите Ваш вопрос. После этого бот автоматически '
                                              'отправит Ваше обращение нам.', reply_markup=markup)
            bot.register_next_step_handler(message, get_problem)
        elif message.content_type == 'video':
            video_assign(message)
            print('видео прикреплено')
            bot.send_message(message.chat.id, 'Медиа успешно прикреплены!')
            bot.send_message(message.chat.id, 'Пожалуйста, подробно опишите Ваш вопрос. После этого бот автоматически '
                                              'отправит Ваше обращение нам.', reply_markup=markup)
            bot.register_next_step_handler(message, get_problem)
        elif message.content_type == 'document':
            documents_assign(message)
            print('docs прикреплено')
            bot.send_message(message.chat.id, 'Пожалуйста, подробно опишите Ваш вопрос. После этого бот автоматически '
                                              'отправит Ваше обращение нам.', reply_markup=markup)
            bot.send_message(message.chat.id, 'Медиа успешно прикреплены!')
            bot.register_next_step_handler(message, get_problem)
    else:
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
    global CLIENT_DATA, RESERVE, group_id
    time = [int(i) for i in str(datetime.today())[11:-10].split(':')]
    time[0] += 3
    time = (':'.join([str(i) for i in time]))
    date = str(datetime.today())
    date = '.'.join(list(reversed(date[:10].split('-'))))
    user_nickname = message.from_user.username
    user_id = message.from_user.id
    bot.send_message(message.chat.id, 'Идёт отправка сообщения...')
    print(CLIENT_DATA)
    bot.send_message(group_id, '*Новая заявка:  ' + '\n' 'ID запроса: ' + '\n' + '*Никнейм пользователя: ' + str(user_nickname) + '\n' + '*ID: '
                     + str(user_id) + '\n' +
                     '*Дата и время: ' + str(date) + ' ' + str(time) + '\n' + '*ФИО: ' + ' '.join(
        i.split('#')[0] for i in CLIENT_DATA if
        str(message.from_user.id) in i and 'na' in i.split('#')) + '\n' + '*Контактная информация: ' + ' '.join(
        i.split('#')[0] for i in CLIENT_DATA if
        str(message.from_user.id) in i and 'co' in i.split('#')) + '\n' + '*Адрес: '
                     + ' '.join(i.split('#')[0] for i in CLIENT_DATA if str(message.from_user.id) in i and 'ad' in i.split(
        '#')) + '\n' + '*Квартира: ' + ' '.join(i.split('#')[0] for i in CLIENT_DATA if
                                                 str(message.from_user.id) in i and 'fl' in i.split(
                                                     '#')) + '\n' + '*Вопрос: ' + ' '.join(
        i.split('#')[0] for i in CLIENT_DATA if str(message.from_user.id) in i and 'qu' in i.split('#')))

    MEDIA = [i.split('#')[-1] for i in CLIENT_DATA if str(message.from_user.id) in i and 'photo' in i or 'video' in i or 'documents' in i]
    CAPTIONS = [i.split('#')[-1] for i in CLIENT_DATA if str(message.from_user.id) in i and 'captphot' in i or 'captvid' in i or 'docs' in i]
    if MEDIA:
        bot.send_message(group_id, 'Медиа: \n' + '\n\n'.join(MEDIA) + '\nПодписи к медиа:\n' + '\n\n'.join(CAPTIONS))
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

    with open(r'C:\Users\alesh\OneDrive\Desktop\botTG\data.txt', 'a+', encoding='utf-8') as f:
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

