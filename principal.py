#! /usr/bin/env python
import os, random, sys, math

import pygame
from pygame.locals import *

from configuracion import *
from funcionesVACIAS import *
from extras import *

#Funcion principal
def main():
        #Centrar la ventana y despues inicializar pygame
        os.environ["SDL_VIDEO_CENTERED"] = "1"
        pygame.init()
        pygame.mixer.init()

        #sonidos
        sonidoCorrecto = pygame.mixer.Sound("assets/sonidos/correct-ding.mp3")
        sonidoError = pygame.mixer.Sound("assets/sonidos/Error.mp3")
        #musica
        musica = pygame.mixer.Sound("assets/sonidos/Tema.mp3")
        musica.play()

        

        #Preparar la ventana
        pygame.display.set_caption("Armar palabras con...")
        screen = pygame.display.set_mode((ANCHO, ALTO))

        
        #tiempo total del juego
        gameClock = pygame.time.Clock()
        totaltime = 0
        segundos = TIEMPO_MAX
        fps = FPS_inicial

        puntos = 0
        candidata = ""
        diccionario = []
        palabrasAcertadas = []
        

        #lee el diccionario
        lectura(diccionario)

        #elige las 7 letras al azar y una de ellas como principal
        letrasEnPantalla = dame7Letras()
        letraPrincipal = dameLetra(letrasEnPantalla)

        #se queda con 7 letras que permitan armar muchas palabras, evita que el juego sea aburrido
        while(len(dameAlgunasCorrectas(letraPrincipal, letrasEnPantalla, diccionario))< MINIMO):
            letrasEnPantalla = dame7Letras()
            letraPrincipal = dameLetra(letrasEnPantalla)

        print(dameAlgunasCorrectas(letraPrincipal, letrasEnPantalla, diccionario))
        

        #dibuja la pantalla la primera vez
        dibujar(screen, letraPrincipal, letrasEnPantalla, candidata, puntos, segundos)

    

        while segundos > fps/1000:
        # 1 frame cada 1/fps segundos
            gameClock.tick(fps)
            totaltime += gameClock.get_time()

            if True:
                fps = 3

            #Buscar la tecla apretada del modulo de eventos de pygame
            for e in pygame.event.get():

                #QUIT es apretar la X en la ventana
                if e.type == QUIT:
                    pygame.quit()
                    return()

                #Ver si fue apretada alguna tecla
                if e.type == KEYDOWN:
                    letra = dameLetraApretada(e.key)
                    candidata += letra   #va concatenando las letras que escribe
                    if e.key == K_BACKSPACE:
                        candidata = candidata[0:len(candidata)-1] #borra la ultima
                    if e.key == K_RETURN:  #presionó enter
                        puntos += procesar(letraPrincipal, letrasEnPantalla, candidata, diccionario , palabrasAcertadas)
                        
                        #emitimos sonidos dependiendo el numero que nos de la función procesar
                        if (procesar(letraPrincipal, letrasEnPantalla , candidata, diccionario, palabrasAcertadas) > 0):
                            sonidoCorrecto.play()
                        else:
                            sonidoError.play()
                        #si la palabra ingresada es valida, la guardamos en palabrasAcertadas    
                        if (esValida(letraPrincipal, letrasEnPantalla, candidata , diccionario , palabrasAcertadas) == True):
                            palabrasAcertadas.append(candidata) 
                            print(palabrasAcertadas)   
                            
                        candidata = ""      
            segundos = TIEMPO_MAX - pygame.time.get_ticks()/1000

            #Limpiar pantalla anterior (#Poner una imagen)
            imagen=pygame.image.load("assets/imagenes/fondo2.jpg")
            screen.blit(imagen,[0,0])

            #Dibujar de nuevo todo
            dibujar(screen, letraPrincipal, letrasEnPantalla, candidata, puntos, segundos)

            pygame.display.flip()

        while 1:
            #Esperar el QUIT del usuario
            for e in pygame.event.get():
                if e.type == QUIT:
                    pygame.quit()
                    return
                
        

#Programa Principal ejecuta Main
if __name__ == "__main__":
    main()
