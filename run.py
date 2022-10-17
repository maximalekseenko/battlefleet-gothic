import pygame


# theatre
from frontend.theatre import theatre

# acts
from frontend.acts import MainAct, GameAct



if __name__=="__main__":
    theatre.mainact = MainAct()
    theatre.gameact = GameAct()

    theatre.current_act = theatre.mainact
    theatre.Begin()
 