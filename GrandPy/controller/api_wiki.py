import wikipedia


class MyWiki:
    """get from api wikipedia articles with one specific geolocation"""

    def __init__(self, lat, long):
        self.lat = lat
        self.long = long
        self.page_title = None
        self.url = None
        self.summary = None
        self.error = False

    def __get_page_title(self):
        """ find article from geocode"""
        wikipedia.set_lang("fr")
        self.page_title = wikipedia.geosearch(
            self.lat, self.long, title=None, results=1, radius=1000
        )[0]

    def __get_page_text(self):
        """ put elements from article in attributs"""
        link = wikipedia.page(self.page_title)

        self.summary = link.summary
        self.url = link.url

    def analyse_location(self):
        """ run all previous fonction """
        self.__get_page_title()
        self.__get_page_text()
