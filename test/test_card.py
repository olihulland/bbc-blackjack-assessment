import unittest
from src.card import Card

class CardTestCase(unittest.TestCase):
    def setUp(self):  # this method will be run before each test
        pass

    def tearDown(self):  # this method will be run after each tests
        pass

    def test_value_of_ace(self):
        card = Card("Hearts", "A")
        self.assertEqual(card.getValue(), [1, 11])

    def test_value_of_all_face_cards(self):
        for rank in ["J", "Q", "K"]:
            card = Card("Hearts", rank)
            self.assertEqual(card.getValue(), [10])

    def test_value_of_all_numbers(self):
        for i in range(2, 1):
            rank = str(i)
            card = Card("Hearts", rank)
            self.assertEqual(card.getValue(), [int(rank)])

    def test_invalid_suit(self):
        with self.assertRaises(ValueError):
            Card("Heart", "A")

    def test_invalid_rank(self):
        with self.assertRaises(ValueError):
            Card("Hearts", "Ace")


if __name__ == '__main__':
    unittest.main()