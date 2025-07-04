from telebot import *

bot = TeleBot('7355802592:AAHQwrC1DoNHEOj93jQngTuX1MoWp_kSwWs') # TG TEST VERSION
# bot = TeleBot('6417715356:AAE3fSAIO_M6_TN8lX2kYb1V6DXDCw_z1Dk') # TG MAIN VERSION
file_admins = open('/home/aleshus2007eu/admins.txt')
file_blocked_users = open('/home/aleshus2007eu/blocked_users.txt')
admins = [int(i) for i in file_admins]
print(admins)
blocked_users = [i for i in file_blocked_users]
count_users = 0
CLIENT_DATA = []
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

group_id = 7355802592
@bot.message_handler(commands=['start'])
def start(m, res=False):
    global count_users
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Оплата/погашение задолжности")
    btn2 = types.KeyboardButton("Вопрос технического или иного характера")
    markup.add(btn1)
    markup.add(btn2)
    bot.send_message(m.chat.id, 'Приветствуем Вас в нашем ТГ-боте!' + '\n' + '#########################' + '\n' + '\n' + 'Это обновленная версия бота, в случае некорректной работы, пожалуйста, '
     'пишите на эл.почту разработчика aleshus2007@gmail.com, это поможет нам найти и пофиксить баги в кратчайшие сроки. Также у нас есть свой сайт https://alekseyelcha.github.io' + '\n' +
        '#########################' + '\n' + '\n' +'Выберите характер интересующего Вас вопроса, нажав на соответсвующую кнопку.', reply_markup=markup)
    count_users += 1
    bot.register_next_step_handler(m, get_quest_type)

@bot.message_handler(content_types=["text"])
def get_quest_type(message):
    if message.text == 'Оплата/погашение задолжности':
        markup = types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, 'По данному вопросу, пожалуйста обратитесь напрямую в Диспетчерскую по тел. +7(495)596-16-03, эл.почта 5961603@mail.ru' + '\n' +
        'ВНИМАНИЕ! Если вы были заблокированы в приложении Спутник: "Наш Дом", скорее всего, у Вас есть задолженность по оплате наших услуг. Обратитесь в Диспетчерскую.', reply_markup=markup)
        renew(message)
    elif message.text == 'Вопрос технического или иного характера':
        bot.send_message(message.chat.id, 'Ответьте на все вопросы, мы постараемся помочь Вам.')
        get_name1(message)
    else:
        bot.send_message(message.chat.id, 'Ошибка! Повторите попытку.')
        bot.register_next_step_handler(message, get_quest_type)

@bot.message_handler(content_types=["text"])
def get_name1(message):
    markup = types.ReplyKeyboardRemove()
    bot.send_message(message.chat.id, 'Представьтесь (ФИО), пожалуйста.', reply_markup=markup)
    bot.register_next_step_handler(message, get_name2_get_contacts1)

# @bot.message_handler(content_types=["text"])
# def site(message):
#     markup = types.InlineKeyboardMarkup()
#     web_info = types.WebAppInfo('https://alekseyelcha.github.io')
#     button_wa = types.InlineKeyboardButton("*Открыть в ТГ*", web_app=web_info, parse_mode='Markdown')
#     button_web = types.InlineKeyboardButton("Открыть в Браузере", url='https://alekseyelcha.github.io')
#     markup.add(button_wa, button_web)
#     bot.send_message(message.chat.id, "На сайте теперь можно отправить обращение через Google Forms (Гугл Формы)!" + '\n' + "*Наш сайт:*",
#                          reply_markup=markup, parse_mode='Markdown')

@bot.message_handler(content_types=["text"])
def get_name2_get_contacts1(message):
    global CLIENT_DATA
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Очистить форму")
    markup.add(btn1)
    if message.text == 'Очистить форму':
        bot.send_message(message.chat.id, 'Заявка очищена.')
        CLIENT_DATA = [i for i in CLIENT_DATA if str(message.from_user.id) not in i]
        bot.send_message(message.chat.id, 'Новая заявка.')
        get_name1(message)
    elif message.text == '/check':
        check_status(message)
    elif message.text == '/admin':
        admin(message)
    else:
        CLIENT_DATA.append(replace_decode(message.text) + '#' + str(message.from_user.id) + '#' + 'na')

        bot.send_message(message.chat.id, 'Предоставьте, пожалуйста, вашу контактную информацию (телефон/эл.почта). '
                                          'В случае её недостоверности обратная связь исключена.', reply_markup=markup)

        bot.register_next_step_handler(message, get_contacts2_get_adress1)

@bot.message_handler(content_types=["text"])
def get_contacts2_get_adress1(message):
    global CLIENT_DATA
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Очистить форму")
    markup.add(btn1)
    if message.text == 'Очистить форму':
        bot.send_message(message.chat.id, 'Заявка очищена')
        CLIENT_DATA = [i for i in CLIENT_DATA if str(message.from_user.id) not in i]
        bot.send_message(message.chat.id, 'Новая заявка')
        get_name1(message)
    else:
        CLIENT_DATA.append(replace_decode(message.text) + '#' + str(message.from_user.id) + '#' + 'co')
        bot.send_message(message.chat.id, 'Какой Ваш адрес? Укажите улицу, номер дома и подъезд.', reply_markup=markup)
        bot.register_next_step_handler(message, get_adress2_get_date_time_problem1)

@bot.message_handler(content_types=["text"])
def get_adress2_get_date_time_problem1(message):
    global CLIENT_DATA
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Очистить форму")
    markup.add(btn1)
    if message.text == 'Очистить форму':
        bot.send_message(message.chat.id, 'Заявка очищена.')
        CLIENT_DATA = [i for i in CLIENT_DATA if str(message.from_user.id) not in i]
        bot.send_message(message.chat.id, 'Новая заявка.')
        get_name1(message)
    else:
        CLIENT_DATA.append(replace_decode(message.text) + '#' + str(message.from_user.id) + '#' + 'ad')
        bot.send_message(message.chat.id, 'Пожалуйста, укажите номер квартиры, это очень важно для нас.')
        bot.register_next_step_handler(message, get_flat)

@bot.message_handler(content_types=["text"])
def get_flat(message):
    global CLIENT_DATA
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Очистить форму")
    markup.add(btn1)
    if message.text == 'Очистить форму':
        bot.send_message(message.chat.id, 'Заявка очищена.')
        CLIENT_DATA = [i for i in CLIENT_DATA if str(message.from_user.id) not in i]
        bot.send_message(message.chat.id, 'Новая заявка.')
        get_name1(message)
    else:
        CLIENT_DATA.append(replace_decode(message.text) + '#' + str(message.from_user.id) + '#' + 'fl')
        bot.send_message(message.chat.id, 'Опишите подробно, пожалуйста, возникший вопрос.', reply_markup=markup)
        us_id = message.from_user.id
        bot.register_next_step_handler(message, get_problem)

@bot.message_handler(content_types=["text"])
def get_problem(message):
    global CLIENT_DATA
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Очистить форму")
    markup.add(btn1)
    if message.text == 'Очистить форму':
        bot.send_message(message.chat.id, 'Заявка очищена.')
        CLIENT_DATA = [i for i in CLIENT_DATA if str(message.from_user.id) not in i]
        bot.send_message(message.chat.id, 'Новая заявка.')
        get_name1(message)
    else:
        CLIENT_DATA.append(replace_decode(message.text) + '#' + str(message.from_user.id) + '#' + 'qu')
        get_message2(message)

@bot.message_handler(content_types=["text"])
def get_message2(message):
    send_q(message)

@bot.message_handler(content_types=["text"])
def send_q(message):
    bot.send_message(message.chat.id, 'Текст Вашего обращения, которое будет отправлено в компанию: ' + '\n' +
    'ФИО: ' + ' '.join([i.split('#')[0] for i in CLIENT_DATA if str(message.from_user.id) in i and 'na' in i.split('#')]) + '\n' +
    'Контактная информация: ' + ' '.join([i.split('#')[0] for i in CLIENT_DATA if str(message.from_user.id) in i and 'co' in i.split('#')]) + '\n' +
    'Адрес: ' + ' '.join([i.split('#')[0] for i in CLIENT_DATA if str(message.from_user.id) in i and 'ad' in i.split('#')]) + '\n' +
    'Вопрос: ' + ' '.join([i.split('#')[0] for i in CLIENT_DATA if str(message.from_user.id) in i and 'qu' in i.split('#')]))

    bot.register_next_step_handler(message, send_qq)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Да")
    btn2 = types.KeyboardButton("Нет, полностью удалить форму.")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, 'Подтвердить отправку обращения?', reply_markup=markup)
@bot.message_handler(content_types=["text"])
def send_qq(message):

    if message.text == 'Да':
        create_text(message)
    else:
        bot.send_message(message.chat.id, 'Ваше обращение полностью очищено!')
        renew(message)

@bot.message_handler(content_types=["text"])
def create_text(message):
    global CLIENT_DATA
    time = [int(i) for i in str(datetime.today())[11:-10].split(':')]
    time[0] += 3
    time = (':'.join([str(i) for i in time]))
    date = str(datetime.today())
    date = '.'.join(list(reversed(date[:10].split('-'))))
    group = -1002119559432
    user_nickname = message.from_user.username
    user_id = message.from_user.id
    print(CLIENT_DATA)
    bot.send_message(group, '*Новая заявка:  ' + '\n' + '*Никнейм пользователя: ' + str(user_nickname) + '\n' + '*ID: '
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
    CLIENT_DATA = [i for i in CLIENT_DATA if str(user_id) not in i]
    print(user_id)
    print(message.from_user.username)
    markup = types.ReplyKeyboardRemove()
    bot.send_message(message.chat.id, 'Ваша заявка отправлена! Благодарим за обращение!', reply_markup=markup)
    renew(message)


@bot.message_handler(content_types=["text"])
def renew(message):
    bot.send_message(message.chat.id, 'Для создания нового обращения нажмите /start ')

if __name__ == "__main__":
    bot.infinity_polling(none_stop=True, timeout=2440)
