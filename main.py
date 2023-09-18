import telebot
import buttons
import database

bot = telebot.TeleBot('6671873953:AAG7oKuVPyqCdywNfN0P-lcHxFrEhIDe-PI')


@bot.message_handler(commands=['start'])
def start_message(message):
    global user_id
    user_id = message.from_user.id
    bot.send_message(user_id, message.from_user.username + ' Добро пожаловать Выберите кнопку',
                     reply_markup=buttons.choice_buttons())

#
#     # получаем тг айди
#     user_id = message.from_user.id
#
#     # проверка пользователя
#     checker = database.check_user(user_id)
#     # если пользователь есть в базе
#     if checker:
#         # получаем актуальный список продуктов
#         products = database.get_pr_name_id()
#
#         # отправляем сообщение с меню
#         bot.send_message(user_id, 'привет!')
#         bot.send_message(user_id, 'выберите пункт меню' reply_markup=buttons.main_menu(products))
#
# #    Если пользователя нету в базе
# elif not checker:
#         bot.send_message(useк_id, 'Привет, назовите своё имя')
#     #  переход на этап получения имени
    bot.register_next_step_handler(message, get_name)

# Этап получения имени
def get_name(message):
    user_id = message.from_user.id

    # сохранить имя в переменную
    username = message.text
    # проверить отправил ли пользователь свой контакт
    if message.contact:
        # сохраним контакт
        phone_number = message.contact.phone_number

        # сохраняем его в базу
        database.register_user(user_id, username, phone_number)







@bot.message_handler(content_types=['text'])
def start_bot_text(message):
    if message.text == 'Заказать услугу':
        bot.send_message(user_id, 'Отправьте свою имю', reply_markup=telebot.types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, get_name)


def get_name(message):
    user_name = message.text
    bot.send_message(user_id, 'Отлично теперь отправьте номер телефона', reply_markup=buttons.number_buttons())
    bot.register_next_step_handler(message, get_number, user_name)


def get_number(message, user_name):
    if message.contact and message.contact.phone_number:
        user_number = message.contact.phone_number
        bot.send_message(user_id, 'Отправьте локацию', reply_markup=buttons.geo_buttons())
        # Переход на этап получения локации
        bot.register_next_step_handler(message, get_location, user_name, user_number)
    else:
        bot.send_message(user_id, 'Отправьте номер через кнопку!')
        bot.register_next_step_handler(message, user_name, get_number)


def get_location(message, user_name, user_number):
    if message.location:
        user_location = message.location
        bot.send_message(user_id, 'Напишите услугу', reply_markup=telebot.types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, get_service, user_name, user_number, user_location)
    else:
        bot.send_message(user_id, 'Отправьте локацию через кнопку!')
        bot.register_next_step_handler(message, user_name, user_number, get_location)


def get_service(message, user_name, user_number, user_location):
    user_service = message.text
    bot.send_message(user_id, 'Какие сроки?')
    # Перенаправляем на этап получении срока
    bot.register_next_step_handler(message, get_deadline, user_number, user_name, user_service, user_location)


def get_deadline(message, user_name, user_number, user_location, user_service):
    user_deadline = message.text

    bot.send_message(              f'Новая заявка!\n\nИмя: {user_name}'
                                  f'Номер телефона:{user_number}\n'
                                  f'Локация:{user_location}\n'
                                  f'Услуга:{user_service}\n'
                                  f'Сроки:{user_deadline}\n')
    bot.send_message(user_id, 'Успешно спасибо за ваши данные Ожидайте звонка от операторов')
    bot.register_next_step_handler(message, start_bot_text)


@bot.message_handler(content_types=['text'])
def start_text_message(message):
    if message.text == 'Википедия':
        bot.send_message(message.from_user.id, 'Введите слово')
    elif message.text == 'Перевод':
        bot.send_message(message.from_user.id, 'Введите слово для передова',
                         reply_markup=telebot.types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, translate)


def translate(message):
    if message.text.lower() == 'hello':
        bot.send_message(message.from_user.id, 'привет')
    elif message.text.lower() == 'bye':
        bot.send_message(message.from_user.id, 'пока')
    else:
        bot.send_message(message.from_user.id, 'Я не знаю что это')


bot.infinity_polling()