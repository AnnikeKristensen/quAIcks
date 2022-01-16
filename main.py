import Pose
import Bræt
import Agent
import Game

brættet = Bræt.Board()
posen = Pose.Bag(brættet)
posen.initialize()
posen.collection_to_bag()
spillet = Game.Game(posen,brættet)
spilleren = Agent.Agent(spillet,posen,brættet)
spilleren.update()
print(spilleren.availableAction())
