import re
from GrandPy.constante import stop_word


class Parser:
    def __init__(self):
        self.initial_text = None
        self.ending_text = None

    def __get_text(self, texte):
        self.initial_text = str(texte)

    def __remove_special_caracters(self):
        self.initial_text = re.sub("[^A-Za-z0-9]+", " ", self.initial_text)

    def __check_size(self):
        self.initial_text = self.initial_text.lower()

    def __split_text(self):
        self.initial_text = self.initial_text.split()

    def __delete_text(self):

        killed_list = stop_word
        self.initial_text = [
            word for word in self.initial_text if word not in killed_list
        ]

    def __fusion_text(self):
        self.ending_text = " ".join(self.initial_text)

    def my_parser(self, initial_text):
        self.__get_text(initial_text)
        self.__remove_special_caracters()
        self.__check_size()
        self.__split_text()
        self.__delete_text()
        self.__fusion_text()
        return self.ending_text


test = Parser()
print(test.my_parser("hello, je souhaite aller à la tour eiffel ?"))