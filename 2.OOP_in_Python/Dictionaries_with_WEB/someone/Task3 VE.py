import requests, json

print("\nПоиск билета в один конец с минимальной ценой")
print("\nВведите полное название городов на русском языке")
origin = input("Введите город отправления: ")
destination = input("Введите город назначения: ")
IATA = f"https://www.travelpayouts.com/widgets_suggest_params?q=Из%20{origin}%20в%20{destination}"
try:
    data = json.loads(requests.get(IATA).text) #
    origin = data["origin"]
    destination = data["destination"]
    link = "http://min-prices.aviasales.ru/calendar_preload?one_way=true&origin={}&destination={}".format(origin["iata"],destination["iata"])
    data = json.loads(requests.get(link).text)
    data = data["best_prices"][0]
except:
    print("Проверьте правильность ввода названий городов")
else:
    print("\nБИЛЕТ", '-' * 50)
    print("Рейс: {} — {}".format(origin["name"],destination["name"]))
    print("Стоимость билета: {} руб".format(int(data["value"])))
    print("Дата отправления: {}".format(data["depart_date"]))
    print("Количество пересадок: {}".format(int(data["number_of_changes"])))