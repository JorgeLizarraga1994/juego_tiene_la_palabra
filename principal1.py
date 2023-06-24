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

        #fondo
        imagen=pygame.image.load("assets/imagenes/espacio.jpg")
        futuro=pygame.image.load("assets/imagenes/futuro.jpg")
        huawei=pygame.image.load("assets/imagenes/huawei.jpg")
        #sonidos
        sonidoCorrecto = pygame.mixer.Sound("assets/sonidos/correct-ding.mp3")
        sonidoError = pygame.mixer.Sound("assets/sonidos/Error.mp3")
        #musica
        musica = pygame.mixer.Sound("assets/sonidos/musica.mp3")
        musica.play()

        

        #Preparar la ventana
        pygame.display.set_caption("Armar palabras con...")
        screen = pygame.display.set_mode((ANCHO, ALTO))
        myfont= pygame.font.SysFont("Calibri",50)

        
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
        dibujar(screen, letraPrincipal, letrasEnPantalla, candidata, puntos, segundos, palabrasAcertadas)       

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
                        if (esValida(letraPrincipal, letrasEnPantalla, candidata , diccionario, palabrasAcertadas) == True):
                            palabrasAcertadas.append(candidata) 
                            print(palabrasAcertadas)        
                        candidata = ""      
            segundos = TIEMPO_MAX - pygame.time.get_ticks()/1000

            #Dibujar de nuevo todo
            dibujar(screen, letraPrincipal, letrasEnPantalla, candidata, puntos, segundos, palabrasAcertadas)

            pygame.display.flip()

            #Crear botones
            """def pintar_botones(screen,boton,palabra):
                if boton.collidepoint(pygame.mouse.get_pos()):
                    pygame.draw.rect(screen,(235,232,52),boton,0)
                else:
                    pygame.draw.rect(screen,(5,227,23),boton,0)
                texto=myfont.render(palabra, True, (255,255,255)) #el nombre de lo que voy a poner
                screen.blit(texto, (boton.x+(boton.width-texto.get_width())/2,  #width establece el ancho de un elemento que en este caso es el texto
                boton.y+(boton.height-texto.get_height())/2)) #, get_width obtiene los pixeles de boton en eje x, get_height en y
            
            facil= Rect(1000,100,150,50) #hace rectangulo 1000 es el eje x 100 el eje y
            medio= Rect(1000,200,150,50)
            dificil= Rect(1000,300,150,50)
            
            pintar_botones(screen,facil,"Facil")
            pintar_botones(screen,medio,"Medio")
            pintar_botones(screen,dificil,"Dificil")

            if e.type == MOUSEBUTTONDOWN and e.button==1:
                    if facil.collidepoint(pygame.mouse.get_pos()):
                            screen.blit(imagen,[0,0])
                            segundos/2
                    if medio.collidepoint(pygame.mouse.get_pos()):
                            screen.blit(futuro,[0,0]) 
                    if dificil.collidepoint(pygame.mouse.get_pos()):
                            screen.blit(huawei,[0,0]) """
            
                
        while 1:
            #Esperar el QUIT del usuario
            for e in pygame.event.get():
                if e.type == QUIT:
                    pygame.quit()
                    return 
        
        

#Programa Principal ejecuta Main
if __name__ == "__main__":
    main()