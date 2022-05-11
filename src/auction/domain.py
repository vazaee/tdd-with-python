
class User:

    def __init__(self, name, wallet):
        self.__name = name
        self.__wallet = wallet

    def proposes_bid(self, auc, value):
        if value > self.__wallet:
            raise ValueError('Cannot bidding with a value higher than wallet value')

        bid = Bid(self, value)
        auc.propose(bid)
        self.__wallet -= value

    @property
    def wallet(self):
        return self.__wallet

    @property
    def name(self):
        return self.__name


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
        if not self.__bids or self.__bids[-1].user != bid.user and bid.value > self.__bids[-1].value:

            if not self.__bids:
                self.lowest_bid = bid.value

            self.highest_bid = bid.value

            self.__bids.append(bid)
        else:
            raise ValueError("Bidding error")

    @property
    def bids(self):
        return self.__bids[:]
