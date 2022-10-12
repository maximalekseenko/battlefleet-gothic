from backend.game import Game
from test2 import LunarClassCruiser


game = Game()

# player 1
game.Join(1)
vessel1p1 = game.Add_Vessel(LunarClassCruiser, 0, (0, 20 ), -90)
vessel2p1 = game.Add_Vessel(LunarClassCruiser, 0, (0, 30 ), -90)
vessel3p1 = game.Add_Vessel(LunarClassCruiser, 0, (0, 40 ), -90)

# player 2
game.Join(2)
vessel1p2 = game.Add_Vessel(LunarClassCruiser, 1, (90, 20), 90)
vessel2p2 = game.Add_Vessel(LunarClassCruiser, 1, (90, 30), 90)
vessel3p2 = game.Add_Vessel(LunarClassCruiser, 1, (90, 40), 45)

# start
game.Start()


print(vessel1p1.position)
game.Handle_Order(1, vessel1p1.Get_Order_By_Id(0).Get(position=(10, 20)))
print(vessel1p1.position)