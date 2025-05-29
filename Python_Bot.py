from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

TOKEN = "7863942705:AAFoG3KUn7IPvYDNo7l9KoYCfT62evIsWCQ"  # Замените на реальный токен

# Ответы на команды
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я бот-автоответчик. Напишите мне что-нибудь")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Доступные команды:\n/start - начать общение\n/help - помощь")

# Автоответчик
async def auto_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text.lower()
    user_name = update.message.from_user.first_name
    
    # Логика ответов
    if "привет" in user_message:
        response = f"Привет, {user_name}! Как дела?"
    elif "как дела" in user_message:
        response = "У меня всё отлично! А у вас?"
    elif "спасибо" in user_message:
        response = "Пожалуйста! Обращайтесь ещё"
    elif "пока" in user_message:
        response = "До свидания! Хорошего дня!"
    else:
        response = "Извините, я не понял ваш вопрос. Попробуйте задать его иначе"
    
    await update.message.reply_text(response)

# Настройка и запуск бота
def main():
    # Создаем приложение
    application = Application.builder().token(TOKEN).build()
    
    # Регистрируем обработчики команд
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    
    # Регистрируем обработчик текстовых сообщений
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, auto_reply))
    
    # Запускаем бота
    print("Бот запущен...")
    application.run_polling()

if __name__ == "__main__":
    main()
