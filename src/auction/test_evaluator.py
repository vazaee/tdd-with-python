from unittest import TestCase

from src.auction.domain import User, Bid, Auction, Evaluator


class TestEvaluator(TestCase):

    def setUp(self):
        self.gabriel = User('Gabriel')
        self.gabriel_bid = Bid(self.gabriel, 150.0)
        self.auc = Auction('Cellphone')

    def test_must_return_the_highest_and_lowest_value_when_added_in_ascending_order(self):
        marcio = User('Marcio')
        marcio_bid = Bid(marcio, 100.0)

        self.auc.bids.append(marcio_bid)
        self.auc.bids.append(self.gabriel_bid)

        evaluator = Evaluator()
        evaluator.evaluate(self.auc)

        lowest_value_expected = 100.0
        highest_value_expected = 150.0

        self.assertEqual(lowest_value_expected, evaluator.lowest_bid)
        self.assertEqual(highest_value_expected, evaluator.highest_bid)

    def test_must_return_the_highest_and_lowest_value_when_added_in_descending_order(self):
        marcio = User('Marcio')
        marcio_bid = Bid(marcio, 100.0)

        self.auc.bids.append(self.gabriel_bid)
        self.auc.bids.append(marcio_bid)

        evaluator = Evaluator()
        evaluator.evaluate(self.auc)

        lowest_value_expected = 100.0
        highest_value_expected = 150.0

        self.assertEqual(lowest_value_expected, evaluator.lowest_bid)
        self.assertEqual(highest_value_expected, evaluator.highest_bid)

    def test_must_return_same_value_for_highest_and_lowest_value_when_auction_has_a_bid(self):
        self.auc.bids.append(self.gabriel_bid)

        evaluator = Evaluator()
        evaluator.evaluate(self.auc)

        self.assertEqual(150.0, evaluator.lowest_bid)
        self.assertEqual(150.0, evaluator.highest_bid)

    def test_must_return_the_highest_and_lowest_value_when_auction_has_three_bids(self):
        marcio = User('Marcio')
        vine = User('Vinicius')

        marcio_bid = Bid(marcio, 100.0)
        vine_bid = Bid(vine, 200.0)

        self.auc.bids.append(self.gabriel_bid)
        self.auc.bids.append(marcio_bid)
        self.auc.bids.append(vine_bid)

        evaluator = Evaluator()
        evaluator.evaluate(self.auc)

        lowest_value_expected = 100.0
        highest_value_expected = 200.0

        self.assertEqual(lowest_value_expected, evaluator.lowest_bid)
        self.assertEqual(highest_value_expected, evaluator.highest_bid)
