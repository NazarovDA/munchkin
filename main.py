from gamecondition import GameCondition
from treasure import Treasure
from curse import Curse
from card import Card
from player import *
from door import Door
from turn import Turn


from random import shuffle



class Game:
    def __init__(
            self,
            players: list[str], 
            card_packs: list[str] = ["M1"],
        ) -> None:
        doors, treasures = self.__create_decks(card_packs)
        self.gameCondition = GameCondition(
            players=[Player(player) for player in players],
            doors=doors,
            treasures=treasures,
            discardedDoors=list(),
            discardedTreasures=list()
        )
        self.currentPlayer: Player = self.gameCondition.players[0]
        self.action = None
        self.actionCard = None
        self.acrionPlayer = None
        for player in self.gameCondition.players:
            self.__give_cards_at_start_or_after_death(player)

    def append_action(self, action: str, cardIndex: str, player: str):
        """
        player - игрок, играющий карту
        cardIndex - номер карты, которую играет игрок

        Для завершения хода необходимо отправить "End of turn"
        Для того, чтоб сыграть карту необходимо отправить "Play the card", в случае, если данную карту сыграть невозможно, будет вызвано исключение
        """
        self.action = action
        self.actionCard = cardIndex
        self.acrionPlayer = player

    
    def run(self):
        turn = Turn(
            con=self.gameCondition,
            currentPlayer=self.currentPlayer
        )

        while self.action != "End of turn":
            if self.action == None:
                pass

            elif self.action == "Play the card":
                turn.play_the_card(
                    player=self.acrionPlayer,
                    card=self.actionCard
                )
                self.__reset_action()

    # !--------------
    # Подписки

    def on_state_change(self, callback: function) -> None:
        self.__on_state_change = callback


    # !--------------
    # Внутренние функции

    def __create_decks(self, packs: list[str]) -> None:
        doors: list[Door] = list()
        treasures: list[Treasure] = list()
        if "M1" in packs:
            from pack_v1 import __TREASURES__ as tr, __DOORS__ as dr
            doors.extend(dr)
            treasures.extend(tr)
            
        
        shuffle(doors)
        shuffle(treasures)

        return doors, treasures

    def __give_cards_at_start_or_after_death(self, player: Player):
        for i in range(4):
            self.gameCondition.add_card_to_hand(player, Door)
            self.gameCondition.add_card_to_hand(player)

    def __check_dead(self):
        for player in self.gameCondition.players:
            if player.isDead:
                self.__give_cards_at_start_or_after_death(player)

    def __reset_action(self):
        self.action = None
        self.actionCard = None
        self.acrionPlayer = None

    # !---------------
    # Функции ивентов

    def __lost_lvl(self, target, card):
        target.lost_level(value=card.value)
        return True

    def __drop_and_append_class(self, target):
        _ = target.lost_class()

        if isinstance(_, Class):
            self.discarded_doors.append(_)

        for card_from_deck in reversed(self.discarded_doors):
            if isinstance(card_from_deck, Class):
                target.append_class(card_from_deck)

    def __taxes(self, initial_player: Player):
        # TODO: figure out the whole algo
        pass

