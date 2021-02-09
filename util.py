# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 17:50:03 2021

@author: Franco
"""
#El archivo util es un archivo en donde guardamos todas nuestras funciones. Sirve para tener todo más organizado 
#Este archivo tiene que estar ligado a la menor cantidad posibles de otros archivos, ya que las funciones definidas aqui son de proposito general 
###################################################################################################
#Librerias
import pygame
import clases_sprites #Como el archivo clases_sprites es de proposito general, hago que trabajen juntos

###################################################################################################
#Variables
pygame.font.init()
fuenta_Arial_Grande    = pygame.font.SysFont("Arial", 100)
fuente_Arial_Mediana   = pygame.font.SysFont("Arial", 75)
fuente_Arial_Chica     = pygame.font.SysFont("Arial", 50)
fuente_Arial_Muy_Chica = pygame.font.SysFont("Arial", 25)
###################################################################################################
#Funciones

#Funciones para imprimir mensajes
def imprimir_mensaje(texto, ventana, posicion): #0 = centro. 1 = arriba. 2 = abajo. 3 = izquierda. 4 = derecha.
    mensaje = fuente_Arial_Mediana.render(texto, 0, (0,0,255) )
    
    if posicion < 3:                  ventana_x = (pygame.display.get_surface().get_width() //2) - (mensaje.get_width()//2)
    elif posicion == 3:               ventana_x = 0
    else:                             ventana_x = pygame.display.get_surface().get_width() - mensaje.get_width() 
   
    if posicion > 2 or posicion == 0: ventana_y = (pygame.display.get_surface().get_height()//2) - (mensaje.get_height()//2)
    elif posicion == 1:               ventana_y = 0
    else:                             ventana_y = (pygame.display.get_surface().get_height() ) - (mensaje.get_height() )
   
    ventana.blit(mensaje, (ventana_x, ventana_y) )
    pygame.display.update()

#--------------------------------------------------------------------------------------------------------#
#Funciones de disparo de las naves enemigas
def disparo_enemigo(object, cantidad_disparos): 
    clock = pygame.time.Clock()
    
    if object.nivel==2: cantidad_disparos = 2
    if object.nivel==3: cantidad_disparos = 3
    
    while True:
        for naveEnemiga in object.lista_Naves_Enemigas_Comunes:
            laserEnemigo1 = clases_sprites.LaserEnemigo()
            laserEnemigo1.rect.y           = naveEnemiga.rect.bottom
            
            if cantidad_disparos == 2:
                laserEnemigo1.rect.centerx = naveEnemiga.rect.centerx + 5
                laserEnemigo2              = clases_sprites.LaserEnemigo()
                laserEnemigo2.rect.centerx = naveEnemiga.rect.centerx - 5
                laserEnemigo2.rect.y       = naveEnemiga.rect.bottom
            else:                    
                laserEnemigo1.rect.centerx = naveEnemiga.rect.centerx
            
            if cantidad_disparos == 3:
                laserEnemigo2              = clases_sprites.LaserEnemigo()
                laserEnemigo2.rect.centerx = naveEnemiga.rect.centerx + 10
                laserEnemigo2.rect.y       = naveEnemiga.rect.bottom
            
                laserEnemigo3              = clases_sprites.LaserEnemigo()
                laserEnemigo3.rect.centerx = naveEnemiga.rect.centerx - 10
                laserEnemigo3.rect.y       = naveEnemiga.rect.bottom

            object.lista_Laser_Enemigos.add(laserEnemigo1)
            if cantidad_disparos > 1:  object.lista_Laser_Enemigos.add(laserEnemigo2)
            if cantidad_disparos == 3:  object.lista_Laser_Enemigos.add(laserEnemigo3)
            
            object.lista_Todos_Los_Sprites.add(laserEnemigo1)
            if cantidad_disparos > 1:  object.lista_Todos_Los_Sprites.add(laserEnemigo2)
            if cantidad_disparos == 3:  object.lista_Todos_Los_Sprites.add(laserEnemigo3)
            
        clock.tick(0.5)


def disparo_jefe(object):
    clock = pygame.time.Clock()
    
    while True:
        for jefe in object.lista_Jefes:
            misilEnemigoDerecha = clases_sprites.MisilDerecha()
            misilEnemigoDerecha.rect.x = jefe.rect.right
            misilEnemigoDerecha.rect.y = jefe.rect.midright
            object.lista_Misiles_Enemigos.add(misilEnemigoDerecha)

            misilEnemigoIzquierda = clases_sprites.MisilIzquierda()
            misilEnemigoIzquierda.rect.x = jefe.rect.left
            misilEnemigoIzquierda.rect.y = jefe.rect.midright
            object.lista_Misiles_Enemigos.add(misilEnemigoIzquierda)

    clock.tick(1)

#--------------------------------------------------------------------------------------------------------#
#Funciones de movimiento
#El movimiento de los disparos hay que modificarlo en el update de la clase Laser o LaserEnemigo (depende de cual queramos modificar)
def movimiento(object, directionX, directionY, quantityX, quantityY):
    if directionX: object.rect.x += quantityX
    if directionY: object.rect.y += quantityY

#--------------------------------------------------------------------------------------------------------#
def nivel_1(object):
    
    if object.fase_nivel == 1:
        for x in range(0, 700, 300): 
            naveEnemigaComun = clases_sprites.NaveEnemigaComun()
            naveEnemigaComun.rect.x = x
            naveEnemigaComun.rect.y = -100
    
            object.lista_Naves_Enemigas_Comunes.add(naveEnemigaComun)
            object.lista_Todas_Las_Naves_Enemigas.add(naveEnemigaComun)
            object.lista_Todos_Los_Sprites.add(naveEnemigaComun)
            
        naveEnemigaKamikaze = clases_sprites.NaveEnemigaKamikaze()
        naveEnemigaKamikaze.rect.x = 200
        naveEnemigaKamikaze.rect.y = -100
            
        object.lista_Naves_Enemigas_Kamikazes.add(naveEnemigaKamikaze)
        object.lista_Todas_Las_Naves_Enemigas.add(naveEnemigaKamikaze)
        object.lista_Todos_Los_Sprites.add(naveEnemigaKamikaze)
    
    
    if object.fase_nivel == 2:
        for i in range(4):
            if i==0:
                naveEnemigaKamikaze = clases_sprites.NaveEnemigaKamikaze()
                naveEnemigaKamikaze.rect.x = 350
                naveEnemigaKamikaze.rect.y = -100
                
    
            if i==1:
                naveEnemigaKamikaze = clases_sprites.NaveEnemigaKamikaze()
                naveEnemigaKamikaze.rect.x = 350
                naveEnemigaKamikaze.rect.y = -200
                
    
            if i==2:
                naveEnemigaKamikaze = clases_sprites.NaveEnemigaKamikaze()
                naveEnemigaKamikaze.rect.x = 350
                naveEnemigaKamikaze.rect.y = -300
                
            if i<=2:
                object.lista_Naves_Enemigas_Kamikazes.add(naveEnemigaKamikaze)
                object.lista_Todas_Las_Naves_Enemigas.add(naveEnemigaKamikaze)
                object.lista_Todos_Los_Sprites.add(naveEnemigaKamikaze)
                
            if i==3:
                naveEnemigaComun = clases_sprites.NaveEnemigaComun()
                naveEnemigaComun.rect.x = 350
                naveEnemigaComun.rect.y = -400
                
                object.lista_Naves_Enemigas_Comunes.add(naveEnemigaComun)
                object.lista_Todas_Las_Naves_Enemigas.add(naveEnemigaComun)
                object.lista_Todos_Los_Sprites.add(naveEnemigaComun)
                
                
    if object.fase_nivel == 3:
        for i in range(3):
            naveEnemigaComun = clases_sprites.NaveEnemigaComun()
            
            if i==0:
                naveEnemigaComun.rect.x = 250
                naveEnemigaComun.rect.y = -100
                naveEnemigaComun.update()
                
            if i==1:
                naveEnemigaComun.rect.x = 325
                naveEnemigaComun.rect.y = -200
                
            if i==2:
                naveEnemigaComun.rect.x = 400
                naveEnemigaComun.rect.y = -100
                    
            object.lista_Naves_Enemigas_Comunes.add(naveEnemigaComun)
            object.lista_Todas_Las_Naves_Enemigas.add(naveEnemigaComun)
            object.lista_Todos_Los_Sprites.add(naveEnemigaComun)
        
    
def nivel_2(object):
    
    if object.fase_nivel == 1:
        for i in range(4):
            naveEnemigaComun = clases_sprites.NaveEnemigaComun()
        
            if i==0:
                naveEnemigaComun.rect.x = 50
                naveEnemigaComun.rect.y = -100
            
            if i==1:
                naveEnemigaComun.rect.x = 100
                naveEnemigaComun.rect.y = -50
            
            if i==2:
                naveEnemigaComun.rect.x = 650
                naveEnemigaComun.rect.y = -50
        
            if i==3:
                naveEnemigaComun.rect.x = 700
                naveEnemigaComun.rect.y = -100
                    
            object.lista_Naves_Enemigas_Comunes.add(naveEnemigaComun)
            object.lista_Todas_Las_Naves_Enemigas.add(naveEnemigaComun)
            object.lista_Todos_Los_Sprites.add(naveEnemigaComun)
        
        
    if object.fase_nivel == 2:
        for x in range(0, 700, 75):
            naveEnemigaKamikaze = clases_sprites.NaveEnemigaKamikaze()
            naveEnemigaKamikaze.rect.x = x
            naveEnemigaKamikaze.rect.y = -100
            
            object.lista_Naves_Enemigas_Kamikazes.add(naveEnemigaKamikaze)
            object.lista_Todas_Las_Naves_Enemigas.add(naveEnemigaKamikaze)
            object.lista_Todos_Los_Sprites.add(naveEnemigaKamikaze)
            
        
    if object.fase_nivel == 3:
        for i in range(9):
            
            if i==0:
                naveEnemigaKamikaze = clases_sprites.NaveEnemigaKamikaze()
                naveEnemigaKamikaze.rect.x = 200
                naveEnemigaKamikaze.rect.y = -100
            
            if i==1:
                naveEnemigaKamikaze = clases_sprites.NaveEnemigaKamikaze()
                naveEnemigaKamikaze.rect.x = 200
                naveEnemigaKamikaze.rect.y = -200
                
            if i==2:
                naveEnemigaKamikaze = clases_sprites.NaveEnemigaKamikaze()
                naveEnemigaKamikaze.rect.x = 200
                naveEnemigaKamikaze.rect.y = -300
            
            if i==3:
                naveEnemigaKamikaze = clases_sprites.NaveEnemigaKamikaze()
                naveEnemigaKamikaze.rect.x = 200
                naveEnemigaKamikaze.rect.y = -400

            if i==4:
                naveEnemigaKamikaze = clases_sprites.NaveEnemigaKamikaze()
                naveEnemigaKamikaze.rect.x = 400
                naveEnemigaKamikaze.rect.y = -100
                
            if i==5:
                naveEnemigaKamikaze = clases_sprites.NaveEnemigaKamikaze()
                naveEnemigaKamikaze.rect.x = 400
                naveEnemigaKamikaze.rect.y = -200
                
            if i==6:
                naveEnemigaKamikaze = clases_sprites.NaveEnemigaKamikaze()
                naveEnemigaKamikaze.rect.x = 400
                naveEnemigaKamikaze.rect.y = -300
                
            if i==7:
                naveEnemigaKamikaze = clases_sprites.NaveEnemigaKamikaze()
                naveEnemigaKamikaze.rect.x = 400
                naveEnemigaKamikaze.rect.y = -400
            
            if i<=7:
                object.lista_Naves_Enemigas_Kamikazes.add(naveEnemigaKamikaze)
                object.lista_Todas_Las_Naves_Enemigas.add(naveEnemigaKamikaze)
                object.lista_Todos_Los_Sprites.add(naveEnemigaKamikaze)
        
            if i==8:
                naveEnemigaComun = clases_sprites.NaveEnemigaComun()
                naveEnemigaComun.rect.x = 300
                naveEnemigaComun.rect.y = -100
                
                object.lista_Naves_Enemigas_Comunes.add(naveEnemigaComun)
                object.lista_Todas_Las_Naves_Enemigas.add(naveEnemigaComun)
                object.lista_Todos_Los_Sprites.add(naveEnemigaComun)
        
        
def nivel_3(object):
    
    if object.fase_nivel == 1:
        for i in range(5):
            naveEnemigaComun = clases_sprites.NaveEnemigaComun()
            
            if i==0:
                naveEnemigaComun.rect.x = 375
                naveEnemigaComun.rect.y = -100
            if i==1:
                naveEnemigaComun.rect.x = 400
                naveEnemigaComun.rect.y = -200
            if i==2:
                naveEnemigaComun.rect.x = 350
                naveEnemigaComun.rect.y = -200
            if i==3:
                naveEnemigaComun.rect.x = 450
                naveEnemigaComun.rect.y = -300
            if i==4:
                naveEnemigaComun.rect.x = 300
                naveEnemigaComun.rect.y = -300
                
            object.lista_Naves_Enemigas_Comunes.add(naveEnemigaComun)
            object.lista_Todas_Las_Naves_Enemigas.add(naveEnemigaComun)
            object.lista_Todos_Los_Sprites.add(naveEnemigaComun)
    
    if object.fase_nivel == 2:
        for i in range(10):
            if i==0:
                naveEnemigaKamikaze = clases_sprites.NaveEnemigaKamikaze()
                naveEnemigaKamikaze.rect.x = 0
                naveEnemigaKamikaze.rect.y = -100
            if i==1:
                naveEnemigaKamikaze = clases_sprites.NaveEnemigaKamikaze()
                naveEnemigaKamikaze.rect.x = 75
                naveEnemigaKamikaze.rect.y = -100
            if i==2:
                naveEnemigaKamikaze = clases_sprites.NaveEnemigaKamikaze()
                naveEnemigaKamikaze.rect.x = 150
                naveEnemigaKamikaze.rect.y = -100
            if i==3:
                naveEnemigaKamikaze = clases_sprites.NaveEnemigaKamikaze()
                naveEnemigaKamikaze.rect.x = 725
                naveEnemigaKamikaze.rect.y = -400
            if i==4:
                naveEnemigaKamikaze = clases_sprites.NaveEnemigaKamikaze()
                naveEnemigaKamikaze.rect.x = 650
                naveEnemigaKamikaze.rect.y = -400
            if i==5:
                naveEnemigaKamikaze = clases_sprites.NaveEnemigaKamikaze()
                naveEnemigaKamikaze.rect.x = 575
                naveEnemigaKamikaze.rect.y = -400
            
            if i<=5:
                object.lista_Naves_Enemigas_Kamikazes.add(naveEnemigaKamikaze)
                object.lista_Todas_Las_Naves_Enemigas.add(naveEnemigaKamikaze)
                object.lista_Todos_Los_Sprites.add(naveEnemigaKamikaze)
            
            if i==6:
                naveEnemigaComun = clases_sprites.NaveEnemigaComun()
                naveEnemigaComun.rect.x = 300
                naveEnemigaComun.rect.y = -100
            if i==7:
                naveEnemigaComun = clases_sprites.NaveEnemigaComun()
                naveEnemigaComun.rect.x = 375
                naveEnemigaComun.rect.y = -100
            if i==8:
                naveEnemigaComun = clases_sprites.NaveEnemigaComun()
                naveEnemigaComun.rect.x = 450
                naveEnemigaComun.rect.y = -100
            if i==9:
                naveEnemigaComun = clases_sprites.NaveEnemigaComun()
                naveEnemigaComun.rect.x = 375
                naveEnemigaComun.rect.y = -200
        
            if i>=6:
                object.lista_Naves_Enemigas_Comunes.add(naveEnemigaComun)
                object.lista_Todas_Las_Naves_Enemigas.add(naveEnemigaComun)
                object.lista_Todos_Los_Sprites.add(naveEnemigaComun)
        
    
    if object.fase_nivel == 3:
        jefe = clases_sprites.Jefe()
        jefe.rect.x = 300
        jefe.rect.y = -100
    
        object.lista_Jefes.add(jefe)
        object.lista_Todas_Las_Naves_Enemigas.add(jefe)
        object.lista_Todos_Los_Sprites.add(jefe)

#--------------------------------------------------------------------------------------------------------#

    
    
    