# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 17:00:05 2021

@author: Franco
"""
import sys,pygame,threading
import clase_game,util 

########################################################################################
def main():
    pygame.init()
    
    clock = pygame.time.Clock()
    
    jugando = True
    juego = clase_game.Game(3)
    #------------------------------------------------------------#
    hilo_ataques_enemigos = threading.Thread(target=util.disparo_enemigo, args=(juego, 1,) ) 
    
    hilo_ataques_enemigos.start()
    #------------------------------------------------------------#
    
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
    
