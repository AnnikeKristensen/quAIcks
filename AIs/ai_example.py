from ContinueAIs.simple_risk_assessing_continue_ai import SimpleRiskAssessingContinueAI
from ContinueAIs.random_choice_continue_ai import RandomChoiceContinueAI
from ContinueAIs.balls_to_the_walls_continue_ai import BallsToTheWallsContinueAI
from BlueAIs.random_blue_ai import RandomBlueAI
from BlueAIs.random_non_white_blue_ai import RandomNonWhiteBlueAI
from BlueAIs.highest_non_white_blue_ai import HighestNonWhiteBlueAI
from BAIs.simple_bai import SimpleBAI

simple = SimpleRiskAssessingContinueAI("SimpleRiskAssessingContinueAI")
rando = RandomChoiceContinueAI("RandomChoiceContinueAI")
wall_e = BallsToTheWallsContinueAI("WALL-E")
simple_silent = SimpleRiskAssessingContinueAI("SimpleRiskAssessingContinueAI",
                                              verbose=False)  # de har alle denne mulighed

BLUEAI_rando = RandomBlueAI("RandomBlueAI")
BLUEAI_rando_coloured = RandomNonWhiteBlueAI("RandomNonWhiteBlueAI")
BLUEAI_high = HighestNonWhiteBlueAI("HighestNonWhiteBlueAI")

BAI_simple = SimpleBAI("SimpleBAI")

example_continue_data = {"boom_risk": 0.5,
                         "unused": "data",
                         "whatever": "doesn't matter"}

example_blue_ai_data = {"list_of_tokens": [("WHITE", 1), ("BLUE", 2), ("GREEN", 1), ("WHITE", 2)]}
example_bai_data = {"money": 13,
                    "store": [
                        (("ORANGE", 1), 3),
                        (("RED", 1), 6),
                        (("RED", 2), 10),
                        (("RED", 4), 16),
                        (("BLUE", 1), 5),
                        (("BLUE", 2), 10),
                        (("BLUE", 4), 19)]}

print("Continue AI decision examples:")
simple.make_decision(example_continue_data)
rando.make_decision(example_continue_data)
wall_e.make_decision(example_continue_data)
print(f"non verbose activation example: {simple_silent.make_decision(example_continue_data)}")

print("\nBlue AI decision examples")
print(f"using choices {example_blue_ai_data}")
BLUEAI_rando.make_decision(example_blue_ai_data)
BLUEAI_rando_coloured.make_decision(example_blue_ai_data)
BLUEAI_high.make_decision(example_blue_ai_data)
print("silent activation works the same way :D")

print("\ntesting BuyAI (BAI) with simplified store")
print(f"store contents:")
for token, price in example_bai_data["store"]:
    print(token, price)
print(f"money: {example_bai_data['money']}")
print("")
BAI_simple.make_decision(example_bai_data)
