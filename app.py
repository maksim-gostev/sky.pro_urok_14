from flask import Flask, jsonify
import utils

app = Flask(__name__)


@app.route("/movie/<title>")
def get_movie(title):
    result = utils.search_by_name(title)
    return jsonify(result)



if __name__ == '__main__':
    app.run()