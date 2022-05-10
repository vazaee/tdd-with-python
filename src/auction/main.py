from src.auction.domain import User, Bid, Auction, Evaluator

gabriel = User('Gabriel')
marcio = User('Marcio')

marcio_bid = Bid(marcio, 100.0)
gabriel_bid = Bid(gabriel, 150.0)

auc = Auction('Cellphone')
auc.bids.append(marcio_bid)
auc.bids.append(gabriel_bid)

for bid in auc.bids:
    print(f'User {bid.user.name} bid {bid.value}')

evaluator = Evaluator()
evaluator.evaluate(auc)

print(f'The lowest bid was {evaluator.lowest_bid} and the highest bid was {evaluator.highest_bid}')