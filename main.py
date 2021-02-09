# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 17:00:05 2021

@author: Franco
"""
import sys,pygame,threading
import clase_game,util 

#Hay que optimizar lo de clase_game desde la linea 116 hasta la 141 y lo de util los metodos nivel_1, nivel_2 y nivel_2
#Agregue dos clases en clases_sprites que serían para los disparos del jefe pero no anda el segundo hilo (anda trabado) asi que no pude comprobar si andan
        
########################################################################################
def main():
    pygame.init()
    
    clock = pygame.time.Clock()
    
    jugando = True
    juego = clase_game.Game(1)
    
    hilo_enemigos_comunes = threading.Thread(target=util.disparo_enemigo, args=(juego, 1,) ) 
    #hilo_jefes = threading.Thread(target=util.disparo_jefe, args=(juego, ) ) #Buscar porque se traba cuando se crea un segundo hilo
    
    hilo_enemigos_comunes.start()
    #hilo_jefes.start()
    
    
    while jugando:
        jugando = juego.procesar_eventos()
        juego.logica()
        juego.mostrar_en_pantalla(clase_game.ventana)
        clock.tick(60)
    
    pygame.quit()                      
    sys.exit()
########################################################################################

if __name__ == "__main__": 
    main()                 
    
    
    
    
    