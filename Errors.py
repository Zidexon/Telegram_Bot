from telegram.error import NetworkError


def main():
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))

    try:
        application.run_polling()
    except NetworkError as e:
        print(f"Ошибка сети: {e}")
        # Здесь можно добавить повторное подключение