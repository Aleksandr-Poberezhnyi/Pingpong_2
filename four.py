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
