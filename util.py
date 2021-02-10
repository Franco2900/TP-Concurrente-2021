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
         
        #------------------------------------------------------------#
        for jefe in object.lista_Jefes:
            laserIzquierda = clases_sprites.LaserEnemigoDiagonalIzquierda()
            laserIzquierda.rect.x = jefe.rect.right
            laserIzquierda.rect.y = jefe.rect.bottom
            object.lista_Laser_Enemigos.add(laserIzquierda)
            object.lista_Todos_Los_Sprites.add(laserIzquierda)
            
            laserDerecha = clases_sprites.LaserEnemigoDiagonalDerecha()
            laserDerecha.rect.x = jefe.rect.left
            laserDerecha.rect.y = jefe.rect.bottom
            object.lista_Laser_Enemigos.add(laserDerecha)
            object.lista_Todos_Los_Sprites.add(laserDerecha)
            """
            La idea de estos misiles era que cambien de dirección cuando estaban en la misma altura x que el jugador
            if jefe.rect.y > 0 and jefe.rect.y < 100:
                misilEnemigoDerecha = clases_sprites.MisilDerecha()
                misilEnemigoDerecha.rect.x = jefe.rect.right
                misilEnemigoDerecha.rect.y = jefe.rect.bottom
                print(jefe.rect.x,jefe.rect.y)
                object.lista_Misiles_Enemigos.add(misilEnemigoDerecha)
                object.lista_Todos_Los_Sprites.add(misilEnemigoDerecha)
        
                misilEnemigoIzquierda = clases_sprites.MisilIzquierda()
                misilEnemigoIzquierda.rect.x = jefe.rect.left
                misilEnemigoIzquierda.rect.y = jefe.rect.bottom
                object.lista_Misiles_Enemigos.add(misilEnemigoIzquierda)
                object.lista_Todos_Los_Sprites.add(misilEnemigoIzquierda)
            """
        #------------------------------------------------------------#
        clock.tick(0.5)



#--------------------------------------------------------------------------------------------------------#
#Funciones de movimiento
#El movimiento de los disparos hay que modificarlo en el update de la clase Laser o LaserEnemigo (depende de cual queramos modificar)
def movimiento(object, directionX, directionY, quantityX, quantityY):
    if directionX: object.rect.x += quantityX
    if directionY: object.rect.y += quantityY

#--------------------------------------------------------------------------------------------------------#
def nivel_1(object):
    
    if object.fase_nivel == 1:
        for x in range(50, 700, 300): 
            naveEnemigaComun = clases_sprites.NaveEnemigaComun(x, -100)
            object.lista_Naves_Enemigas_Comunes.add(naveEnemigaComun)
            object.lista_Todas_Las_Naves_Enemigas.add(naveEnemigaComun)
            object.lista_Todos_Los_Sprites.add(naveEnemigaComun)
            
        for x in range(250, 451, 200):
            naveEnemigaKamikaze = clases_sprites.NaveEnemigaKamikaze(x, -100)
            object.lista_Naves_Enemigas_Kamikazes.add(naveEnemigaKamikaze)
            object.lista_Todas_Las_Naves_Enemigas.add(naveEnemigaKamikaze)
            object.lista_Todos_Los_Sprites.add(naveEnemigaKamikaze)
    
    
    elif object.fase_nivel == 2:
        for y in range(-100, -301, -100):
            naveEnemigaKamikaze = clases_sprites.NaveEnemigaKamikaze(350, y)
            object.lista_Naves_Enemigas_Kamikazes.add(naveEnemigaKamikaze)
            object.lista_Todas_Las_Naves_Enemigas.add(naveEnemigaKamikaze)
            object.lista_Todos_Los_Sprites.add(naveEnemigaKamikaze)
        
        naveEnemigaComun = clases_sprites.NaveEnemigaComun(350, -250)
        object.lista_Naves_Enemigas_Comunes.add(naveEnemigaComun)
        object.lista_Todas_Las_Naves_Enemigas.add(naveEnemigaComun)
        object.lista_Todos_Los_Sprites.add(naveEnemigaComun)
                
                
    elif object.fase_nivel == 3:
        for i in range(250, 450, 75):
            if i != 325: naveEnemigaComun = clases_sprites.NaveEnemigaComun(i, -100)
            else:      naveEnemigaComun = clases_sprites.NaveEnemigaComun(i, -200)
            object.lista_Naves_Enemigas_Comunes.add(naveEnemigaComun)
            object.lista_Todas_Las_Naves_Enemigas.add(naveEnemigaComun)
            object.lista_Todos_Los_Sprites.add(naveEnemigaComun)
        
    
def nivel_2(object):
    if object.fase_nivel == 1:
        x = 50
        y = -100
        while x < 726:
            naveEnemigaComun = clases_sprites.NaveEnemigaComun(x, y)
            object.lista_Naves_Enemigas_Comunes.add(naveEnemigaComun)
            object.lista_Todas_Las_Naves_Enemigas.add(naveEnemigaComun)
            object.lista_Todos_Los_Sprites.add(naveEnemigaComun)
            if x == 50: y = -50
            elif x == 100: x = 600
            elif x == 650: y = -100
            x += 50
        
        
    elif object.fase_nivel == 2:
        for x in range(0, 700, 75):
            naveEnemigaKamikaze = clases_sprites.NaveEnemigaKamikaze(x, -100)
            object.lista_Naves_Enemigas_Kamikazes.add(naveEnemigaKamikaze)
            object.lista_Todas_Las_Naves_Enemigas.add(naveEnemigaKamikaze)
            object.lista_Todos_Los_Sprites.add(naveEnemigaKamikaze)
            
        
    elif object.fase_nivel == 3:
        for i in range (9):
            if i < 8:
                if i < 4:
                    x = 200
                    y = (i + 1) * -100
                else:
                    x = 400
                    y = (i - 3) * - 100
                naveEnemigaKamikaze = clases_sprites.NaveEnemigaKamikaze(x, y)
                object.lista_Naves_Enemigas_Kamikazes.add(naveEnemigaKamikaze)
                object.lista_Todas_Las_Naves_Enemigas.add(naveEnemigaKamikaze)
                object.lista_Todos_Los_Sprites.add(naveEnemigaKamikaze)
            else:
                naveEnemigaComun = clases_sprites.NaveEnemigaComun(300, -100)
                object.lista_Naves_Enemigas_Comunes.add(naveEnemigaComun)
                object.lista_Todas_Las_Naves_Enemigas.add(naveEnemigaComun)
                object.lista_Todos_Los_Sprites.add(naveEnemigaComun)
        
        
def nivel_3(object):
    
    if object.fase_nivel == 1:
        naveEnemigaComun = clases_sprites.NaveEnemigaComun(375, -100)
        object.lista_Naves_Enemigas_Comunes.add(naveEnemigaComun)
        object.lista_Todas_Las_Naves_Enemigas.add(naveEnemigaComun)
        object.lista_Todos_Los_Sprites.add(naveEnemigaComun)
        y = -100
        for x in range(375, 500, 50):
            naveEnemigaComun = clases_sprites.NaveEnemigaComun(x, y)
            object.lista_Naves_Enemigas_Comunes.add(naveEnemigaComun)
            object.lista_Todas_Las_Naves_Enemigas.add(naveEnemigaComun)
            object.lista_Todos_Los_Sprites.add(naveEnemigaComun)
            y -= 100
        for x in range(275, 350, 50):
            y += 100
            naveEnemigaComun = clases_sprites.NaveEnemigaComun(x, y)
            object.lista_Naves_Enemigas_Comunes.add(naveEnemigaComun)
            object.lista_Todas_Las_Naves_Enemigas.add(naveEnemigaComun)
            object.lista_Todos_Los_Sprites.add(naveEnemigaComun)  
    

    elif object.fase_nivel == 2:
        x = 0
        y = -100
        while x <= 726: 
            naveEnemigaKamikaze = clases_sprites.NaveEnemigaKamikaze(x, y)
            object.lista_Naves_Enemigas_Kamikazes.add(naveEnemigaKamikaze)
            object.lista_Todas_Las_Naves_Enemigas.add(naveEnemigaKamikaze)
            object.lista_Todos_Los_Sprites.add(naveEnemigaKamikaze)
            if x != 150:    x += 75
            else:
                            x = 575
                            y = -400
        x = 300
        y = -100
        while y >= -200:
            naveEnemigaComun = clases_sprites.NaveEnemigaComun(x, y)
            object.lista_Naves_Enemigas_Comunes.add(naveEnemigaComun)
            object.lista_Todas_Las_Naves_Enemigas.add(naveEnemigaComun)
            object.lista_Todos_Los_Sprites.add(naveEnemigaComun)
            if x == 450:
                x = 375
                y = -200
            elif y == -200: y-=1 #Terminar while
            else: x += 75
        
    
    elif object.fase_nivel == 3:
        jefe = clases_sprites.Jefe(300, -100)
        object.lista_Jefes.add(jefe)
        object.lista_Todas_Las_Naves_Enemigas.add(jefe)
        object.lista_Todos_Los_Sprites.add(jefe)

#--------------------------------------------------------------------------------------------------------#
