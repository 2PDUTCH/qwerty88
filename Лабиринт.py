import pygame
pygame.init()
from random import *
from time import time
from math import floor
end_game = 0
class Sprite():
    def __init__(self, pic , x , y , width , height):
        self.pic = pygame.transform.scale(pygame.image.load(pic), (width, height))
        self.rect = self.pic.get_rect()
        self.rect.x = x
        self.rect.y = y

    def render(self):
        #pygame.draw.rect(window ,(0 , 0 , 0), self.rectangle)
        window.blit(self.pic , (self.rect.x , self.rect.y))

class Player(Sprite):
    def __init__ (self, pic , x , y , width , height , x_speed , y_speed ):
        super().__init__( pic , x , y , width , height)
        self.x_speed = x_speed
        self.y_speed = y_speed

    def update(self):
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed

    def check_collision(self , wall):
        if pygame.sprite.collide_rect(Viking, wall):
            if self.rect.right > wall.rect.left and self.x_speed > 0:
                self.rect.right = wall.rect.left
                self.x_speed = 0
                self.y_speed = 0
            elif self.rect.left < wall.rect.right and self.x_speed < 0:
                self.rect.left = wall.rect.right
                self.x_speed = 0
                self.y_speed = 0
            elif self.rect.bottom > wall.rect.top and self.y_speed > 0:
                self.rect.bottom = wall.rect.top
                self.x_speed = 0
                self.y_speed = 0
            elif self.rect.top < wall.rect.bottom and self.y_speed < 0:
                self.rect.top = wall.rect.bottom
                self.x_speed = 0
                self.y_speed = 0
    def fire(self):
        bullet = Bullet('Lance.png' , self.rect.x + self.rect.width , self.rect.y , 60 , 100 , 15)
        bullets.append(bullet)

class Enemy(Sprite):
    def __init__ (self, pic , x , y , width , height , direction , speed):
        super().__init__(pic , x , y , width , height)
        self.direction = direction
        self.speed = speed

    def update(self):
        if self.rect.x <= 460:
            self.direction = 'right'
        if self.rect.x >= 715:
            self.direction = 'left'
        if self.direction == 'right':
            self.rect.x += self.speed
        if self.direction == 'left':
            self.rect.x -= self.speed

class Bullet(Sprite):
    def __init__(self, pic, x, y, width, height, speed):
        super().__init__(pic, x, y, width, height)
        self.speed = speed

    def update(self):
        self.rect.x += self.speed

    def check_collision(self):
        global Knight
        if self.rect.colliderect(Lava.rect):
            bullets.remove(self)
        if self.rect.colliderect(Knight.rect):
            Knight.speed = 0
            bullets.remove(self)


bullets = list()


Viking = Player( 'VIKING.jpg' , 100 , 100 , 100 , 100  , 0 , 0)
Food = Sprite( 'Food.png' , 700 , 700 , 60 ,60)
Knight = Enemy('Knight.jpg', 600 , 400 , 80 ,100 , 'left' , 2)
Lance = Sprite('Lance.png', 250 , 250 , 50 ,30)
Lava =Sprite('Lava.png', 300 , 350 , 150 , 600)
Barier_left = Sprite('BARIER.png' , 0 , 0 ,1 , 800)
Barier_top = Sprite('BARIER.png' , 1 , 1 ,800 , 1)
Barier_under = Sprite('BARIER.png' , 0 , 800 ,800 , 1)
Barier_right = Sprite('BARIER.png' , 800 , 0 ,1 , 800)


window = pygame.display.set_mode((800,800))
window.fill((29, 125, 15))
clock = pygame.time.Clock()
game = True
running = True
while running and game:
    sp = pygame.event.get()
    for event in sp:
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                if Viking.x_speed >= -5:
                    Viking.x_speed -= 5
            if event.key == pygame.K_d:
                if Viking.x_speed <= 5:
                    Viking.x_speed += 5
            if event.key == pygame.K_w:
                if Viking.y_speed >= -5:
                    Viking.y_speed -= 5
            if event.key == pygame.K_s:
                if Viking.y_speed <= 5:
                    Viking.y_speed += 5
            if event.key == pygame.K_SPACE:
                Viking.fire()
    if pygame.sprite.collide_rect(Viking , Food):
        end_game = pygame.transform.scale(pygame.image.load('URA.jpg'), (800, 800))
        game = False
        pass #условие выигрыша
    elif pygame.sprite.collide_rect(Viking , Knight ):
        end_game = pygame.transform.scale(pygame.image.load('Lose.jpg'), (800, 800))
        game = False
        pass #условия проигрыша

    window.fill((29, 125, 15))
    Viking.check_collision(Lava)
    Viking.check_collision(Barier_under)
    Viking.check_collision(Barier_left)
    Viking.check_collision(Barier_top)
    Viking.check_collision(Barier_right)
    Viking.update()
    Viking.render()
    Food.render()
    Lava.render()
    for i in bullets:
        i.check_collision()
        i.render()
        i.update()
    Knight.render()
    Knight.update()
    pygame.display.update()
    clock.tick(60)
while running:
    sp = pygame.event.get()
    for event in sp:
        if event.type == pygame.QUIT:
            running = False
    window.blit(end_game, (0, 0))
    pygame.display.update()
    clock.tick(60)