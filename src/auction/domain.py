from src.auction.exceptions import InvalidBid


class User:

    def __init__(self, name, wallet):
        self.__name = name
        self.__wallet = wallet

    def proposes_bid(self, auc, value):
        if not self._is_value_valid(value):
            raise InvalidBid('Cannot bidding with a value higher than wallet value')

        bid = Bid(self, value)
        auc.propose(bid)
        self.__wallet -= value

    @property
    def wallet(self):
        return self.__wallet

    @property
    def name(self):
        return self.__name

    def _is_value_valid(self, value):
        return value <= self.__wallet


class Bid:

    def __init__(self, user, value):
        self.user = user
        self.value = value


class Auction:

    def __init__(self, description):
        self.description = description
        self.__bids = []
        self.highest_bid = 0.0
        self.lowest_bid = 0.0

    def propose(self, bid: Bid):
        if self._is_bid_valid(bid):

            if not self._has_bids():
                self.lowest_bid = bid.value

            self.highest_bid = bid.value

            self.__bids.append(bid)

    @property
    def bids(self):
        return self.__bids[:]

    def _has_bids(self):
        return self.__bids

    def _different_users(self, bid):
        if self.__bids[-1].user != bid.user:
            return True
        raise InvalidBid("User cannot bid twice in a row.")

    def _value_higher_than_last_bid(self, bid):
        if bid.value > self.__bids[-1].value:
            return True
        raise InvalidBid("Bid value should be higher than the last bid.")

    def _is_bid_valid(self, bid):
        return not self._has_bids() or (self._different_users(bid) and
                                        self._value_higher_than_last_bid(bid))
