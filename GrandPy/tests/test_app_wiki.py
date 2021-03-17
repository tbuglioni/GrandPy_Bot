from GrandPy.controller.api_wiki import MyWiki
import wikipedia


def test_wiki_is_ok(monkeypatch):
    def init_mock():
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

    init_mock()
    test = MyWiki(43.6227, 7.145126899999999)
    test.analyse_location()
    expected_result = "https://fr.wikipedia.org/wiki/Gare_d%27Antibes"
    result = test.url
    assert result == expected_result
