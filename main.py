import pygame

# theatre
from theatre import theatre

# acts
from game.game_act import Game_Act
from mainmenu import MainAct



if __name__=="__main__":
    theatre.mainact = MainAct()
    theatre.game_act = Game_Act()

    theatre.current_act = theatre.mainact
    theatre.Begin()
 