# 1. Напишите функцию получения IATA-кода города из его названия, используя API Aviasales
# для усовершенствования приложения по парсингу информации об авиабилетах, созданного нами в ходе урока.
# Примечание: воспользуйтесь документацией по API, которая доступна на странице www.aviasales.ru/API
# (ссылка на значке «API-документация»). Вам необходимо изучить раздел «API для определения IATA-кода».

import requests
import json


def separator(sign):
    print()
    print(sign*33)


def get_iatacode(text_message):
    while True:
        try:
            city = input(text_message)
            link = f'https://www.travelpayouts.com/widgets_suggest_params?q=Из%20{city}%20в%20Москва'
            iata_city = json.loads(requests.get(link).text)['origin']['iata']
            return {"iata": iata_city, "city": city}
        except:
            print("К сожалению, такой город не найден в базе Aviasales. Введите другой: ")


separator('*')
iata_city = get_iatacode("Введите название города, чтобы получить его IATA-код: ")
print(f"IATA-код города {iata_city['city']}: {iata_city['iata']}")


