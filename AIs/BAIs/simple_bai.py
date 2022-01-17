from AIs.abstract_ai import AbstractAI
import random


class SimpleBAI(AbstractAI):

    def do_ai(self, args):
        assert "money" in args and "store" in args, "Assuming names 'money' and 'store' for purchase power and prices."
        if args["money"] < 3:
            return None, None
        first_limit = args['money'] - 3
        first_buy, first_price = self.buy_most_expensive_token(first_limit, args["store"])
        if first_price == 3:
            only_buy, _ = self.buy_most_expensive_token(args["money"], args["store"])
            return only_buy, None
        else:
            second_buy, _ = self.buy_most_expensive_token(args["money"] - first_price, args["store"],
                                                          skip_colour=first_buy[0])
            return first_buy, second_buy

    @staticmethod
    def buy_most_expensive_token(money, store, skip_colour=None):
        print("using money:", money)
        expensive_tokens = []
        current_price = 0
        for token, price in store:
            token_colour, _ = token
            if current_price < price <= money and token_colour != skip_colour:
                current_price = price
                expensive_tokens = [token]
            elif price == current_price and token_colour != skip_colour:
                expensive_tokens.append(token)
        print(expensive_tokens)
        return random.choice(expensive_tokens), current_price
