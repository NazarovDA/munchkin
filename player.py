from card import Card
from race import Race
from classes import Class

class Player:
    def __init__(self, name):
        self.name = name

        self.__LEVEL: int = 1

        self.__RACE: Race = None

        self.__CLASS: Class = None
        self.__isAdditionalClassEnabled = False
        self.__ADDITIONAL_CLASS: Class = None
        self.hand: list[Card] = list()
        self.isDead = False

    def lost_level(self, value):
        if value > self.__LEVEL:
            pass
    
    def get_class(self): return self.__CLASS

    def lost_class(self):
        returned_shit = self.__CLASS
        self.__CLASS = None
        return returned_shit
    
    def append_class(self, newClass: Class, number_of_class: int = 1):
        if self.__CLASS == None:
            self.__CLASS = newClass

        elif self.__isAdditionalClassEnabled and self.__ADDITIONAL_CLASS is None:
            self.__ADDITIONAL_CLASS = newClass

    def get_info(self) -> dict:
        info = {
            "name": self.name,
            "class": self.__CLASS,
            "level": self.__RACE,
            "isAdditionalClassEnabled": self.__isAdditionalClassEnabled,
            "secondClass": self.__ADDITIONAL_CLASS
        }
        return info

    def append_card_to_hand(self, card:Card) -> None:
        self.hand.append(card)

    def DIE(self):
        if self.isDead:
            self.__LEVEL: int = 1

            self.__RACE: Race = None

            self.__CLASS: Class = None
            self.__isAdditionalClassEnabled = False
            self.__ADDITIONAL_CLASS: Class = None
            self.hand: list[Card] = list()
            self.isDead = False
