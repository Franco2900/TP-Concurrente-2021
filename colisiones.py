# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 20:52:48 2021

@author: Franco
"""
import pygame

def chequearColisionesDeDisparos(object):
    
    #En caso de que se acierte un disparo a una nave comun
    for laserJugador in object.lista_Laser_Jugador: 
        lista_Naves_Enemigas_impactadas = pygame.sprite.spritecollide(laserJugador, object.lista_Naves_Enemigas_Comunes, False) 
        for naveEnemigaComun in lista_Naves_Enemigas_impactadas:
            object.lista_Todos_Los_Sprites.remove(laserJugador)
            object.lista_Laser_Jugador.remove(laserJugador)
            naveEnemigaComun.vida -= 1
            if naveEnemigaComun.vida <= 0:
                object.lista_Naves_Enemigas_Comunes.remove(naveEnemigaComun)
                object.lista_Todas_Las_Naves_Enemigas.remove(naveEnemigaComun)
                object.lista_Todos_Los_Sprites.remove(naveEnemigaComun)
          
            
    #En caso de que se acierte un disparo a una nave kamikaze
    for laserJugador in object.lista_Laser_Jugador: 
        lista_Naves_Enemigas_impactadas = pygame.sprite.spritecollide(laserJugador, object.lista_Naves_Enemigas_Kamikazes, True) 
        for naveEnemigaKamikaze in lista_Naves_Enemigas_impactadas:
            object.lista_Todos_Los_Sprites.remove(laserJugador)
            object.lista_Laser_Jugador.remove(laserJugador)
            
            
    #En caso de que se acierte un disparo a un jefe
    for laserJugador in object.lista_Laser_Jugador: 
        lista_Naves_Enemigas_impactadas = pygame.sprite.spritecollide(laserJugador, object.lista_Jefes, False) 
        for jefe in lista_Naves_Enemigas_impactadas:
            object.lista_Todos_Los_Sprites.remove(laserJugador)
            object.lista_Laser_Jugador.remove(laserJugador)
            jefe.vida -= 1
            if jefe.vida <= 0: 
                object.lista_Jefes.remove(jefe)
                object.lista_Todas_Las_Naves_Enemigas.remove(jefe)
                object.lista_Todos_Los_Sprites.remove(jefe)
    
    
    #En caso de que el jugador sea impactado por un disparo
    for laserEnemigo in object.lista_Laser_Enemigos: 
        if laserEnemigo.rect.colliderect(object.naveJugador): 
            object.lista_Todos_Los_Sprites.remove(laserEnemigo)
            object.lista_Todos_Los_Sprites.remove(object.naveJugador)
            object.lista_Laser_Enemigos.remove(laserEnemigo)
            object.muerte_Jugador = True 
    
    
################################################################################################################################    
    
def chequearChoquesEntreNaves(object):
    
    #Choque de una nave comun contra el jugador
    for naveEnemigaComun in object.lista_Naves_Enemigas_Comunes: 
        if naveEnemigaComun.rect.colliderect(object.naveJugador):
            object.lista_Todos_Los_Sprites.remove(naveEnemigaComun)
            object.lista_Todos_Los_Sprites.remove(object.naveJugador)
            object.lista_Todas_Las_Naves_Enemigas.remove(naveEnemigaComun)
            object.lista_Naves_Enemigas_Comunes.remove(naveEnemigaComun)
            object.muerte_Jugador = True 
    
    
    #Choque de una nave kamikaze contra el jugador
    for naveEnemigaKamikaze in object.lista_Naves_Enemigas_Kamikazes: 
        if naveEnemigaKamikaze.rect.colliderect(object.naveJugador):
            object.lista_Todos_Los_Sprites.remove(naveEnemigaKamikaze)
            object.lista_Todos_Los_Sprites.remove(object.naveJugador)
            object.lista_Todas_Las_Naves_Enemigas.remove(naveEnemigaKamikaze)
            object.lista_Naves_Enemigas_Kamikazes.remove(naveEnemigaKamikaze)
            object.muerte_Jugador = True
    
    
    #Choque de un jefe contra el jugador
    for jefe in object.lista_Jefes: 
        if jefe.rect.colliderect(object.naveJugador):
            object.lista_Todos_Los_Sprites.remove(jefe)
            object.lista_Todos_Los_Sprites.remove(object.naveJugador)
            object.lista_Todas_Las_Naves_Enemigas.remove(jefe)
            object.lista_Jefes.remove(jefe)
            object.muerte_Jugador = True
    
    