from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (wight, height)) #вместе 55,55 - параметры
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < 400:
            self.rect.x += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < 400:
            self.rect.x += self.speed

#pyinstaller --onefail<pin_pong_end>.py pyinstaller --onefail PIN_PONG.py

window = display.set_mode((550,750))#размер экрана
display.set_caption('Чёрная понг')#название приложения
fon = transform.scale(image.load('pole.png'),(550,750))#картинка фона и её размер

'''global game
global finish'''
game = True
finish = False
clock = time.Clock()
FPS = 60
  
racket1 = Player('pok1.png', 0, 52, 10, 150, 30) 
racket2 = Player('pok2.png', 400, 670, 10, 150, 30)
ball = GameSprite('boll1.png', 260, 350, 10, 30, 30)
'''
sprite1 = Player('pok1.png',252, 50, 50, 11, 5)
sprite2 = Player('pok2.png',252, 700, 50, 11, 5)
boll = GameSprite('boll1.png',252, 350, 50, 50, 5)
win_width = 600_ширина = 600
win_height = 500_высота = 500
'''
font.init()
font = font.Font(None, 70)
lose1 = font.render('Зелёный выиграл!', True, (0, 255, 0))
lose2 = font.render('Красный выиграл!', True, (255, 0, 0))
lose3 = font.render('Зелёный проиграл!', True, (0, 255, 0))
lose4 = font.render('Красный проиграл!', True, (255, 0, 0))
speed_x = 10
speed_y = 10

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        

    if finish != True:
        window.blit(fon,(0,0))
        racket1.update_l()
        racket2.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_y *= -1
            speed_x *= 1 

        if ball.rect.x > 500 or ball.rect.x < 0:
            speed_x *= -1

        if ball.rect.y < 0:
            finish = True
            window.blit(lose1, (50, 600))
            window.blit(lose4, (50, 100))
            game_over = True

        if ball.rect.y > 750:
            finish = True
            window.blit(lose2, (50, 100))#красный
            window.blit(lose3, (50, 600))
            game_over = True

        '''keys = key.get_pressed()
        if keys[K_UP] :
            game = True and finish = False'''

        racket1.reset()
        racket2.reset()
        ball.reset()
    display.update()
    clock.tick(FPS)
    