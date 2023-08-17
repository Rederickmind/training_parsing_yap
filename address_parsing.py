# Импортируйте модуль для работы с регулярными выражениями.
import re

addresses = [
    ('Он проживал в городе Иваново на улице Наумова. '
     'Номер дома 125 был зеркальной копией его номера квартиры 521'),
    'Адрес: город Новосибирск, улица Фрунзе, дом 321, квартира 15.'
]

for address in addresses:
    # Напишите регулярное выражение.
    pattern = r'город.? (?P<city>\w+).*улиц.? (?P<street>\w+).* дом.? (?P<house>\d+).* квартир.? (?P<flat>.\d+)'
    # Примените метод регулярных выражений, который
    # найдёт шаблон pattern в строке address.
    address_match = re.search(pattern, address)

    # Распечатайте названия городов и улиц, номера домов и квартир
    # из обеих строк.
    if address_match:
        print(
            address_match.group('city'),
            address_match.group('street'),
            address_match.group('house'),
            address_match.group('flat')
        )
