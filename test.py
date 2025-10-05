# Убедитесь, что у вас установлен python-dotenv:
# pip install python-dotenv

from dotenv import load_dotenv
import os

# Загружаем переменные из файла .env
load_dotenv()

# Получаем значение переменной API_KEY
api_key = os.getenv("API_KEY")

# Выводим ключ (в реальном проекте так делать не стоит из соображений безопасности!)
print("API Key:", api_key)