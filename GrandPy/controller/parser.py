import re

from GrandPy.constante import stop_word


class Parser:
    """ from sentence get few words """

    def __init__(self):
        self.initial_text = None
        self.ending_text = None

    def __get_text(self, texte):
        """ from text entry  to class attibuts"""
        self.initial_text = str(texte)

    def __remove_special_caracters(self):
        """ remove special characters """
        valide_caracters = "[^A-Za-z0-9éèçîï]+"
        self.initial_text = re.sub(valide_caracters, " ", self.initial_text)

    def __check_size(self):
        """ check str size and def size=lower """
        self.initial_text = self.initial_text.lower()

    def __split_text(self):
        """ split text into words """
        self.initial_text = self.initial_text.split()

    def __delete_text(self):
        """ delete all commun words from stop_word_list """

        killed_list = stop_word
        self.initial_text = [
            word for word in self.initial_text if word not in killed_list
        ]

    def __fusion_text(self):
        """ join all words """
        self.ending_text = " ".join(self.initial_text)

    def my_parser(self, initial_text):
        """ run all previous fonction """
        self.__get_text(initial_text)

        if not self.initial_text or len(self.initial_text) == 0:
            raise ValueError("no text to parse :/")
        else:
            self.__remove_special_caracters()
            self.__check_size()
            self.__split_text()
            self.__delete_text()
            self.__fusion_text()
            return self.ending_text
