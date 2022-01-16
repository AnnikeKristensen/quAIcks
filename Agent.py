import Game
import Pose
import Bræt

class Agent:

    def __init__(self,game,bag,board):
        self.game = game
        self.bag = bag
        self.board = board
        self.pos = game.position
        self.bagbag = bag.bag
        self.posvalues = ()
        self.whiteinbag = 0
        self.tokensinbag = 0
        self.valuetillboom = 0
        self.amountForBoom = 0

    def update(self):
        self.pos = self.game.position
        self.posvalues = self.board.get_position_value(self.pos)
        self.whiteinbag = self.bag.white_in_bag()
        self.tokensinbag = self.bag.get_bag_size()
        self.valuetillboom = self.game.boomvalue -self.board.get_white_sum()
        self.amountForBoom = self.amountToGoBoom()

    def amountToGoBoom(self):
        counter = 0
        if self.tokensinbag != 0:
            for token_color, token_value in self.bagbag:
                if token_color == "White":
                    if token_value >= self.valuetillboom:
                        counter += 1
            return counter


    def availableAction(self):
        """1: pick a random token to put on the board
        2: Stop """
        availableAction = []
        if self.valuetillboom >= 0:
            availableAction.append(1)

        if self.game.stop == False:
            availableAction.append(2)

        return availableAction
