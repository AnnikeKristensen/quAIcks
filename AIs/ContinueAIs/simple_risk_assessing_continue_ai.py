from AIs.abstract_ai import AbstractAI
import random


class SimpleRiskAssessingContinueAI(AbstractAI):
    ai_name = "SimpleRiskAssessingContinueAI"

    def do_ai(self, args):
        assert "boom_risk" in args, "This AI needs the risk of going boom, or needs to be rewritten to calculate it."
        assert 0 <= args["boom_risk"] <= 1, "Boom risk needs to be between 0 and 1, sorry!"
        choice = random.random()
        if choice <= args["boom_risk"]:
            return "STOP"
        return "CONTINUE"
