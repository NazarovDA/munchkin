from door import Door
from player import Player
from card import Card
from treasure import Treasure
import typing


class GameCondition:
    def __init__(
            self,
            players: list[Player],
            doors: list[Door],
            treasures: list[Treasure],
            discardedDoors: list[Door],
            discardedTreasures: list[Treasure]
        ):
        self.players = players
        self.doors = doors
        self.treasures = treasures
        self.discardedDoors = discardedDoors
        self.discardedTreasures = discardedTreasures
        self.cardsOnTable: list[Card] = list()
    
    def add_card_to_hand(self, player: Player, type: str = "Treasure"):
        """
        Expected type is Door or Treasure. Write Door if Door is needed, Treasure is default value
        """
        playerIndex = self.players.index(player)
        self.players[playerIndex].append_card_to_hand(self.doors.pop() if type == "Door" else self.treasures.pop())
        return self

    def get_door(self):
        returningDoor = self.doors.pop()

        if self.doors.__len__ == 0: self.__update_doors_deck()

        return (returningDoor, self)

    def get_treasure(self):
        returningTreasure = self.doors.pop()

        if self.treasures.__len__ == 0: self.__update_treasure_deck()

        return (returningTreasure, self)

    def discard_treasure(self, treasure:Treasure):
        self.discardedTreasures.append(treasure)
        return self

    def discard_door(self, door: Door):
        self.discardedDoors.append(door)
        return self

    def discard_table(self):
        for card in self.cardsOnTable:
            if isinstance(card, Treasure):
                self.discardedTreasures.append(card)
            elif isinstance(card, Door):
                self.discardedDoors.append(card)

        self.cardsOnTable.clear()
        return self

    def __update_doors_deck(self):
        """
        Внутренний метод, вызывается только если кончились карты в колоде дверей
        """
        self.doors = self.discardedDoors
        self.discardedDoors = []

    def __update_treasure_deck(self):
        """
        Внутренний метод, вызывается только если кончились карты в колоде сокровищ
        """
        self.treasures = self.discardedTreasures
        self.discardedTreasures = []

    def player_leave(self, player: Player):
        self.players.remove(player)
        return self