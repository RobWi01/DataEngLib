from math import floor


# We can buy, sell, or do nothing each time we make a decision.
# This class defies a nobject for keeping track of our current investments/profits for each currency pair
class Portfolio(object):
    def __init__(self, from_, to):
        # Initialize the 'From' currency amont to 1
        self.amount = 1
        self.curr2 = 0
        self.from_ = from_
        self.to = to
        # We want to keep track of state, to see what our next trade should be
        self.Prev_Action_was_Buy = False

    # This defines a function to buy the 'To' currency. It will always buy the max amount, in whole number
    # increments
    def buy_curr(self, price):
        if self.amount >= 1:
            num_to_buy = floor(self.amount)
            self.amount -= num_to_buy
            self.Prev_Action_was_Buy = True
            self.curr2 += num_to_buy * price
            print(
                "Bought %d worth of the target currency (%s). Our current profits and losses in the original currency (%s) are: %f." % (
                    num_to_buy, self.to, self.from_, (self.amount - 1)))
        else:
            print("There was not enough of the original currency (%s) to make another buy." % self.from_)

    # This defines a function to sell the 'To' currency. It will always sell the max amount, in a whole number
    # increments
    def sell_curr(self, price):
        if self.curr2 >= 1:
            num_to_sell = floor(self.curr2)
            self.amount += num_to_sell * (1 / price)
            self.Prev_Action_was_Buy = False
            self.curr2 -= num_to_sell
            print(
                "Sold %d worth of the target currency (%s). Our current profits and losses in the original currency (%s) are: %f." % (
                    num_to_sell, self.to, self.from_, (self.amount - 1)))
        else:
            print("There was not enough of the target currency (%s) to make another sell." % self.to)
