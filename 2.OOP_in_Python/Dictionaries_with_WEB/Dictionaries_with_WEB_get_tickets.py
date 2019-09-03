# 1. Напишите функцию получения IATA-кода города из его названия, используя API Aviasales
# для усовершенствования приложения по парсингу информации об авиабилетах, созданного нами в ходе урока.
# Примечание: воспользуйтесь документацией по API, которая доступна на странице www.aviasales.ru/API
# (ссылка на значке «API-документация»). Вам необходимо изучить раздел «API для определения IATA-кода».

import requests
import json
import datetime


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

def get_tickets_info(origin, destination, depart_date, one_way, return_date_parameter):
    link = f"http://min-prices.aviasales.ru/calendar_preload?origin={origin}&destination={destination}&depart_date={depart_date}&one_way={one_way}{return_date_parameter}"
    return json.loads(requests.get(link).text)

separator('*')
iata_city = get_iatacode("Введите название города, чтобы получить его IATA-код: ")
print(f"IATA-код города {iata_city['city']}: {iata_city['iata']}")


#Определим лучший билет
separator('*')
print("Определим самый дешёвый авиабилет по вашим требованиям")
origin = get_iatacode("Введите название города - пункта отправления: ")['iata']
depart_date_my = datetime.datetime.strptime(input("Введите предполагаемую дату отправления в формате DD.MM.YYYY: "),"%d.%m.%Y")
depart_date = depart_date_my.strftime("%Y-%m-%d")
destination = get_iatacode("Введите название города - пункта назначения: ")['iata']
one_way = True if input("Билет только туда (введите 1) или туда и обратно (введите 2)?: ") == '1' else False
if one_way:
    return_date = depart_date
    return_date_parameter = ""
    tickets_data = get_tickets_info(origin, destination, depart_date, one_way, return_date_parameter)
    best_ticket = next(item for item in tickets_data['best_prices'] if item["depart_date"] == depart_date)

else:
    return_date_my = datetime.datetime.strptime(input("Введите предполагаемую дату возвращения в формате DD.MM.YYYY: "),"%d.%m.%Y")
    return_date = return_date_my.strftime("%Y-%m-%d")
    return_date_parameter = f"&return_date={return_date}"
    tickets_data = get_tickets_info(origin, destination, depart_date, one_way, return_date_parameter)
    best_ticket = next(item for item in tickets_data['current_depart_date_prices'] if item['depart_date'] == depart_date and item['return_date'] == return_date )

value = best_ticket['value']
aviacompany = best_ticket['gate']

print(f"Лучший авиабилет предлагает компания {aviacompany} по стоимости {value}")


