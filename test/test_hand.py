import unittest
from src.deck import Deck
from src.hand import Hand
from src.card import Card

class HandTestCase(unittest.TestCase):
    def setUp(self):  # this method will be run before each test
        self.deck = Deck()
        self.hand = Hand(self.deck)

    def tearDown(self):  # this method will be run after each tests
        pass

    def test_number_of_cards_start(self):
        number_of_cards = len(self.hand.cards)
        self.assertEqual(number_of_cards, 2)

    def test_score_hand_1(self):
        testHand = Hand(self.deck)
        testHand.cards = [Card("Hearts", "K"), Card("Hearts", "A")]
        self.assertEqual(testHand.getBestTotal(), 21)

    def test_score_hand_2(self):
        testHand = Hand(self.deck)
        testHand.cards = [Card("Hearts", "K"), Card("Hearts", "Q"), Card("Hearts", "A")]
        self.assertEqual(testHand.getBestTotal(), 21)

    def test_score_hand_3(self):
        testHand = Hand(self.deck)
        testHand.cards = [Card("Hearts", "9"), Card("Hearts", "A"), Card("Hearts", "A")]
        self.assertEqual(testHand.getBestTotal(), 21)


if __name__ == '__main__':
    unittest.main()
