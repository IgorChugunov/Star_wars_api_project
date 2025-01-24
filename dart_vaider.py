import requests

"""Метод по созданию запроса get и выводу значения поля"""
def get_http_methods(url, field_name):
    result = requests.get(url) # Запрос get
    result_info = result.json()
    value = result_info.get(field_name) # получение значений из введённого поля
    return value

"""Получение url всех персонажей, что были в одном в фильме с Дартом Вейдером"""

characters_url_1 = set() # создание пустого множества для дальнейшего объединения множеств
darth_vader_films_urls = get_http_methods('https://swapi.dev/api/people/4/', 'films') # фильмы в которых есть Вейдер
for film_url in darth_vader_films_urls: # цикл по url фильмов
    characters_urls_2 = set(get_http_methods(film_url, 'characters')) # преобразование во множество списка url персонажей полученного из функции
    characters_urls_finaly = characters_urls_2 | characters_url_1 # объединение множеств для получения уникальных url
    characters_urls_1 = characters_urls_2 # присвоение первому множеству предыдущего для корректного объединения
characters_urls_finaly.remove('https://swapi.dev/api/people/4/') # удаление url Дарта Вейдера

"""Получение имён всех персонажей, что были в одном в фильме с Дартом Вейдером"""

list_names = sorted([get_http_methods(character_url, 'name') for character_url in characters_urls_finaly])
# создание списка всех персонажей, что были в одном в фильме с Дартом Вейдером отсортированного в алфавитном порядке
names = '\n'.join(list_names) # преобразования списка в строку, где каждое слово переходит в новую строку

"""Запись в файл полученных имён"""

with open('star_wars.txt', 'w', encoding='utf-8') as file_names: # создание файла для записи имён
    file_names.write(names) # запись имён
