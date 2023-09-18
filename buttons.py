from telebot import types
# from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
#
# # кнопки со всеми продуктами(основное меню)
# def main_menu(get_pr_name_id):
#     # создаем пространство для кнопок
#     buttons = InlineKeyboardMarkup(row_width=2)
# # создаем кнопки (несгораемые)
#     order = InlineKeyboardButton(text='Оформить заказ', callback_data='order')
#     cart = InlineKeyboardButton(text='Корзина', callback_data='cart')
# #     генерация кнопок с товарами (базы данных)
#     all_products = [InlineKeyboardButton(text=f'{i[0]}', callback_data=i[1]) for i in get_pr_name_id]
#
# #  Обьеденить наши кнопки с пространством
#
#     buttons.row(order)
#     buttons.add(all.products)
#     buttons.row(cart)
#
#     return buttons
#
# #  кнопки для выбора количества
# def choose_product_count(plus_or_minus='', current_amount=1):
#     #создаем пространство для кнопок
#     buttons = InlineKeyboardMarkup(row_width=3)
#     # несгораемые кнопки
#     back = InlineKeyboardButton(text='назад', callback_data='back')
#     plus = InlineKeyboardButton(text='+', callback_data='plus')
#     minus = InlineKeyboardButton(text='-', callback_data='minus')
#     cart =InlineKeyboardButton(text='Добавить в корзину', callback_data='to_cart')
#     count = InlineKeyboardButton(text=str(current_amount), callback_data=str(current_amount))
#     #отслеживать плюс или минус
#     if plus_or_minus == 'plus':
#         new_amount = int(current_amount) + 1
#
#         count = InlineKeyboardButton(text=str(new_amount), callback_data=str(new_amount))
#     elif plus_or_minus == 'minus':
#         if int(current_amount) > 1:
#             new_amount = int(current_amount) - 1
#
#             count = InlineKeyboardButton(text=str(new_amount), callback_data=str(new_amount))
#
#     buttons.add(minus, count, plus)
#     buttons.row(cart)
#     buttons.row(back)
#     return buttons
#     # кнопки чтобы потвердить заказ
# def get_accept():
#     buttons = ReplyKeyboardMarkup(resize_keyboard=True)
#
#     yes = KeyboardButton('Потвердить')
#     no = KeyboardButton ('Отменить')
#
#     buttons.add (yes, no)
#     return buttons
#
#     # кнопка для перехода в корзину
# def get_cart():
#     buttons = InlineKeyboardMarkup(row_width=1)
#
#     clear_cart = InlineKeyboardButton(text='Очистить корзину', callback_data='claer_cart')
#     order = InlineKeyboardButton(text='Оформить заказ' callback_data= 'order')
#
#
#




















def choice_buttons():
    # Создать пространство для кнопок
    buttons = types.ReplyKeyboardMarkup(resize_keyboard=True)

    # Создаем кнопки
    service_button = types.KeyboardButton('Заказать услугу')

    # Добавляем кнопки в пространство
    buttons.add(service_button)

    # вернем все эти значени
    return buttons


def number_buttons():
    # Создать пространство для кнопок
    buttons = types.ReplyKeyboardMarkup(resize_keyboard=True)

    num_button = types.KeyboardButton('Поделиться контактом', request_contact=True)

    buttons.add(num_button)

    return buttons


def geo_buttons():
    # Создать пространство для кнопок
    buttons = types.ReplyKeyboardMarkup(resize_keyboard=True)

    g_button = types.KeyboardButton('Поделиться локацием', request_location=True)

    buttons.add(g_button)

    return buttons