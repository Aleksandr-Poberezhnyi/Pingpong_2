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

while game:
    for e in event.get():
        if e.type == quit:
            GAME = False
    if finish != True:
        window.fill(back)
        racket1.update_r()
        racket.update_l()
        ball.rect.x += speed_x 
        ball.rect.y += speed_y 
        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1
            speed_y *= 1
        if ball.rect.y > win_height-50 or ball.rect.y < 0:
            speed_y *= -1
        
        #если мяч улетел дальши ракетки, выводим условие программы для первого игрока 
        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200))
            game_over = True

        #если мяч улетел дальши ракетки, выводим условие программы для второго игрока 
        if ball.rect.x > win_width:
            finish = True
            window.blit(lose2, (200, 200))
            game_over = True
        racket1.reset()
        racket2.reset()
        ball.reset()
    display.update()
    clock.tick(FPS)
