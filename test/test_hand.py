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
        hand.add_card(Card("Diamonds", "10"))
        self.assertEqual(hand.score, originalScore + 10)

    def test_valid_21_under(self):
        """Given my score is updated or evaluated, when my score is 21 or under, I should not be bust"""
        hand = Hand([Card("Spades", "10"), Card("Clubs", "10")])
        self.assertEqual(hand.bust, False)  # 20 is not bust
        hand.add_card(Card("Diamonds", "A"))
        self.assertEqual(hand.bust, False)  # 21 is not bust

    def test_bust_22_over(self):
        """Given my score is updated or evaluated, when my score is 22 or over, I should be bust"""
        hand = Hand([Card("Spades", "10"), Card("Clubs", "10")])
        hand.add_card(Card("Diamonds", "2"))
        self.assertEqual(hand.bust, True)  # 22 is bust

    def test_score_hand_1(self):
        """Given I have a king and an ace, when I evaluate my score, I should have 21"""
        cards = [Card("Hearts", "K"), Card("Hearts", "A")]
        self.assertEqual(Hand.get_best_total(cards), 21)

    def test_score_hand_2(self):
        """Given I have a king, a queen and an ace, when I evaluate my score, I should have 21"""
        cards = [Card("Hearts", "K"), Card("Hearts", "Q"), Card("Hearts", "A")]
        self.assertEqual(Hand.get_best_total(cards), 21)

    def test_score_hand_3(self):
        """Given I have a king, a queen, a jack and an ace, when I evaluate my score, I should have 21"""
        cards = [Card("Hearts", "9"), Card("Hearts", "A"), Card("Hearts", "A")]
        self.assertEqual(Hand.get_best_total(cards), 21)


if __name__ == '__main__':
    unittest.main()
