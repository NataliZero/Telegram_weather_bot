import requests

API_KEY = "cb81feb613e66e7f352fd2fc8db991cd"  # Ваш API-ключ
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city="Санкт-Петербург"):
    """
    Получение данных о погоде для указанного города.
    """
    try:
        # Формируем запрос
        url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric&lang=ru"
        response = requests.get(url)
        data = response.json()

        # Проверяем статус ответа
        if response.status_code == 200:
            temperature = data["main"]["temp"]
            weather_description = data["weather"][0]["description"]
            return f"Погода в {city}:\nТемпература: {temperature}°C\nОписание: {weather_description.capitalize()}"
        else:
            return f"Ошибка: {data.get('message', 'Не удалось получить данные о погоде.')}"
    except Exception as e:
        return f"Произошла ошибка: {e}"
