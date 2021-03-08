from flask import Flask, render_template, request, jsonify
from GrandPy.controller.parser import Parser
from GrandPy.controller.api_wiki import MyWiki
from GrandPy.controller.api_google import MyGoogleMap

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/process", methods=["POST"])
def process():

    name = request.form["my_text"]

    if name:
        newName = name[::-1]

        return jsonify({"name": newName})

    return jsonify({"error": "Missing data!"})


if __name__ == "__main__":
    app.run(debug=True)
