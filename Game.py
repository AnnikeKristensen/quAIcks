class Game():
    """The actual gameplay"""
    def __init__(self, bag, board, stats, actions):
        self.score = 0
        self.bag= self.bag.bag
        self.boardtokens = self.board.tokens_on_board
        self.color_on_board = self.board.get_colors_sum()[2]
        print(self.color_on_board)

    def available_actions_roundA(self):
        """What the AI can do next"""
        pass

    def boomValue(self):
        """Checks the boomvalue. Per default >7, but can be increased with specific tokens"""
        pass

    def turn(self):
        """defines a turn"""
        pass

    def temp_end_turn(self):
        """ For now while roundB hasnt been made, if AI chooses to stop, this will happen.
        Scores get accumulated, all tokens get back into the bag"""
        pass
