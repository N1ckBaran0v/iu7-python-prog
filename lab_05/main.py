# PyGame Animation
# IU7-25B Nikolay Baranov

import pygame
from math import sin, cos, pi
from random import randint

class Drawned(): # Нарисованный
    def __init__(self):
        self.xc = [500 + int(350 * cos(t * pi / 90)) for t in range(180)]
        self.xb = [int(50 * sin(t * pi / 180)) for t in range(360)]
        self.yb = [int(50 * cos(pi + t * pi / 180)) for t in range(360)]
        self.xal = [int(60 * cos(pi + t * pi / 45)) for t in range(90)]
        self.xar = [int(60 * cos(t * pi / 45)) for t in range(90)]
        self.ya = [int(60 * -sin(t * pi / 45)) for t in range(90)]
        self.cnt = 0
        
    def next(self, screen):
        pygame.draw.line(screen, (0, 255, 0), (self.xc[self.cnt % 180], 750), \
                        (self.xc[self.cnt % 180] + 50, 800), 5)
        pygame.draw.line(screen, (0, 255, 0), (self.xc[self.cnt % 180], 750), \
                        (self.xc[self.cnt % 180] - 50, 800), 5)
        pygame.draw.line(screen, (0, 255, 0), (self.xc[self.cnt % 180], 750), \
                        (self.xc[self.cnt % 180] + self.xb[self.cnt], 750 + self.yb[self.cnt]), 5)
        pygame.draw.line(screen, (0, 255, 0), (self.xc[self.cnt % 180] + self.xb[self.cnt], 750 + self.yb[self.cnt]), \
                        (self.xc[self.cnt % 180] + self.xb[self.cnt] + self.xal[self.cnt % 90], 750 + self.yb[self.cnt] + self.ya[self.cnt % 90]), 5)
        pygame.draw.line(screen, (0, 255, 0), (self.xc[self.cnt % 180] + self.xb[self.cnt], 750 + self.yb[self.cnt]), \
                        (self.xc[self.cnt % 180] + self.xb[self.cnt] + self.xar[self.cnt % 90], 750 + self.yb[self.cnt] + self.ya[self.cnt % 90]), 5)
        pygame.draw.circle(screen, (0, 255, 0), (self.xc[self.cnt % 180] + self.xb[self.cnt], 730 + self.yb[self.cnt]), 20)
        self.cnt += 1
        self.cnt %= 360
        
class Bebra(): # Мишка Фредди
    def __init__(self):
        self.img = pygame.image.load("freddy.png").convert()
        self.rect = self.img.get_rect()
        self.img.set_colorkey((255, 0, 0))
        
    def next(self, screen):
        self.rect.x = randint(0, 1620)
        self.rect.y = randint(0, 820)
        screen.blit(self.img, self.rect)
        
class Monika(): # Моника
    def __init__(self):
        self.img = pygame.image.load("monika.png").convert()
        self.rect = self.img.get_rect()
        self.img.set_colorkey((0, 0, 0))
        self.generate()
        
    def generate(self):
        self.y = []
        self.x = []
        t1 = [436 + int(350 * -cos(pi * i / 100)) for i in range(100)]
        t2 = [686 + int(100 * cos(pi * i / 100)) for i in range(100)]
        self.x.extend(t1)
        self.x.extend(t2)
        self.x.extend(t2[::-1])
        self.x.extend(t1[::-1])
        t1 = [800 - 10 * i + i * (i + 1) // 2 for i in range(10)]
        self.y.extend(t1)
        self.y.extend(t1[::-1])
        self.y.extend([800 for i in range(180)])
        self.cnt = 0
        
    def next(self, screen):
        self.rect.x = self.x[self.cnt]
        self.rect.y = self.y[self.cnt % 200]
        screen.blit(self.img, self.rect)
        self.cnt += 1
        self.cnt %= 400
        
class Cat(): # Котейка
    def __init__(self):
        self.img = pygame.image.load("cat.png").convert()
        self.rect = self.img.get_rect()
        self.img.set_colorkey((255, 0, 0))
        self.generate()
        
    def generate(self):
        self.y = []
        self.x = 1025
        t1 = [800 - 10 * i + i * (i + 1) // 2 for i in range(10)]
        self.y.extend([800 for i in range(300)])
        self.y.extend(t1)
        self.y.extend(t1[::-1])
        self.y.extend([800 for i in range(80)])
        self.cnt = 0
        
    def next(self, screen):
        self.rect.x = self.x
        self.rect.y = self.y[self.cnt]
        screen.blit(self.img, self.rect)
        self.cnt += 1
        self.cnt %= 400
        
class Elissu(): # Элиссу
    def __init__(self):
        self.img = pygame.image.load("elissu.png").convert()
        self.rect = self.img.get_rect()
        self.img.set_colorkey((255, 255, 255))
        self.generate()
        
    def generate(self):
        self.y = []
        self.x = []
        t1 = [1500 + int(200 * -cos(pi * i / 100)) for i in range(100)]
        self.x.extend(t1)
        self.x.extend(t1[::-1])
        self.x.extend([1300 for i in range(200)])
        
        t1 = [800 - 10 * i + i * (i + 1) // 2 for i in range(10)]
        self.y.extend([800 for i in range(100)])
        self.y.extend(t1)
        self.y.extend(t1[::-1])
        self.y.extend([800 for i in range(280)])
        self.cnt = 0
        
    def next(self, screen):
        self.rect.x = self.x[self.cnt]
        self.rect.y = self.y[self.cnt]
        screen.blit(self.img, self.rect)
        self.cnt += 1
        self.cnt %= 400
        
class Ball(): # Мячик (да он баскетббольный, и что?)
    def __init__(self):
        self.img = pygame.image.load("basketball.png").convert()
        self.rect = self.img.get_rect()
        self.img.set_colorkey((0, 0, 0))
        self.generate()
        
    def generate(self):
        self.y = []
        self.x = []
        t1 = [86 + int(1650 * i / 100) for i in range(100)]
        t2 = [1736 - int(1150 * i / 100) for i in range(100)]
        t3 = [586 + int(475 * i / 100) for i in range(100)]
        t4 = [1061 - int(975 * i / 100) for i in range(100)]
        self.x.extend(t1)
        self.x.extend(t2)
        self.x.extend(t3)
        self.x.extend(t4)
        t1 = [800 - int(300 * sin(pi * i / 100)) for i in range(50)]
        self.y.extend(t1)
        self.y.extend(t1[::-1])
        self.cnt = 0
        
    def next(self, screen):
        self.rect.x = self.x[self.cnt]
        self.rect.y = self.y[self.cnt % 100]
        screen.blit(self.img, self.rect)
        self.cnt += 1
        self.cnt %= 400
       
class Shakal(): # Шакал (степень сжатия 10 из 10)
    def __init__(self):
        self.img = pygame.image.load("shakal.png").convert()
        self.rect = self.img.get_rect()
        self.img.set_colorkey((255, 255, 255))
        self.generate()
        
    def generate(self):
        self.y = []
        self.x = 1700
        t1 = [666 - 10 * i + i * (i + 1) // 2 for i in range(10)]
        self.y.extend(t1)
        self.y.extend(t1[::-1])
        self.cnt = 0
        
    def next(self, screen):
        self.rect.x = self.x
        self.rect.y = self.y[self.cnt]
        screen.blit(self.img, self.rect)
        self.cnt += 1
        self.cnt %= 20
        
class Anon(): # Анонимус (Анонимность уровень 100)
    def __init__(self):
        self.img = pygame.image.load("anon.png").convert()
        self.rect = self.img.get_rect()
        self.img.set_colorkey((0, 0, 0))
        self.angle = 0
        
    def next(self, screen):
        temp = (300, 850)
        rot = pygame.transform.rotate(self.img, self.angle)
        rot.get_rect().center = temp
        screen.blit(rot, temp)
        self.angle += 5
        self.angle %= 360
        
class Gd(): # Не спрашивайте что это:)
    def __init__(self):
        self.img = pygame.image.load("gd.png").convert()
        self.rect = self.img.get_rect()
        self.img.set_colorkey((255, 0, 0))
        self.posy = [i for i in range(-100, 1180, 15)]
        self.t = 0
        
    def next(self, screen):
        if self.t > 1000 and self.t < 1001 + len(self.posy):
            temp = (900, self.posy[self.t - 1001])
            rot = pygame.transform.rotate(self.img, self.t - 1001)
            rot.get_rect().center = temp
            screen.blit(rot, temp)
        self.t += 1
        self.t %= 1001 + len(self.posy)

def get_list(): # Список наших персонажей
    return [Drawned(), Shakal(), Monika(), Cat(), Elissu(), Anon(), Ball(), Gd(), Bebra()]

def main(): # А вот и анимация
    pygame.init()
    screen = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
    gameover = False
    back = pygame.image.load("background.jpg") 
    backrect = back.get_rect()
    backrect.x = 0
    backrect.y = 0 
    sprites = get_list()
    while not gameover: # цикл обработки событий
        screen.fill([255, 255, 255])
        screen.blit(back, backrect)
        for hum in sprites:
            hum.next(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameover = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    gameover = True
        pygame.display.flip()
        pygame.time.wait(10)
        
    pygame.quit()
        
    
if __name__ == "__main__":
    main()
