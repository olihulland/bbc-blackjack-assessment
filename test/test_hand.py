import unittest
from src.logic.deck import Deck
from src.logic.hand import Hand
from src.logic.card import Card

class HandTestCase(unittest.TestCase):
    def setUp(self):  # this method will be run before each test
        pass

    def tearDown(self):  # this method will be run after each tests
        pass

    def test_valid_then_hit(self):
        hand = Hand([Card("Spades", "10"), Card("Clubs", "10")])
        self.assertEqual(hand.bust, False)
        originalScore = hand.score
        hand.addCard(Card("Diamonds", "10"))
        self.assertEqual(hand.score, originalScore + 10)

    def test_valid_21_under(self):
        hand = Hand([Card("Spades", "10"), Card("Clubs", "10")])
        self.assertEqual(hand.bust, False)  # 20 is not bust
        hand.addCard(Card("Diamonds", "A"))
        self.assertEqual(hand.bust, False)  # 21 is not bust

    def test_bust_22_over(self):
        hand = Hand([Card("Spades", "10"), Card("Clubs", "10")])
        hand.addCard(Card("Diamonds", "2"))
        self.assertEqual(hand.bust, True)  # 22 is bust

    def test_score_hand_1(self):
        cards = [Card("Hearts", "K"), Card("Hearts", "A")]
        self.assertEqual(Hand.getBestTotal(cards), 21)

    def test_score_hand_2(self):
        cards = [Card("Hearts", "K"), Card("Hearts", "Q"), Card("Hearts", "A")]
        self.assertEqual(Hand.getBestTotal(cards), 21)

    def test_score_hand_3(self):
        cards = [Card("Hearts", "9"), Card("Hearts", "A"), Card("Hearts", "A")]
        self.assertEqual(Hand.getBestTotal(cards), 21)


if __name__ == '__main__':
    unittest.main()
