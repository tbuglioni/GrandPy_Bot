from flask import Flask, render_template, request, jsonify
from GrandPy.controller.parser import Parser
from GrandPy.controller.api_wiki import MyWiki
from GrandPy.controller.api_google import MyGoogleMap
import dotenv
import os

dotenv.load_dotenv()

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/process", methods=["POST"])
def process():

    entry_text = request.form["my_text"]

    if entry_text:
        gg_key = os.getenv("API_GOOGLE_KEY")

        # Parser:
        my_parser = Parser()
        parsed_text = my_parser.my_parser(entry_text)
        # ggmap:
        my_google_map = MyGoogleMap(parsed_text)
        my_google_map.get_geocode()
        # wiki:
        my_wiki = MyWiki(my_google_map.lat, my_google_map.lng)
        my_wiki.analyse_location()

        return jsonify(
            {
                "google_key": gg_key,
                "lat": my_google_map.lat,
                "lng": my_google_map.lng,
                "formated_location": my_google_map.formatted_address,
                "wiki_summary": my_wiki.summary,
                "wiki_link": my_wiki.url,
            }
        )

    return jsonify({"error": "Missing data!"})


if __name__ == "__main__":
    app.run(debug=True)
