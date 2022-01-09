import Actions
import Game
import Pose
import Bræt
import Stats


def from_bag_to_board(token):
    Bræt.board.tokens_on_board.append(token)

mitBræt = Bræt.Board()
mitBræt.tokens_on_board
minHånd = Pose.Bag(mitBræt)
minHånd.initialize()
minHånd.collection_to_bag()
minHånd.get_bag_size()
minHånd.get_random_token()
mineStats = Stats.stats(mitBræt,minHånd)
mineActions = Actions.Actions()
mitSpil = Game.Game(minHånd,mitBræt,mineStats,mineActions)
print(mitSpil.color_on_board)


print(Bræt.Board.tokens_on_board)

if __name__ == '__main__':
    pass


