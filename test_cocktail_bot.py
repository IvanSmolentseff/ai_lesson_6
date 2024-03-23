import telebot
import openai

# Установка токенов и ключей
TELEGRAM_TOKEN = "6916982472:AAHqstufUf20XEyR5G79DlZHlo8AgYmNd1U"
OPENAI_API_KEY = "sk-ywhHY51tVhkZGWF5p1ErT3BlbkFJJfpuPO7yHGckcoqk____"  # Если нужно проверить в работе вышлю полный api_key

# Настройка OpenAI API
openai.api_key = OPENAI_API_KEY

# Инициализация бота
bot = telebot.TeleBot(TELEGRAM_TOKEN)

# Обработка команды /start
@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.reply_to(message, "Привет! Я Бот-Бармен, спроси меня про коктейли!")

# Обработка входящих сообщений
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    # Получение вопроса от пользователя
    user_question = message.text

    # Запрос к модели ChatGPT для получения ответа
    response = openai.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt=user_question,
        temperature=0.7,
        max_tokens=100
    )

    # Отправка ответа пользователю в Telegram
    bot.reply_to(message, response.choices[0].text.strip())


# Запуск бота
bot.polling()
