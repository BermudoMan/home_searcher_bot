import telebot

from config import TOKEN

from parser_ import run_parser
from dbase import create_table, cost_sorting, print_table

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, """
  Список комманд:
  /aggregate - сбор данных с сайта avito.ru (квартиры/иваново) в базу данных...(может занять какое-то время)
  /printall - вывод данных из таблицы
  /print - вывод данных из таблицы (сортировка по цене)
  /clear - очистить базу данных
                                      """)


@bot.message_handler(commands=['aggregate'])
def avito_parser(message):
    run_parser()
    bot.send_message(message.chat.id, 'Данные загружены в локальную базу данных')


@bot.message_handler(commands=['clear'])
def clear_sql_table(message):
    create_table()
    bot.send_message(message.chat.id, 'Данные в локальной базе данных очищены')


@bot.message_handler(commands=['printall'])
def printing(message):
    rows = print_table()
    for i in range(len(rows)):
        data = str(i + 1) + ') ' + str(rows[i][1]) + ' руб' + '\n' + str(rows[i][2]).replace('Объявление', '') + \
               'ССЫЛКА: ' + str(
            rows[i][3])
        bot.send_message(message.chat.id, data)


@bot.message_handler(commands=['print'])
def test(message):
    if message.text == '/print':
        bot.reply_to(message,
                     'Введите максимальное и минимальное значение цены квартиры \n Формат ввода: [min,max] - два '
                     'числа через запятую без пробелов')

        @bot.message_handler(content_types=['text'])
        def message_input_step(message):
            global text
            text = message.text
            bot.reply_to(message, f'Введенные данные: {message.text}')
            data = str(message.text).split(',')

            rows = cost_sorting(data[0], data[1])
            for i in range(len(rows)):
                data = str(i + 1) + ') ' + str(rows[i][1]) + ' руб' + '\n' + \
                       str(rows[i][2]).replace('Объявление', '') + 'ССЫЛКА: ' + str(rows[i][3])
                bot.se  nd_message(message.chat.id, data)


# @bot.message_handler(commands=['print_b']) def printing(message): rows = cost_sorting(1000000, 2000000) for i in
# range(len(rows)): data = str(i + 1) + ') ' + str(rows[i][1]) + ' руб' + '\n' + str(rows[i][2]).replace(
# 'Объявление', '') + 'ССЫЛКА: ' + str(rows[i][3]) bot.send_message(message.chat.id, data)

bot.polling()
