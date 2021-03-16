import random


class RandomText:
    """ return random text """

    def __init__(self):
        self.text_list = [
            "Oula quel endroit ! Ca a bien changé depuis. ",
            "j'ai rencontré GrandMa à 5 minutes de là. ",
            "J'ai toujours aimé marcher pas loins de là. ",
            "J'aime bien ce coins. ",
            "AH oui! je m'en souviens. ",
            "Il était une fois : ",
            "j'avais un ami dans le coins, un chic type ! Louis.",
            "Le temps passe vite ... je reconnais plus cet endroit",
            "Je te conseille vraiment d'aller voir ce coins",
            "Trop facile. ",
            "ah ca je connais bien !",
            "j'ai lu un truc sur ce coins une fois :",
            "bouge pas je vais tapper sur wikipedia ce coins",
        ]

    def return_random(self):
        """ return random text """
        return random.choice(self.text_list)
