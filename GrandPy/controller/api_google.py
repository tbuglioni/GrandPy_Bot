import googlemaps
import dotenv
import os

dotenv.load_dotenv()


class MyGoogleMap:
    """get from api googlemap geolocation and
    formatted address from words (ex: paris)"""

    def __init__(self, place_to_find):
        self.place_to_find = place_to_find
        self.lat = None
        self.lng = None
        self.formatted_address = None

    def get_geocode(self):
        """ get elements from api and put them in class attributs"""

        gmaps = googlemaps.Client(key=(os.getenv("API_GOOGLE_KEY")))

        geocode_result = gmaps.geocode(self.place_to_find)
        self.lat = geocode_result[0]["geometry"]["location"]["lat"]
        self.lng = geocode_result[0]["geometry"]["location"]["lng"]
        self.formatted_address = geocode_result[0]["formatted_address"]
