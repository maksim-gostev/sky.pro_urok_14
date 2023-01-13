import json
import sqlite3


def search_by_name(title)-> str:
    """
    поиск фильма в базе данных по названию
    :param title: название фильма
    :return: отформатированные данные фильма
    """
    with sqlite3.connect("netflix.db") as con:
        cur = con.cursor()
        sqlite_query = ("SELECT title, country, release_year, listed_in, description "
                        "FROM netflix"
                        f" WHERE title LIKE '%{title}%' "
                        " ORDER BY date_added DESC "
                        )
        cur.execute(sqlite_query)
        result = cur.fetchone()

    result_dict = {
                   "title": result[0],
		           "country": result[1],
		           "release_year": result[2],
		           "genre": result[3],
		           "description": result[4]
                   }

    return result_dict


def search_by_range_of_release_years(year_1, year_2)-> str:
    """
    поиск по диапазону лет выпуска
    :param year_1: год начала диапазона
    :param year_2: год конца диапазона
    :return: отформатированные данные фильма
    """
    with sqlite3.connect("netflix.db") as con:
        cur = con.cursor()
        sqlite_query = ("SELECT title, release_year "
                        "FROM netflix "
                        f"WHERE release_year BETWEEN {year_1} AND {year_2} "
                        "LIMIT 100")
        cur.execute(sqlite_query)
        result = cur.fetchall()

    # список куда будут добовлятся словари
    result_list = []

    for res in result:
        result_dict = {
                       "title": res[0],
                       "release_year": res[1],
                      }
        result_list.append(result_dict)

    return result_list


def definition_of_the_rating(rating)-> str:
    """
    групировка рейтингов
    :param rating: определите группы
    :return: кортеж рейтингов
    """
    if rating == 'children':
        rating_tuplt = ('G', 'TV-G')
        print(type(rating_tuplt))

    elif rating == 'family':
        rating_tuplt = ('G', 'PG', 'PG-13', 'TV-PG')

    elif rating == 'adult':
        rating_tuplt = ('R', 'NC-17')

    result = search_by_rating(rating_tuplt)

    return result


def search_by_rating(rating)->tuple:
    """
    поиск по рейтингу
    :param rating: список рейтингов
    :return: отформатированные данные
    """
    with sqlite3.connect("netflix.db") as con:
        cur = con.cursor()
        sqlite_query = ("SELECT title, rating, description "
                        "FROM netflix "
                        "WHERE rating IN {}" .format(rating))
        cur.execute(sqlite_query)
        result = cur.fetchall()

    # список куда будут добовлятся словари
    result_list = []

    for res in result:
        result_dict = {
                       "title": res[0],
                       "rating": res[1],
                       "description": res[2]
                      }
        result_list.append(result_dict)

    return result_list


def search_by_genre(genre)-> str:
    """
    поиск фильмов по жанру
    :param genre: жанр
    :return: возвращает 10 самых свежих фильмов в формате json
    """
    with sqlite3.connect("netflix.db") as con:
        cur = con.cursor()
        sqlite_query = ("SELECT title, description "
                        "FROM netflix "
                        f"WHERE listed_in LIKE '%{genre}%' "
                        "ORDER BY date_added DESC "
                        "LIMIT 10")
        cur.execute(sqlite_query)
        result = cur.fetchall()

    # список куда будут добовлятся словари
    result_list = []
    for res in result:

        description = str(res[1])

        result_dict = {
            "title": res[0],
            "description": description.rstrip()
        }

        result_list.append(result_dict)

    return json.dumps(result_list, indent=4)
