import backend.game._new


print(1,2, 2 | 2)

quit()

from backend.game import Game
from test2 import LunarClassCruiser


game = Game()

# player 1
game.Join(1)
vessel1p1 = game.Add_Vessel(LunarClassCruiser, 0, (10, 20 ), -45)
vessel2p1 = game.Add_Vessel(LunarClassCruiser, 0, (10, 30 ), 0)
vessel3p1 = game.Add_Vessel(LunarClassCruiser, 0, (10, 40 ), 0)

# player 2
game.Join(2)
vessel1p2 = game.Add_Vessel(LunarClassCruiser, 1, (80, 20), 180)
vessel2p2 = game.Add_Vessel(LunarClassCruiser, 1, (80, 30), 180)
vessel3p2 = game.Add_Vessel(LunarClassCruiser, 1, (80, 40), 180)

# start
game.Start()


print(vessel1p1.position)
game.Handle_Order(1, vessel1p1.Get_Order_By_Id(0).Get(target=(20, 30)))
print(vessel1p1.position)