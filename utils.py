import sqlite3
import pprint


def search_by_name(title):
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

def search_by_range_of_release_years(year_1, year_2):
    with sqlite3.connect("netflix.db") as con:
        cur = con.cursor()
        sqlite_query = ("SELECT title, release_year "
                        "FROM netflix "
                        f"WHERE release_year BETWEEN {year_1} AND {year_2} "
                        "LIMIT 100")
        cur.execute(sqlite_query)
        result = cur.fetchall()
    result_list = []
    for res in result:
        result_dict = {
                       "title": res[0],
                       "release_year": res[1],
                      }
        result_list.append(result_dict)
    return result_list

def definition_of_the_rating(rating):
    if rating == 'children':
        rating_tuplt = ('G', 'TV-G')
        print(type(rating_tuplt))
    elif rating == 'family':
        rating_tuplt = ('G', 'PG', 'PG-13', 'TV-PG')
    elif rating == 'adult':
        rating_tuplt = ('R', 'NC-17')

    result = search_by_rating(rating_tuplt)
    return result
def search_by_rating(rating):

    with sqlite3.connect("netflix.db") as con:
        cur = con.cursor()
        sqlite_query = ("SELECT title, rating, description "
                        "FROM netflix "
                        "WHERE rating IN {}" .format(rating))
        cur.execute(sqlite_query)
        result = cur.fetchall()
    result_list = []
    for res in result:
        result_dict = {
                       "title": res[0],
                       "rating": res[1],
                       "description": res[2]
                      }
        result_list.append(result_dict)
    return result_list

def search_by_genre(genre):
    with sqlite3.connect("netflix.db") as con:
        cur = con.cursor()
        sqlite_query = ("SELECT title, description "
                        "FROM netflix "
                        f"WHERE listed_in LIKE '%{genre}%' "
                        "ORDER BY date_added DESC "
                        "LIMIT 10")
        cur.execute(sqlite_query)
        result = cur.fetchall()
    result_list = []
    for res in result:
        result_dict = {
            "title": res[0],
            "description": res[1]
        }
        result_list.append(result_dict)
    return result_list



pprint.pprint(search_by_genre('International TV Shows'))






