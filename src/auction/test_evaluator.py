from unittest import TestCase

from src.auction.domain import User, Bid, Auction


class TestEvaluator(TestCase):

    def setUp(self):
        self.gabriel = User('Gabriel')
        self.gabriel_bid = Bid(self.gabriel, 150.0)
        self.auc = Auction('Cellphone')

    def test_must_return_the_highest_and_lowest_value_when_added_in_ascending_order(self):
        marcio = User('Marcio')
        marcio_bid = Bid(marcio, 100.0)

        self.auc.propose(marcio_bid)
        self.auc.propose(self.gabriel_bid)

        lowest_value_expected = 100.0
        highest_value_expected = 150.0

        self.assertEqual(lowest_value_expected, self.auc.lowest_bid)
        self.assertEqual(highest_value_expected, self.auc.highest_bid)

    def test_must_return_the_highest_and_lowest_value_when_added_in_descending_order(self):
        marcio = User('Marcio')
        marcio_bid = Bid(marcio, 100.0)

        self.auc.propose(self.gabriel_bid)
        self.auc.propose(marcio_bid)

        lowest_value_expected = 100.0
        highest_value_expected = 150.0

        self.assertEqual(lowest_value_expected, self.auc.lowest_bid)
        self.assertEqual(highest_value_expected, self.auc.highest_bid)

    def test_must_return_same_value_for_highest_and_lowest_value_when_auction_has_a_bid(self):
        self.auc.propose(self.gabriel_bid)

        self.assertEqual(150.0, self.auc.lowest_bid)
        self.assertEqual(150.0, self.auc.highest_bid)

    def test_must_return_the_highest_and_lowest_value_when_auction_has_three_bids(self):
        marcio = User('Marcio')
        vine = User('Vinicius')

        marcio_bid = Bid(marcio, 100.0)
        vine_bid = Bid(vine, 200.0)

        self.auc.propose(self.gabriel_bid)
        self.auc.propose(marcio_bid)
        self.auc.propose(vine_bid)

        lowest_value_expected = 100.0
        highest_value_expected = 200.0

        self.assertEqual(lowest_value_expected, self.auc.lowest_bid)
        self.assertEqual(highest_value_expected, self.auc.highest_bid)
