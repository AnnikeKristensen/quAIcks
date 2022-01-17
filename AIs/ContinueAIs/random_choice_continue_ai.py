from AIs.abstract_ai import AbstractAI
import random


class RandomChoiceContinueAI(AbstractAI):
    ai_name = "RandomChoiceContinueAI"

    def do_ai(self, args):
        return random.choice(["CONTINUE", "STOP"])
