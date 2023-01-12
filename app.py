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

@app.route("/rating/children")
def get_by_rating_children():
    result = utils.definition_of_the_rating('children')
    return jsonify(result)


@app.route("/rating/family")
def get_by_rating_family():
    result = utils.definition_of_the_rating('family')
    return jsonify(result)


@app.route("/rating/adult")
def get_by_rating_adult():
    result = utils.definition_of_the_rating('adult')
    return jsonify(result)

@app.route("/genre/<genre>")
def get_by_genre(genre):
    result = utils.search_by_genre(genre)
    return jsonify(result)


if __name__ == '__main__':
    app.run()