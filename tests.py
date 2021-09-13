from main import Game
import unittest

list_of_players = ["Player1", "Player2", "Player3"]

global game

class TestGame(unittest.TestCase):
    def test_game_creating(self):
        global game
        game = Game(card_packs=["M1"], players=list_of_players)

    def test_players(self):
        global game
        players = [player.name for player in game.players]
        self.assertListEqual(players, list_of_players)
    
    def test_info(self):
        global game
        data = [player.get_info() for player in game.players]
        print(data)

if __name__ == "__main__":
    unittest.main()