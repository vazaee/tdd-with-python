from src.auction.domain import User, Auction

import pytest


@pytest.fixture
def vini():
    return User('Vinicius', 100.0)


@pytest.fixture
def auc():
    return Auction('Cellphone')


def test_must_subtract_value_from_the_users_wallet_when_the_user_proposes_a_bid(vini, auc):
    vini.proposes_bid(auc, 50.0)

    assert vini.wallet == 50.0


def test_must_allow_bidding_when_value_lower_than_wallet_value(vini, auc):
    vini.proposes_bid(auc, 1.0)

    assert vini.wallet == 99.0


def test_must_allow_bidding_when_value_equal_wallet_value(vini, auc):
    vini.proposes_bid(auc, 100.0)

    assert vini.wallet == 0.0


def test_should_not_allow_bidding_with_value_higher_than_wallet_value(vini, auc):
    with pytest.raises(ValueError):

        vini.proposes_bid(auc, 200.0)
