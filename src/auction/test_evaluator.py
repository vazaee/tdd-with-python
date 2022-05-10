from unittest import TestCase

from src.auction.domain import User, Bid, Auction, Evaluator


class TestEvaluator(TestCase):
    def test_evaluate(self):
        gabriel = User('Gabriel')
        marcio = User('Marcio')

        marcio_bid = Bid(marcio, 100.0)
        gabriel_bid = Bid(gabriel, 150.0)

        auc = Auction('Cellphone')
        auc.bids.append(marcio_bid)
        auc.bids.append(gabriel_bid)

        evaluator = Evaluator()
        evaluator.evaluate(auc)

        lowest_value_expected = 100.0
        highest_value_expected = 150.0

        self.assertEqual(lowest_value_expected, evaluator.lowest_bid)
        self.assertEqual(highest_value_expected, evaluator.highest_bid)
