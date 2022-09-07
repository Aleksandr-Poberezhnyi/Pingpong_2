        #если мяч достигает границ экрана меняем направление его движения    
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
