import os
import wikipedia
import googlemaps
import dotenv
from flask import jsonify
from GrandPy.controller.parser import Parser
from GrandPy.controller.api_wiki import MyWiki
from GrandPy.controller.api_google import MyGoogleMap
from GrandPy.controller.random_text import RandomText

dotenv.load_dotenv()


class ProcessPost:
    """get words, parse them,
    find geolocation,
    find articles in wikipedia from geolocation"""

    def __init__(self, entry_text):
        self.entry_text = entry_text
        self.parsed_text = None
        self.gg_key = os.getenv("API_GOOGLE_KEY")
        self.lat = None
        self.lng = None
        self.formated_location = None
        self.wiki_summary = None
        self.wiki_link = None
        self.random_text = None

    def __process_parser(self):
        """ get words, split them and delete commun words """
        try:
            my_parser = Parser()
            self.parsed_text = my_parser.my_parser(self.entry_text)
            if not self.parsed_text:
                raise ValueError("trouble with parser")
        except ValueError:

            raise ValueError("trouble with parser")

    def __process_gmap(self):
        """ get gelocations from couple of words"""
        try:
            my_google_map = MyGoogleMap(self.parsed_text)
            my_google_map.get_geocode()
            self.lat = my_google_map.lat
            self.lng = my_google_map.lng
            self.formated_location = my_google_map.formatted_address

        except (
            IndexError,
            googlemaps.exceptions.ApiError,
            googlemaps.exceptions.HTTPError,
            googlemaps.exceptions.Timeout,
            googlemaps.exceptions.TransportError,
        ):
            raise ValueError("trouble with gmap")

    def __process_wiki(self):
        """ get wikipedia article from geolocation"""
        try:
            my_wiki = MyWiki(self.lat, self.lng)
            my_wiki.analyse_location()
            self.wiki_summary = my_wiki.summary
            self.wiki_link = my_wiki.url
        except (
            IndexError,
            wikipedia.exceptions.DisambiguationError,
            wikipedia.exceptions.HTTPTimeoutError,
            wikipedia.exceptions.PageError,
            wikipedia.exceptions.RedirectError,
            wikipedia.exceptions.WikipediaException,
        ):
            raise ValueError("trouble with wikipedia")

    def __process_random_text(self):
        """ return random intro text """
        my_random_text = RandomText()
        self.random_text = my_random_text.return_random()

    def processing(self):
        """ performe previous fonctions together"""

        if self.entry_text:
            try:
                self.__process_parser()
                self.__process_gmap()
                self.__process_wiki()
                self.__process_random_text()
            except ValueError:
                return jsonify(
                    {
                        "error": "Désolé mais je suis perdu... "
                        "soit je n'ai pas compris "
                        "soit je ne m'en souviens plus..."
                    }
                )

            return jsonify(
                {
                    "google_key": self.gg_key,
                    "lat": self.lat,
                    "lng": self.lng,
                    "formated_location": self.formated_location,
                    "wiki_summary": self.wiki_summary,
                    "wiki_link": self.wiki_link,
                    "random_text": self.random_text,
                }
            )

        return jsonify({"error": "Hein ? tu peux repeter ?"})
