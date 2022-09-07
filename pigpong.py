from pygame import *

class Sprite_(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,width,height):
        super().__init__()
        
        self.image = transform.scale(image.load(player_image), (width,height))
        self.speed = player_speed

        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        win.blit(self.image,(self.rect.x,self.rect.y))
