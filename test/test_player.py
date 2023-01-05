import unittest
from src.logic.player import Player
from src.logic.deck import Deck

class PlayerTestCase(unittest.TestCase):
    def setUp(self):  # this method will be run before each test
        self.deck = Deck()

    def tearDown(self):  # this method will be run after each tests
        pass

    def test_new_player_has_2_cards(self):
        player = Player("Test", self.deck)
        self.assertEqual(len(player.cards), 2)

    def test_new_player_not_bust(self):
        player = Player("Test", self.deck)
        self.assertEqual(player.bust, False)

    def test_player_hit(self):
        player = Player("Test", self.deck)
        originalScore = player.score
        originalDeckSize = len(player.cards)
        player.hit()
        self.assertEqual(len(player.cards), originalDeckSize + 1)
        self.assertNotEqual(player.score, originalScore)

    def test_player_stand(self):
        player = Player("Test", self.deck)
        originalScore = player.score
        originalDeckSize = len(player.cards)
        player.stand()
        self.assertEqual(len(player.cards), originalDeckSize)
        self.assertEqual(player.score, originalScore)
        