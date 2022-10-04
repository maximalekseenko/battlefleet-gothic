from backend.game import Game
from test2 import LunarClassCruiser


class PseudoPlayer:
    def __init__(self, actions) -> None:
        self.actions = actions

    def sendall(self, data):pass
    def recv(self): return self.actions.pop(0)


game = Game()

# player 1
player1 = PseudoPlayer(["test"])
game.Join(player1)
vessel1p1 = game.Add_Vessel(LunarClassCruiser, 0, (0, 20 ), -90)
vessel2p1 = game.Add_Vessel(LunarClassCruiser, 0, (0, 30 ), -90)
vessel3p1 = game.Add_Vessel(LunarClassCruiser, 0, (0, 40 ), -90)

# player 2
player2 = PseudoPlayer(["test"])
game.Join(player2)
vessel1p2 = game.Add_Vessel(LunarClassCruiser, 1, (90, 20), 90)
vessel2p2 = game.Add_Vessel(LunarClassCruiser, 1, (90, 30), 90)
vessel3p2 = game.Add_Vessel(LunarClassCruiser, 1, (90, 40), 45)

# start
game.Start()


# from backend.game.common.actions.move import Move
game_actions = [
    # turn1
    [
        vessel1p1.movement_actions[0].Get_Done(game, (10, 20)),
        vessel2p1.movement_actions[0].Get_Done(game, (20, 30)),
        vessel3p1.movement_actions[0].Get_Done(game, (30, 20))
    ],
]



import pygame

vessel1_image = pygame.Surface((5,10), pygame.SRCALPHA)
pygame.draw.polygon(vessel1_image, "#a00000", ((0,9),(2,0),(4,9)))

vessel2_image = pygame.Surface((5,10), pygame.SRCALPHA)
pygame.draw.polygon(vessel2_image, "#00a000", ((0,9),(2,0),(4,9)))


def Render(screen:pygame.Surface):
    # field
    pygame.draw.rect(screen, "#a0a0a0", ((0,0), (game.size[0] * 2, game.size[1] * 2)), 1)

    # vessels
    for vessel in game.forces:
        vessel_image = vessel1_image.copy() if vessel.owner==player1 else vessel2_image.copy()
        vessel_image = pygame.transform.rotate(vessel_image, vessel.rotation)

        screen.blit(vessel_image, (
            vessel.position[0] * 2 - vessel_image.get_width() / 2, 
            vessel.position[1] * 2 - vessel_image.get_height() / 2))

        mouse_position = pygame.mouse.get_pos()
        mouse_position = (mouse_position[0]/2, mouse_position[1]/2)
        target_screen_position = vessel.movement_actions[0].Fix_Args(game, mouse_position)['position']
        target_screen_position = (target_screen_position[0] * 2, target_screen_position[1] * 2)
        # action
        pygame.draw.line(screen, "#ff0000", (vessel.position[0] * 2, vessel.position[1] * 2), target_screen_position)


def Handle(event:pygame.event.Event):
    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
        if len(game_actions) == 0: return
        turn_actions = game_actions.pop(0)
        for action in turn_actions:
            game.Handle_Action(player1 ,action)
            game.Handle_Action(player2 ,action)

    if event.type == pygame.MOUSEBUTTONDOWN:
        pass


def Run():

    # pygame init
    pygame.init()
    screen = pygame.display.set_mode((640, 480), pygame.RESIZABLE)
    clock = pygame.time.Clock()
    is_running = True

    # loop
    while is_running:

        # tick
        clock.tick(60)

        # handle
        for event in pygame.event.get():

            Handle(event)
            
            if event.type == pygame.QUIT:
                is_running = False

        # render
        screen.fill('#ffffff')
        Render(screen)

        pygame.display.update()

    pygame.quit()

Run()
