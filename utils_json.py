import sqlite3
import json


def get_list_cast(actor_1, actor_2) -> str:
    """
    поиск актёров кто играет с ними в паре больше 2 раз
    :param actor_1: имя первого актёра
    :param actor_2:имя второго актёра
    :return: список акрёров
    """
    with sqlite3.connect("netflix.db") as con:
        cur = con.cursor()
        sqlite_query = ("SELECT netflix.cast "
                        "FROM netflix "
                        f"WHERE netflix.cast LIKE '%{actor_1}%' "
                        f"AND netflix.cast LIKE '%{actor_2}%' "
                        "GROUP BY netflix.cast")
        cur.execute(sqlite_query)
        result = cur.fetchall()

    # список куда будут добавлены все акрёры
    cast_list = []
    # цикл добовления всех актёров из колонки cast
    for res in result:
        list_res = list(res)
        for item in list_res:
            cast_list += item.split(', ')

    # список куда будут добовлятся которые играют с ними в паре больше 2 раз
    cast_result = []
    # цикл проверки и добовления
    for i in range(len(cast_list)):
        if cast_list.count(cast_list[i]) > 2:
            cast_result.append(cast_list[i])
    unique_cast = set(cast_result)
    unique_cast.discard(actor_1)
    unique_cast.discard(actor_2)
    return list(unique_cast)


#print(get_list_cast('Rose McIver', 'Ben Lamb'))


def search_parameters():
    """
    функция получения типа картины
    года выпуска и ее жанра
    :return: данныё картин в формате json
    """
    # цикл выбора типа картины
    while True:
        type_movie = input('Что вы хотите найти, фильм или сериал?\n'
                           'Если фильм то нажмите "1", если сериал "2"\n')
        if type_movie == '1':
            type_ = 'Movie'
            break
        elif type_movie == '2':
            type_ = 'TV Show'
            break
    # цикл ввода года выпуска
    while True:
        release = input('Введите год выпуска\n')
        if release.isnumeric():
            break
    #жанр картины
    genre = input('Введите жанр\n')
    # отформатированные данные картин
    json_data_movie = get_data_movie(type_, release, genre)
    return json_data_movie


def get_data_movie(type_, release, genre) -> str:
    """
    функция поиска картин по типу, году выпуска и жанру
    :param type_: тип картины
    :param release: год выпуска
    :param genre: жанр
    :return: данные картин
    """
    with sqlite3.connect("netflix.db") as con:
        cur = con.cursor()
        sqlite_query = ("SELECT title, description "
                        "FROM netflix "
                        f"WHERE type = '{type_}' "
                        f"AND release_year = '{release}' "
                        f"AND listed_in LIKE '%{genre}%' "
                        f"LIMIT 1")

        cur.execute(sqlite_query)
        result = cur.fetchall()
    # отформатированные данные картин
    result_json = format_json(result)
    return result_json


def format_json(data)-> list[tuple]:
    """
    функция форматирования данных
    :param data: список кортежей
    :return: отформатированныё данныё
    """
    # список словарей
    data_list = []
    # цикл добовления словарей данных в список
    for item in data:
        description = str(item[1])
        data_dict = {'title': item[0],
                     'description': description.rstrip()}
        data_list.append(data_dict)

    return json.dumps(data_list, indent=4)


#search_parameters()