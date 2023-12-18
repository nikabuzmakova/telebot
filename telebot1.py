import telebot
from telebot import types
import random

# Список книг для различных тем
books_by_topic = {
    'программирование': ['Clean Code', 'Code Complete', 'Python Crash Course'],
    'наука': ['A Brief History of Time', 'Sapiens', 'Cosmos'],
    'фантастика': ['Dune', 'Neuromancer', 'The Hitchhiker\'s Guide to the Galaxy'],
    'роман': ['Pride and Prejudice', 'To Kill a Mockingbird', 'Jane Eyre'],
    'детектив': ['Sherlock Holmes', 'The Girl with the Dragon Tattoo', 'Gone Girl'],
}

# Список авторов
authors = ['Agatha Christie', 'Stephen King', 'Jane Austen', 'Isaac Asimov', 'J.K. Rowling']

# Токен бота
token = 'token'
bot = telebot.TeleBot(token)

# Обработчик команды /recommend
@bot.message_handler(commands=['recommend'])
def recommend(message):
    try:
        category = message.text.split(' ', 1)[1].lower()
    except IndexError:
        bot.reply_to(message, 'Укажите тему, автора или жанр для рекомендации, например: /recommend программирование')
        return

    if category:
        if category in books_by_topic:
            book = random.choice(books_by_topic[category])
            bot.reply_to(message, f'Рекомендую книгу по теме "{category}": {book}')
        elif category in authors:
            author_books = [book for genre_books in books_by_topic.values() for book in genre_books if category in book]
            if author_books:
                book = random.choice(author_books)
                bot.reply_to(message, f'Рекомендую книгу от автора "{category}": {book}')
            else:
                bot.reply_to(message, f'Нет информации о книгах от автора "{category}" в моей базе данных.')
        else:
            bot.reply_to(message, f'Неизвестная категория: {category}.')
    else:
        bot.reply_to(message, 'Укажите тему, автора или жанр для рекомендации, например: /recommend программирование')

# Обработчик команды /help
@bot.message_handler(commands=['help'])
def help_command(message):
    available_genres = ', '.join(books_by_topic.keys())
    help_text = "Список доступных команд:\n"
    help_text += "/recommend <категория> - Получить рекомендацию книги по заданной теме, автору или жанру.\n"
    help_text += "/help - Справка.\n"
    help_text += f"Бот знает следующие жанры: {available_genres}."
    bot.reply_to(message, help_text)

# Запуск бота
if __name__ == '__main__':
    bot.polling(none_stop=True)
