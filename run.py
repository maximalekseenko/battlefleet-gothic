import pygame

# theatre
from backend.theatre import theatre

# acts
from frontend.acts import MainAct, GameAct



if __name__=="__main__":
    theatre.mainact = MainAct()
    theatre.game_act = GameAct()

    theatre.current_act = theatre.mainact
    theatre.Begin()
 