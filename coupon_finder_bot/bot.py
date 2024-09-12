# Основной файл, запускающий бота

# Импортируем необходимые модули из библиотеки python-telegram-bot
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from dotenv import load_dotenv
import os

load_dotenv()
telegram_token = os.getenv("TELEGRAM_TOKEN")

# Функция-обработчик команды /start
def start(update: Update, context: CallbackContext) -> None:
    # Отправляем приветственное сообщение пользователю
    update.message.reply_text('Hello! I am your discount bot. Type /help to see available commands.')

# Функция-обработчик команды /help
def help_command(update: Update, context: CallbackContext) -> None:
    # Отправляем сообщение с инструкциями по доступным командам
    update.message.reply_text('Available commands:\n/start - Start the bot\n/help - Show this help message')

# Основная функция для запуска бота
def main() -> None:
    # Создаём объект Updater, который будет управлять обновлениями и запуском бота
    updater = Updater(TOKEN)

    # Получаем диспетчер для обработки обновлений
    dispatcher = updater.dispatcher

    # Регистрируем обработчик команды /start
    dispatcher.add_handler(CommandHandler("start", start))
    # Регистрируем обработчик команды /help
    dispatcher.add_handler(CommandHandler("help", help_command))

    # Запускаем процесс опроса сервера Telegram на наличие новых сообщений
    updater.start_polling()
    # Удерживаем бота в рабочем состоянии до тех пор, пока его не остановят вручную
    updater.idle()

# Проверяем, что скрипт выполняется как основной модуль
if __name__ == '__main__':
    # Запускаем основную функцию
    main()
