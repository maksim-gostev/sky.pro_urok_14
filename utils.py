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

print(search_by_name(100))






