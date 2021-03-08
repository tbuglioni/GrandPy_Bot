from GrandPy.controller.api_wiki import MyWiki
import wikipedia

# set of data :
# (43.5836, 7.10905) "Gare d'Antibes" "https://fr.wikipedia.org/wiki/Gare_d%27Antibes"
# (48.85837009999999, 2.2944813) "https://fr.wikipedia.org/wiki/Tour_Eiffel"


def test_wiki_is_ok(monkeypatch):
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
    test = MyWiki(43.5836, 7.10905)
    test.analyse_location()
    expected_result = "https://fr.wikipedia.org/wiki/Gare_d%27Antibes"
    result = test.url
    assert result == expected_result
