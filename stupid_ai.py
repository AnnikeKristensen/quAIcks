from abstract_ai import AbstractAI


class StupidAI(AbstractAI):

    def __init__(self):
        super().__init__()

    @staticmethod
    def continue_picking_ingredients(stats):
        return True
