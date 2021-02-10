# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 20:49:54 2021

@author: Franco
"""
import pygame,util,random

class NaveEnemigaComun(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("Imagenes/Sprites/nave_enemiga_comun.png").convert_alpha(), (75,75) ) 
        self.image = pygame.transform.rotozoom (self.image, 180, 1)
        self.image.set_colorkey([255, 255, 255])
        self.rect = self.image.get_rect() 
        self.vida = 2
        self.rect.x = x
        self.rect.y = y
        
    def update(self):
        if self.rect.y > 650: self.rect.y = -100 #En caso de que la nave se pierda de vista
        else:                 self.rect.y += 1
        
    
class LaserEnemigo(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Imagenes/Sprites/laser.png")
        self.image.set_colorkey([255,255,255])
        self.rect = self.image.get_rect()
    
    def update(self):
        util.movimiento(self, False, True, 0, 5)

class NaveEnemigaKamikaze(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("Imagenes/Sprites/nave_kamikaze.png").convert_alpha(), (75,75) ) 
        self.image = pygame.transform.rotozoom (self.image, 180, 1)
        self.image.set_colorkey([255, 255, 255])
        self.rect = self.image.get_rect() 
        self.vida = 1
        self.rect.x = x
        self.rect.y = y
        
    def update(self):
        if self.rect.y > 650: self.rect.y = -100 #En caso de que la nave se pierda de vista
        else:                 self.rect.y += 5



class NaveJugador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("Imagenes/Sprites/Nave de Galaga 130x100.png").convert_alpha(), (50,50) )
        self.rect = self.image.get_rect() 
        
    def update(self):
        
        keys = pygame.key.get_pressed()
        velocidadX = 7
        
        if keys[pygame.K_a] and self.rect.left >= 0:  self.rect.centerx -= velocidadX #Si la tecla que se apreto es la fecha izquierda
        if keys[pygame.K_d] and self.rect.right <= 800:  self.rect.centerx += velocidadX #Si la tecla que se apreto es la fecha derecha
        
        
        self.rect.centery = 550


class LaserJugador(pygame.sprite.Sprite): 
    def __init__(self): 
        super().__init__()
        self.image = pygame.image.load("Imagenes/Sprites/laser.png")
        self.image.set_colorkey([255,255,255])
        self.rect = self.image.get_rect()
    
    def update(self):
        self.rect.y -= 5
        
        
class Jefe(pygame.sprite.Sprite):
    def __init__(self, x, y): 
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("Imagenes/Sprites/jefe.png"), (150,150) )
        self.image = pygame.transform.rotozoom (self.image, 180, 1)
        self.image.set_colorkey([255,255,255])
        self.rect = self.image.get_rect()
        self.vida = 50
        self.rect.x = x
        self.rect.y = y
        
    def update(self):
        if self.rect.y > 750: #En caso de que la nave se pierda de vista
            self.rect.y = -200 
            self.rect.x = random.randrange(650)
        else: self.rect.y += 3
        
"""       
class MisilDerecha(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("Imagenes/Sprites/misil.png"), (45,45) )
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += 5
        

class MisilIzquierda(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("Imagenes/Sprites/misil.png"), (45,45) )
        self.image = pygame.transform.rotozoom (self.image, 180, 1)
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x -= 5
"""

class LaserEnemigoDiagonalIzquierda(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Imagenes/Sprites/laser.png")
        self.image.set_colorkey([255,255,255])
        self.rect = self.image.get_rect()
    
    def update(self):
        util.movimiento(self, True, True, 3, 5)
        

class LaserEnemigoDiagonalDerecha(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Imagenes/Sprites/laser.png")
        self.image.set_colorkey([255,255,255])
        self.rect = self.image.get_rect()
    
    def update(self):
        util.movimiento(self, True, True, -3, 5)