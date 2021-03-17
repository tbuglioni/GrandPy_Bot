from GrandPy.controller.process_post import ProcessPost
from GrandPy.views import app
from flask import json
import wikipedia
import googlemaps

geo_value = [
    {
        "address_components": [
            {
                "long_name": "Antibes",
                "short_name": "Antibes",
                "types": ["locality", "political"],
            },
            {
                "long_name": "Alpes-Maritimes",
                "short_name": "Alpes-Maritimes",
                "types": ["administrative_area_level_2", "political"],
            },
            {
                "long_name": "Provence-Alpes-Côte d'Azur",
                "short_name": "Provence-Alpes-Côte d'Azur",
                "types": ["administrative_area_level_1", "political"],
            },
            {
                "long_name": "France",
                "short_name": "FR",
                "types": ["country", "political"],
            },
        ],
        "formatted_address": "Antibes, France",
        "geometry": {
            "bounds": {
                "northeast": {"lat": 43.6227, "lng": 7.145126899999999},
                "southwest": {"lat": 43.541863, "lng": 7.0645681},
            },
            "location": {"lat": 43.58041799999999, "lng": 7.125102},
            "location_type": "APPROXIMATE",
            "viewport": {
                "northeast": {"lat": 43.6227, "lng": 7.145126899999999},
                "southwest": {"lat": 43.541863, "lng": 7.0645681},
            },
        },
        "place_id": "ChIJqZFankXVzRIRsJ-X_aUZCAQ",
        "types": ["locality", "political"],
    }
]


def test_processing_views(monkeypatch):
    # gmap
    class MockResponse:
        def __init__(self, key=None):
            self.key = key

        def geocode(self, *args, **kwargs):
            return geo_value

    monkeypatch.setattr(googlemaps, "Client", MockResponse)

    # wikipedia
    def mock_set_langue(*args, **kwargs):
        pass

    def mock_geosearch(*args, **kwargs):
        return "Gare d'Antibes"

    class MockResponse(object):
        def __init__(self):
            self.summary = None
            self.url = "https://fr.wikipedia.org/wiki/Gare_d%27Antibes"

    def mock_pager(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr(wikipedia, "set_lang", mock_set_langue)
    monkeypatch.setattr(wikipedia, "geosearch", mock_geosearch)
    monkeypatch.setattr(wikipedia, "page", mock_pager)

    # run in flask context
    with app.app_context():
        test = ProcessPost("antibes")
        result = test.processing()
        data = json.loads(result.get_data(as_text=True))
        expected_result = 200
        assert result.status_code == expected_result
        assert data["lat"] == 43.58041799999999
