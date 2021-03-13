import os
import wikipedia
import googlemaps
import dotenv
from flask import request, jsonify
from GrandPy.controller.parser import Parser
from GrandPy.controller.api_wiki import MyWiki
from GrandPy.controller.api_google import MyGoogleMap

dotenv.load_dotenv()


class ProcessPost:
    def __init__(self):
        pass

    def processing(self):
        entry_text = request.form["my_text"]

        if entry_text:
            gg_key = os.getenv("API_GOOGLE_KEY")

            # Parser:
            try:
                my_parser = Parser()
                parsed_text = my_parser.my_parser(entry_text)
                if not parsed_text:
                    return jsonify({"error": "Hein ? tu peux repeter ?"})
            except:
                return jsonify({"error": "Hein ? tu peux repeter ?"})

            try:
                # ggmap:
                my_google_map = MyGoogleMap(parsed_text)
                my_google_map.get_geocode()
                # wiki:
                my_wiki = MyWiki(my_google_map.lat, my_google_map.lng)
                my_wiki.analyse_location()

            except (
                IndexError,
                googlemaps.exceptions.ApiError,
                googlemaps.exceptions.HTTPError,
                googlemaps.exceptions.Timeout,
                googlemaps.exceptions.TransportError,
                wikipedia.exceptions.DisambiguationError,
                wikipedia.exceptions.HTTPTimeoutError,
                wikipedia.exceptions.PageError,
                wikipedia.exceptions.RedirectError,
                wikipedia.exceptions.WikipediaException,
            ):
                return jsonify({"error": "Désolé mais je ne m'en souviens plus"})

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

        return jsonify({"error": "Hein ? tu peux repeter ?"})
