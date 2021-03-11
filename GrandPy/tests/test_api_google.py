from GrandPy.controller.api_google import MyGoogleMap
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


def test_google_is_ok(monkeypatch):
    class MockResponse:
        def __init__(self, key=None):
            self.key = key

        def geocode(self, *args, **kwargs):
            return geo_value

    monkeypatch.setattr(googlemaps, "Client", MockResponse)
    test = MyGoogleMap("antibes")
    test.get_geocode()
    expected_result = 43.58041799999999
    result = test.lat
    assert result == expected_result
