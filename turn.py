from monster import Monster
from player import Player
from gamecondition import GameCondition
from curse import Curse


class Turn:
    def __init__(self, con: GameCondition, currentPlayer: Player):
        self.condition = con
        self.activePlayer = currentPlayer
        self.start_of_turn()

    def open_the_door(self):
        door = self.condition.get_door()

        return door

    def play_the_card(self, player: Player, card):
        for handCard in player.hand:
            if card == handCard.id:
                pass

    def play_door(self):
        pass

    def play_treasure(self):
        pass