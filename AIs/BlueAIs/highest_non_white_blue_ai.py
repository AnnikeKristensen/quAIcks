from AIs.abstract_ai import AbstractAI
import random

class HighestNonWhiteBlueAI(AbstractAI):

    def do_ai(self, list_of_tokens):
        non_whites = [(token_colour, token_value) for token_colour, token_value in list_of_tokens if
                      token_colour != "WHITE"]
        if len(non_whites) == 0:
            return None
        best = max([token_value for token_colour, token_value in non_whites if
                    token_colour != "WHITE"])
        best_set = [(token_colour, token_value) for token_colour, token_value in non_whites if
                    token_value == best]
        return random.choice(best_set)
