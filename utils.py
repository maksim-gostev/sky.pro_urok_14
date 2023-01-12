import sqlite3


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








