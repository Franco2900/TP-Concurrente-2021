# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 16:51:23 2021

@author: Franco
"""
#Añadiendo pausa
import pygame
import clases_sprites,util,colisiones
pygame.mixer.init()

ancho_ventana = 800 
alto_ventana  = 600  

ventana = pygame.display.set_mode((ancho_ventana, alto_ventana) )
####################################################################################

class Game(object): 
    def __init__(self, nivel): 
        self.stage_complete = False 
        self.muerte_Jugador = False
        self.pausa = False 
        
        self.lista_Naves_Enemigas_Comunes   = pygame.sprite.Group()
        self.lista_Naves_Enemigas_Kamikazes = pygame.sprite.Group()
        self.lista_Jefes                    = pygame.sprite.Group()
        self.lista_Todas_Las_Naves_Enemigas = pygame.sprite.Group()
        self.lista_Laser_Enemigos           = pygame.sprite.Group()
        self.lista_Misiles_Enemigos         = pygame.sprite.Group()
        self.lista_Laser_Jugador            = pygame.sprite.Group() 
        self.lista_Todos_Los_Sprites        = pygame.sprite.Group()
              
        
        self.naveJugador = clases_sprites.NaveJugador()
        self.lista_Todos_Los_Sprites.add(self.naveJugador)
        
        self.nivel = nivel
        self.fase_nivel = 1
        
        #Niveles
        if nivel == 1:
            
            self.fondo = pygame.transform.scale(pygame.image.load("Imagenes/Fondos/fondo_espacio_1.jpg"), (ancho_ventana,1200) ) 
            self.altura_fondo = -self.fondo.get_height()+alto_ventana 
            
            util.nivel_1(self)
                                
            pygame.mixer.music.load("Musica/Raiden Trad SNES Music - Gallantry.mp3")
            pygame.mixer.music.play(-1)
            
        elif nivel == 2:      
            
            self.fondo = pygame.transform.scale(pygame.image.load("Imagenes/Fondos/fondo_espacio_2.jpg"), (ancho_ventana,1200) )
            self.altura_fondo = -self.fondo.get_height()+alto_ventana
            
            util.nivel_2(self)
            
            pygame.mixer.music.load("Musica/Raiden Trad SNES Music - Lightning War.mp3")
            pygame.mixer.music.play(-1)
            
        elif nivel == 3:      
            
            self.fondo = pygame.transform.scale(pygame.image.load("Imagenes/Fondos/fondo_espacio_3.jpg"), (ancho_ventana,1200) )
            self.altura_fondo = -self.fondo.get_height()+alto_ventana
            
            util.nivel_3(self)
    
            pygame.mixer.music.load("Musica/Raiden Trad SNES Music - Fighting Thunder.mp3")
            pygame.mixer.music.play(-1)
    
    def procesar_eventos(self):
         
        for event in pygame.event.get(): #Chequeo si cerrar el juego o no
            if event.type == pygame.QUIT:                 
                return False
    
            elif self.muerte_Jugador and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  self.__init__(self.nivel)
            elif self.stage_complete and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  self.__init__(self.nivel+1) 
            
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE and not self.stage_complete and not self.muerte_Jugador: 
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
        
        if not self.stage_complete and not self.pausa: 
            self.lista_Todos_Los_Sprites.update()                                  
            colisiones.chequearColisionesDeDisparos(self)
            colisiones.chequearChoquesEntreNaves(self)         
            
            for laserJugador in self.lista_Laser_Jugador: #En caso de que los disparos del jugador se pierdan de vista
                if laserJugador.rect.y < -10: 
                    self.lista_Todos_Los_Sprites.remove(laserJugador)
                    self.lista_Laser_Jugador.remove(laserJugador)
            
            for laserEnemigo in self.lista_Laser_Enemigos: #En caso de que los disparos del enemigo se pierdan de vista
                if laserEnemigo.rect.y > 610: 
                    self.lista_Todos_Los_Sprites.remove(laserEnemigo)
                    self.lista_Laser_Enemigos.remove(laserEnemigo)

            if len(self.lista_Todas_Las_Naves_Enemigas) == 0 and self.nivel == 1 and self.fase_nivel < 3: #Para chequear la fase del nivel
                self.fase_nivel += 1         
                util.nivel_1(self)
                                
            if len(self.lista_Todas_Las_Naves_Enemigas) == 0 and self.nivel == 1 and self.fase_nivel == 3: #En caso de que se maten a todos los enemigos de la ultima fase de nivel
                self.stage_complete = True
    
            if len(self.lista_Todas_Las_Naves_Enemigas) == 0 and self.nivel == 2 and self.fase_nivel < 3: #Para chequear la fase del nivel
                self.fase_nivel += 1         
                util.nivel_2(self)
                                
            if len(self.lista_Todas_Las_Naves_Enemigas) == 0 and self.nivel == 2 and self.fase_nivel == 3: #En caso de que se maten a todos los enemigos de la ultima fase de nivel
                self.stage_complete = True
                

            if len(self.lista_Todas_Las_Naves_Enemigas) == 0 and self.nivel == 3 and self.fase_nivel < 3: #Para chequear la fase del nivel
                self.fase_nivel += 1
                if self.fase_nivel == 3:
                    pygame.mixer.music.load("Musica/Go To Blazes! (Boss Theme) Raiden Trad Genesis Soundtrack.mp3")
                    pygame.mixer.music.play(-1)
                util.nivel_3(self)                

            if len(self.lista_Todas_Las_Naves_Enemigas) == 0 and self.nivel == 3 and self.fase_nivel == 3: #En caso de que se maten a todos los enemigos de la ultima fase de nivel
                self.stage_complete = True
                pygame.mixer.music.stop()
                pygame.mixer.music.load("Musica/All Stage Clear Contra Hard Corps Genesis Soundtrack.mp3")
                pygame.mixer.music.play(-1)

            #------------------------------------------------------------#
            #Para el ataque con los laseres duales delanteros del jefe
            for jefe in self.lista_Jefes:
                laserEnemigo = clases_sprites.LaserEnemigo()
                laserEnemigo.rect.x = jefe.rect.centerx-7
                laserEnemigo.rect.y = jefe.rect.bottom
                self.lista_Laser_Enemigos.add(laserEnemigo)
                self.lista_Todos_Los_Sprites.add(laserEnemigo)
                
                laserEnemigo = clases_sprites.LaserEnemigo()
                laserEnemigo.rect.x = jefe.rect.centerx-22
                laserEnemigo.rect.y = jefe.rect.bottom             
                self.lista_Laser_Enemigos.add(laserEnemigo)
                self.lista_Todos_Los_Sprites.add(laserEnemigo)
            #------------------------------------------------------------#

            """if len(self.lista_Todas_Las_Naves_Enemigas) == 0:
                if self.nivel == 1:
                    if self.fase_nivel < 3: #Para chequear la fase del nivel
                        self.fase_nivel += 1         
                        util.nivel_1(self)
                    else: #En caso de que se maten a todos los enemigos de la ultima fase de nivel
                        self.stage_complete = True
    
                elif self.nivel == 2:
                    if self.fase_nivel < 3: #Para chequear la fase del nivel
                        self.fase_nivel += 1         
                        util.nivel_2(self)
                    else: #En caso de que se maten a todos los enemigos de la ultima fase de nivel
                        self.stage_complete = True
                      
                elif self.nivel == 3:
                    if self.fase_nivel < 3: #Para chequear la fase del nivel
                        self.fase_nivel += 1         
                        util.nivel_3(self)
                    else: #En caso de que se maten a todos los enemigos de la ultima fase de nivel
                        self.stage_complete = True"""
                        
    

    def mostrar_en_pantalla(self, ventana):
        
        if self.altura_fondo < 0: self.altura_fondo += 0.5  #Chequeo si la parte de arriba del fondo toco el pixel 0 y me fijo si sigo reccoriendo o no el fondo
        ventana.blit(self.fondo, (0,self.altura_fondo) ) 
        
        #------------------------------------------------------------#
        #Barra de vida de los enemigos
        if len(self.lista_Todas_Las_Naves_Enemigas) > 0 and not self.pausa and not self.muerte_Jugador:
            for nave in self.lista_Todas_Las_Naves_Enemigas:
                largo_total_barra = nave.rect.width
                alto_total_barra = 15
                calculo_vida_restante = int((nave.vida*100)/largo_total_barra)
                rectangulo_vida = pygame.Rect(nave.rect.left, nave.rect.top-alto_total_barra, calculo_vida_restante, alto_total_barra)
                pygame.draw.rect(ventana, ([0,255,0]), rectangulo_vida)
        #------------------------------------------------------------#
        
        if self.muerte_Jugador:                        util.imprimir_mensaje("Has muerto", ventana, 0)       
        elif self.pausa:                               util.imprimir_mensaje("Pausa", ventana, 0) 
        elif self.stage_complete and not self.muerte_Jugador:
            if self.nivel < 3:                         util.imprimir_mensaje("Stage complete", ventana, 0)
            else:                                      util.imprimir_mensaje("You won the game", ventana, 0)        
        elif not self.stage_complete and not self.pausa:    self.lista_Todos_Los_Sprites.draw(ventana) 
        
        pygame.display.update() 
