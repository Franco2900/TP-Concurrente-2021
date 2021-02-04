# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 16:51:23 2021

@author: Franco
"""
#Añadiendo pausa
import pygame
import clases_sprites,util,math
pygame.mixer.init()

ancho_ventana = 800 
alto_ventana  = 600  

ventana = pygame.display.set_mode((ancho_ventana, alto_ventana) )
####################################################################################

class Game(object): 
    def __init__(self, nivel): 
        self.game_over = False 
        self.muerte_Jugador = False
        self.pausa = False 
        
        self.lista_Naves_Enemigas_Comunes   = pygame.sprite.Group()
        self.lista_Naves_Enemigas_Kamikazes = pygame.sprite.Group()
        self.lista_Jefes                    = pygame.sprite.Group()
        self.lista_Todas_Las_Naves_Enemigas = pygame.sprite.Group()
        self.lista_Laser_Enemigos           = pygame.sprite.Group() 
        self.lista_Laser_Jugador            = pygame.sprite.Group() 
        self.lista_Todos_Los_Sprites        = pygame.sprite.Group()
        
        
        self.naveJugador = clases_sprites.NaveJugador()
        self.lista_Todos_Los_Sprites.add(self.naveJugador)
        
        self.nivel = nivel
        
        #Niveles
        if nivel == 1:
            
            self.fondo = pygame.transform.scale(pygame.image.load("Imagenes/Fondos/fondo_espacio_1.jpg"), (ancho_ventana,1200) ) 
            self.altura_fondo = -self.fondo.get_height()+alto_ventana 
            
            util.nivel_1(self)
                                
            pygame.mixer.music.load("Musica/Raiden Trad SNES Music - Gallantry.mp3")
            pygame.mixer.music.play()
            
        elif nivel == 2:      
            
            self.fondo = pygame.transform.scale(pygame.image.load("Imagenes/Fondos/fondo_espacio_2.jpg"), (ancho_ventana,1200) )
            self.altura_fondo = -self.fondo.get_height()+alto_ventana
            
            util.nivel_2(self)
            
            pygame.mixer.music.load("Musica/Raiden Trad SNES Music - Lightning War.mp3")
            pygame.mixer.music.play()
            
        elif nivel == 3:      
            
            self.fondo = pygame.transform.scale(pygame.image.load("Imagenes/Fondos/fondo_espacio_3.jpg"), (ancho_ventana,1200) )
            self.altura_fondo = -self.fondo.get_height()+alto_ventana
            
            util.nivel_3(self)
    
            pygame.mixer.music.load("Musica/Raiden Trad SNES Music - Fighting Thunder.mp3")
            pygame.mixer.music.play()
    
    def procesar_eventos(self):
         
        for event in pygame.event.get():           
            if event.type == pygame.QUIT:                 
                return False
    
            elif self.muerte_Jugador and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  self.__init__(self.nivel)
            elif self.game_over and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:       self.__init__(self.nivel+1) 
            
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE and not self.game_over and not self.muerte_Jugador: 
                if not self.pausa: self.pausa = True
                else:              self.pausa = False
    
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: 
                laser = clases_sprites.LaserJugador()
                    
                laser.rect.centerx = self.naveJugador.rect.centerx
                laser.rect.y       = self.naveJugador.rect.top
                
                self.lista_Laser_Jugador.add(laser)
                self.lista_Todos_Los_Sprites.add(laser)
    
        return True
    
    
    
    def logica(self):
        
        if not self.game_over and not self.pausa: 
            self.lista_Todos_Los_Sprites.update()                                
                
            for laserJugador in self.lista_Laser_Jugador: #En caso de que se acierte a una nave comun
                lista_Naves_Enemigas_impactadas = pygame.sprite.spritecollide(laserJugador, self.lista_Naves_Enemigas_Comunes, False) 
                for naveEnemigaComun in lista_Naves_Enemigas_impactadas:
                    self.lista_Todos_Los_Sprites.remove(laserJugador)
                    self.lista_Laser_Jugador.remove(laserJugador)
                    naveEnemigaComun.vida -= 1
                    if naveEnemigaComun.vida <= 0:
                        self.lista_Naves_Enemigas_Comunes.remove(naveEnemigaComun)
                        self.lista_Todas_Las_Naves_Enemigas.remove(naveEnemigaComun)
                        self.lista_Todos_Los_Sprites.remove(naveEnemigaComun)
                        
            for laserJugador in self.lista_Laser_Jugador: #En caso de que se acierte a una nave kamikaze
                lista_Naves_Enemigas_impactadas = pygame.sprite.spritecollide(laserJugador, self.lista_Naves_Enemigas_Kamikazes, True) 
                for naveEnemigaKamikaze in lista_Naves_Enemigas_impactadas:
                    self.lista_Todos_Los_Sprites.remove(laserJugador)
                    self.lista_Laser_Jugador.remove(laserJugador)
            
            for laserJugador in self.lista_Laser_Jugador: #En caso de que se acierte a un jefe
                lista_Naves_Enemigas_impactadas = pygame.sprite.spritecollide(laserJugador, self.lista_Jefes, False) 
                for jefe in lista_Naves_Enemigas_impactadas:
                    self.lista_Todos_Los_Sprites.remove(laserJugador)
                    self.lista_Laser_Jugador.remove(laserJugador)
                    jefe.vida -= 1
                    if jefe.vida <= 0: 
                        self.lista_Jefes.remove(jefe)
                        self.lista_Todas_Las_Naves_Enemigas.remove(jefe)
                        self.lista_Todos_Los_Sprites.remove(jefe)
            
            
            for laserEnemigo in self.lista_Laser_Enemigos: #En caso de que el jugador sea impactado
                if laserEnemigo.rect.colliderect(self.naveJugador): 
                    self.lista_Todos_Los_Sprites.remove(laserEnemigo)
                    self.lista_Todos_Los_Sprites.remove(self.naveJugador)
                    self.lista_Laser_Enemigos.remove(laserEnemigo)
                    self.muerte_Jugador = True 
            
            for naveEnemigaComun in self.lista_Naves_Enemigas_Comunes: #Choque de una nave comun contra el jugador
                if naveEnemigaComun.rect.colliderect(self.naveJugador):
                    self.lista_Todos_Los_Sprites.remove(naveEnemigaComun)
                    self.lista_Todos_Los_Sprites.remove(self.naveJugador)
                    self.lista_Todas_Las_Naves_Enemigas.remove(naveEnemigaComun)
                    self.lista_Naves_Enemigas_Comunes.remove(naveEnemigaComun)
                    self.muerte_Jugador = True 
                    
            for naveEnemigaKamikaze in self.lista_Naves_Enemigas_Kamikazes: #Choque de una nave kamikaze contra el jugador
                if naveEnemigaKamikaze.rect.colliderect(self.naveJugador):
                    self.lista_Todos_Los_Sprites.remove(naveEnemigaKamikaze)
                    self.lista_Todos_Los_Sprites.remove(self.naveJugador)
                    self.lista_Todas_Las_Naves_Enemigas.remove(naveEnemigaKamikaze)
                    self.lista_Naves_Enemigas_Kamikazes.remove(naveEnemigaKamikaze)
                    self.muerte_Jugador = True
            
            
            for laserJugador in self.lista_Laser_Jugador: #En caso de que los disparos del jugador se pierdan de vista
                if laserJugador.rect.y < -10: 
                    self.lista_Todos_Los_Sprites.remove(laserJugador)
                    self.lista_Laser_Jugador.remove(laserJugador)
            
            for laserEnemigo in self.lista_Laser_Enemigos: #En caso de que los disparos del enemigo se pierdan de vista
                if laserEnemigo.rect.y > 610: 
                    self.lista_Todos_Los_Sprites.remove(laserEnemigo)
                    self.lista_Laser_Enemigos.remove(laserEnemigo)
    
    
            if len(self.lista_Todas_Las_Naves_Enemigas) == 0: 
                   self.game_over = True
    
             
    
    def mostrar_en_pantalla(self, ventana):
        
        if self.altura_fondo < 0: self.altura_fondo += 0.5  #Chequeo si la parte de arriba del fondo toco el pixel 0 y me fijo si sigo reccoriendo o no el fondo
        ventana.blit(self.fondo, (0,self.altura_fondo) ) 
        
              
        for nave in self.lista_Todas_Las_Naves_Enemigas:#No anda como debe / Posible segundo hilo
            largo_total_barra = nave.rect.width
            alto_total_barra = 15
            calculo_vida_restante = int((nave.vida*100)/largo_total_barra)
            #print(math.ceil(nave.vida/100))
            #print(calculo_vida_restante)
            rectangulo_vida = pygame.Rect(nave.rect.left, nave.rect.top-alto_total_barra, calculo_vida_restante, alto_total_barra)
            pygame.draw.rect(ventana, ([0,255,0]), rectangulo_vida)
        
        
        if self.game_over and not self.muerte_Jugador:   util.imprimir_mensaje("Game over", ventana, 0)        
        elif self.muerte_Jugador:                        util.imprimir_mensaje("Has muerto", ventana, 0)       
        elif self.pausa:                                 util.imprimir_mensaje("Pausa", ventana, 0) 
        elif not self.game_over and not self.pausa:      self.lista_Todos_Los_Sprites.draw(ventana) 
        
        pygame.display.update() 
