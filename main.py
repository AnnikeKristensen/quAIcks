import Actions
import Game
import Pose
import Bræt
import Stats


def from_bag_to_board(token):
    Bræt.board.tokens_on_board.append(token)

mitBræt = Bræt.Board()
minHånd = Pose.Bag(mitBræt)
minHånd.initialize()
print("Collection: ",minHånd.token_collection)
minHånd.collection_to_bag()
print("Bag: ", minHånd.bag)
minHånd.add_to_collection(minHånd.token_collect.green_token(1))
minHånd.collection_to_bag()
print("")
mineStats = Stats.stats(mitBræt,minHånd)
mitBræt.remove_all_tokens_from_board()
round = 0
white_sum = mitBræt.white_sum
print(mitBræt.white_sum)
print(type(white_sum))

while white_sum <= 7:
    round += 1
    minHånd.get_random_token()
    print("Round: ",round)
    print("Collection: ",minHånd.token_collection)
    print("Bag: ", minHånd.bag, "bagsize: ", minHånd.get_bag_size())
    print("Board: ", mitBræt.tokens_on_board)
    white_sum = mitBræt.white_sum
    print("White sum: ", mitBræt.get_white_sum())
    print("")

print(white_sum)
print("Boom")
if __name__ == '__main__':
    pass


