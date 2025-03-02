Для создания Telegram-бота с использованием библиотеки `python-telegram-bot` версии 20.x и `requests`, а также с функционалом логирования ошибок и автоматическим перезапуском при сбоях, можно использовать следующий код:

### Установка зависимостей
Сначала установите необходимые библиотеки:

```bash
pip install python-telegram-bot requests
```

### Код бота

```python
import logging
import os
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filename='bot_errors.log'
)
logger = logging.getLogger(__name__)

# Обработчик команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Привет! Я бот. Используй /help для получения списка команд.')

# Обработчик команды /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Доступные команды:\n/start - Начать работу с ботом\n/help - Получить справку')

# Функция для автоматического перезапуска при сбоях
async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.error(f'Update {update} caused error {context.error}')
    # Здесь можно добавить логику для перезапуска бота
    # Например, можно использовать os.execv для перезапуска скрипта
    os.execv(sys.executable, ['python'] + sys.argv)

# Основная функция
def main():
    # Создаем приложение бота
    application = ApplicationBuilder().token('YOUR_BOT_TOKEN').build()

    # Регистрируем обработчики команд
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))

    # Регистрируем обработчик ошибок
    application.add_error_handler(error_handler)

    # Запускаем бота
    application.run_polling()

if __name__ == '__main__':
    main()
```

### Описание кода

1. **Логирование ошибок**: Логирование ошибок настроено с использованием модуля `logging`. Все ошибки будут записываться в файл `bot_errors.log`.

2. **Обработчики команд**:
   - `/start`: Отправляет приветственное сообщение.
   - `/help`: Отправляет список доступных команд.

3. **Обработчик ошибок**: В случае возникновения ошибки, она будет залогирована, и бот автоматически перезапустится.

4. **Автоматический перезапуск**: В случае сбоя, бот перезапускается с помощью `os.execv`. Это позволяет боту автоматически восстановить работу после ошибки.

### Запуск бота

1. Замените `'YOUR_BOT_TOKEN'` на токен вашего бота, который вы получили от BotFather.
2. Запустите скрипт:

```bash
python your_bot_script.py
```

Теперь ваш бот будет работать, логировать ошибки и автоматически перезапускаться в случае сбоев.