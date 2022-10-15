import pygame
from backend.game import Order


# engine
from engine import Element
from backend.theatre import theatre



# other
from frontend.elements import Clickable



class OrdersHolder(Element):
    def __init__(self, scene, orders:list[Order]) -> None:
        super().__init__(scene)

        # for snippets
        from frontend.scenes import ActionsMenu
        self.scene:ActionsMenu

        # variables
        self.orders_buttons:list[Element] = [order.Get_Visual(self.scene) for order in orders]


    def On_Update(self):
        self.rect.width = self.scene.rect.width

        left = 1
        top = self.rect.top

        # orders buttons positions
        for order_button in self.orders_buttons:

            # fix position of the order button
            order_button.rect = pygame.Rect((left, top), order_button.rect.size)
            order_button.Update()

            # get position of the next order button
            if self.rect.width <= left + 1 + order_button.rect.width:
                left = 0
                top += order_button.rect.height
            else:
                left += 1 + order_button.rect.width

        # get position of the next order button 2
        top += order_button.rect.height

        self.rect.height = top - self.rect.top


    def On_Handle(self, event:pygame.event.Event):
        for order_button in self.orders_buttons: order_button.Handle(event)


    
    def On_Render(self, target:pygame.Surface):
        for order_button in self.orders_buttons: order_button.Render(target)

