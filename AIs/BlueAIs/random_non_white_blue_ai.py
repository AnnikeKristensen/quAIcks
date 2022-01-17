from AIs.abstract_ai import AbstractAI
import random


class RandomNonWhiteBlueAI(AbstractAI):

    def do_ai(self, args):
        list_of_tokens = args["list_of_tokens"]
        non_whites = [(token_colour, token_value) for token_colour, token_value in list_of_tokens if
                      token_colour != "WHITE"] + [None]
        return random.choice(non_whites)
