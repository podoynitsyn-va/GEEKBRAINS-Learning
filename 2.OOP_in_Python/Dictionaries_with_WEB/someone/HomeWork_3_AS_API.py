import requests
import re
import json

def IATA_City_cod_by_name():

    org_IATA= ''
    dst_IATA= ''
    one_way = None
    city_IATA = {}
    flag = True
    while flag :
        origin = input('Введите город отправления  : ')
        destination = input('Введите город прибытия     : ')
        one_way = input ('Туда и обратно? y/any key  ')
        if one_way == 'y' or one_way == 'Y' or one_way == 'У' or one_way == 'у':
            one_way = False
            symb = '<->'
        else:
            one_way= True
            symb = '->'
        link_IATA_city_id = 'https://www.travelpayouts.com/widgets_suggest_params?q=Из%20'+origin+'%20в%20'+destination
        req_txt = requests.get(link_IATA_city_id).text
        city_IATA = json.loads(req_txt)
        #print(city_IATA)
        if city_IATA == {} :
            print('Город отправления или назначения введен не верно. Повторите ввод.')
        else:
            flag = False
            org_IATA  = city_IATA['origin']['iata']
            dst_IATA = city_IATA['destination']['iata']
            print(f'From org {org_IATA} to dst {dst_IATA}    {symb}')
    return  org_IATA, dst_IATA, one_way

org_IATA, dst_IATA, one_way = IATA_City_cod_by_name()

one_way_str = str(one_way)
#print(one_way)

link = 'http://min-prices.aviasales.ru/calendar_preload?&one_way='+one_way_str+'&origin='+org_IATA+'&destination='+dst_IATA
data= json.loads(requests.get(link).text)

#print(data)
#print(bprice_dict)
if one_way == True :
    print(f'Лучшая цена  {data["best_prices"][0]["value"]} дата вылета {data["best_prices"][0]["depart_date"]}')
else:
    print(f'Лучшая цена  {data["best_prices"][0]["value"]} дата вылета {data["best_prices"][0]["depart_date"]} дата возвращения {data["best_prices"][0]["return_date"]}')
