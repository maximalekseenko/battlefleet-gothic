class Player:
    def __init__(self, game, socket) -> None:
        self.socket = socket

        from backend.game.game import Game
        self.game:Game = game

        self.color = self.game.Get_Player_Color()
