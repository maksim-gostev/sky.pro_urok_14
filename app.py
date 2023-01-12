from flask import Flask, jsonify
import utils

app = Flask(__name__)


@app.route("/movie/<title>")
def get_movie(title):
    result = utils.search_by_name(title)
    return jsonify(result)

@app.route("/movie/<year_1>/to/<year_2>")
def get_by_year(year_1, year_2):
    result = utils.search_by_range_of_release_years(year_1, year_2)
    return jsonify(result)



if __name__ == '__main__':
    app.run()