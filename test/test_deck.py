import unittest
from src.deck import Deck


class DeckTestCase(unittest.TestCase):

    def setUp(self):  # this method will be run before each test
        self.deck = Deck()

    def tearDown(self):  # this method will be run after each tests
        pass

    def test_number_of_cards(self):  # any method beginning with 'test' will be run by unittest
        number_of_cards = len(self.deck.cards)
        self.assertEqual(number_of_cards, 52)

    def test_values_on_cards(self):
        for card in self.deck.cards:
            self.assertTrue(card.rank in ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"])
            self.assertTrue(card.suit in ["Hearts", "Diamonds", "Spades", "Clubs"])

    def test_draw_card(self):
        number_of_cards = len(self.deck.cards)
        newCard = self.deck.draw()
        self.assertEqual(len(self.deck.cards), number_of_cards - 1)
        self.assertEqual(newCard in self.deck.cards, False)


if __name__ == '__main__':
    unittest.main()
