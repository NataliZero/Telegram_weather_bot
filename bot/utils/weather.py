import requests
from bs4 import BeautifulSoup

def get_weather():
    url = "https://www.gismeteo.ru/weather-sankt-peterburg-4079/"  # URL страницы с погодой
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")

        # Получаем температуру из элемента <span> с классом "temperature-value"
        temperature_tag = soup.find("span", class_="temperature-value")
        if temperature_tag:
            temperature = temperature_tag.text.strip()
        else:
            temperature = "Температура не найдена"

        # Получаем состояние погоды (например, описание) — это нужно искать по подходящему тегу
        # Пример поиска для описания состояния погоды, скорее всего, нужно будет уточнить:
        condition_tag = soup.find("div", class_="widget-now")  # Поищите класс для описания погоды
        condition = condition_tag.text.strip() if condition_tag else "Состояние погоды не найдено"

        result = f"Температура: {temperature}, Погода: {condition}"
        print(result)  # Выводим результат в консоль
        return result
    else:
        return "Не удалось получить данные о погоде."
