# Тема 3. Словари. Применение объектов в работе в вебом

# ======================================================================================================================
#  Напишите функцию получения IATA-кода города из его названия, используя API Aviasales для усовершенствования
# приложения по парсингу информации об авиабилетах, созданного нами в ходе урока.
# Примечание: воспользуйтесь документацией по API, которая доступна на странице www.aviasales.ru/API
# (ссылка на значке «API-документация»). Вам необходимо изучить раздел «API для определения IATA-кода».

from requests import get
from json import loads


def get_iata(city):
    link = f'https://www.travelpayouts.com/widgets_suggest_params?q=Из%20{city}%20в%20{city}'
    resp = get(link).text
    data = loads(resp)
    try:
        return data['origin']['iata']
    except:
        not_found = 'IATA код не найден. Проверьте правильность ввода'
        return not_found


city = input('Ведите название города на русском языке: ')
print('IATA код:', get_iata(city))
