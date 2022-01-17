from AIs.abstract_ai import AbstractAI
import random


class RandomBlueAI(AbstractAI):

    def do_ai(self, args):
        list_of_tokens = args["list_of_tokens"]
        # TODO: bør det være en dict på formen {"list_of_tokens":[]} for at holde formatet?
        return random.choice(list_of_tokens + [None])
