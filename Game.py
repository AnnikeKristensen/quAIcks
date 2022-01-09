class Game():
    def __init__(self, bag, board, stats, actions):
        self.score = 0
        self.bag= self.bag.bag
        self.boardtokens = self.board.tokens_on_board
        self.color_on_board = self.board.get_colors_sum()[2]
        print(self.color_on_board)

    def available_actions_roundA(self):
        pass

    def boomValue(self):
        pass

    def turn(self):
        pass

    def temp_end_turn(self):
        pass
