import telebot
from time import *
from telebot import *
from datetime import *
bot = TeleBot('6417715356:AAE5WBKMtAmnai-q6zsq6heVXvx7qMoQFYc')
print('Started')

client_name = contacts = client_adress = date_time_problem = client_problem = ''
final_message_to_send = ''

@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Обслуживание, ремонт, монтаж любой сложности, домашний и подъездный IP-домофон (Умный домофон), видеонаблюдение, шлагбаумы, калитки и т.д.')
    get_name1(m)

@bot.message_handler(content_types=["text"])
def get_name1(message):
    global client_name, contacts, client_adress, date_time_problem, client_problem, final_message_to_send
    client_name = contacts = client_adress = date_time_problem = client_problem = final_message_to_send = ''
    bot.send_message(message.chat.id, 'Если есть вопросы - представьтесь (ФИО), пожалуйста.')
    bot.register_next_step_handler(message, get_name2_get_contacts1)

@bot.message_handler(content_types=["text"])
def get_name2_get_contacts1(message):
    global client_name, contacts, client_adress, date_time_problem, client_problem, final_message_to_send
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Очистить форму")
    markup.add(btn1)
    if message.text == 'Очистить форму':
        bot.send_message(message.chat.id, 'Заявка очищена.')
        bot.send_message(message.chat.id, 'Новая заявка.')
        get_name1(message)
    client_name = message.text
    bot.send_message(message.chat.id, 'Предоставьте, пожалуйста, вашу контактную информацию (телефон/эл.почта). '
                                      'В случае её недостоверности обратная связь исключена.', reply_markup=markup)
    bot.register_next_step_handler(message, get_contacts2_get_adress1)
@bot.message_handler(content_types=["text"])

def get_contacts2_get_adress1(message):
    global client_name, contacts, client_adress, date_time_problem, client_problem, final_message_to_send
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Очистить форму")
    markup.add(btn1)
    if message.text == 'Очистить форму':
        bot.send_message(message.chat.id, 'Заявка очищена')
        bot.send_message(message.chat.id, 'Новая заявка')
        get_name1(message)
    else:
        contacts = message.text
        bot.send_message(message.chat.id, 'Какой Ваш адрес?', reply_markup=markup)
        bot.register_next_step_handler(message, get_adress2_get_date_time_problem1)

@bot.message_handler(content_types=["text"])
def get_adress2_get_date_time_problem1(message):
    global client_name, contacts, client_adress, date_time_problem, client_problem, final_message_to_send
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Очистить форму")
    markup.add(btn1)
    if message.text == 'Очистить форму':
        bot.send_message(message.chat.id, 'Заявка очищена.')
        bot.send_message(message.chat.id, 'Новая заявка.')
        get_name1(message)
    else:
        client_adress = message.text
        bot.send_message(message.chat.id, 'Опишите подробно, пожалуйста, возникший вопрос', reply_markup=markup)
        # bot.register_next_step_handler(message, get_date_time_problem2_get_message1)
        bot.register_next_step_handler(message, get_message2)

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
    global client_name, contacts, client_adress, date_time_problem, client_problem, final_message_to_send, x
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Очистить форму")
    markup.add(btn1)
    if message.text == 'Очистить форму':
        bot.send_message(message.chat.id, 'Заявка очищена.')
        bot.send_message(message.chat.id, 'Новая заявка.')
        get_name1(message)
    else:
        client_problem = message.text
        x = message.from_user.id
        create_text(message)

@bot.message_handler(content_types=["text"])
def create_text(message):
    global client_name, contacts, client_adress, date_time_problem, client_problem, final_message_to_send, x
    date = str(datetime.today())
    time = date.split()[1][:5]
    date = '.'.join(list(reversed(date[:10].split('-'))))
    final_message_to_send = ('ФИО: ' + client_name + '\n' + 'Контактная информация: ' + contacts + '\n'
                             + 'Адрес: ' + client_adress + '\n' + 'Дата проблемы: ' + date_time_problem + '\n'
                             + 'Проблема: ' + client_problem)
    group = -1002119559432
    user_nickname = message.from_user.username
    bot.send_message(group, '*Новая заявка: *' + '\n' + '*Никнейм пользователя: *' + user_nickname + '\n' + '*Дата и время: *' + date + '  ' + time + '\n' + '*ФИО: *' + client_name + '\n' + '*Контактная информация: *' + contacts + '\n'
                             + '*Адрес: *' + client_adress + '\n'
                             + '*Вопрос: *' + client_problem, parse_mode='Markdown')
    print(x)
    print(message.from_user.username)
    bot.send_message(message.chat.id, 'Ваша заявка принята!')
    renew(message)

@bot.message_handler(content_types=["text"])
def renew(message):
    # bot.send_message(message.chat.id, 'Новая заявка.')
    start(message)

bot.polling(none_stop=True, interval=0)


