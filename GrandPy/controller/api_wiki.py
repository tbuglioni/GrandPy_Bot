import wikipedia


class MyWiki:
    def __init__(self, lat, long):
        self.lat = lat
        self.long = long
        self.page_title = None
        self.url = None
        self.summary = None
        self.error = False

    def __get_page_title(self):
        wikipedia.set_lang("fr")
        self.page_title = wikipedia.geosearch(
            self.lat, self.long, title=None, results=1, radius=1000
        )[0]
        # print(self.page_title) #Gare d'Antibes

    def __get_page_text(self):
        link = wikipedia.page(self.page_title)
        self.summary = link.summary
        self.url = link.url

    def analyse_location(self):
        self.__get_page_title()
        self.__get_page_text()
