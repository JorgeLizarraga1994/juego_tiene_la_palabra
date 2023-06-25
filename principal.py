#! /usr/bin/env python
import os, random, sys, math

import pygame
from pygame.locals import *

from configuracion import *
from funcionesVACIAS import *
from extras import *


#Funcion principal
def main():
    
        TIEMPO_MAX = 60
        seleccion_dificultad = False
        # Establecer la codificación en UTF-8
        sys.stdout.reconfigure(encoding='utf-8')
        #Centrar la ventana y despues inicializar pygame
        os.environ["SDL_VIDEO_CENTERED"] = "1"
        pygame.init()
        pygame.mixer.init()

        #fondo
        imagen_fondo = pygame.image.load("assets/imagenes/espacio.jpg")
        futuro=pygame.image.load("assets/imagenes/futuro.jpg")
        huawei=pygame.image.load("assets/imagenes/huawei.jpg")
        imagen2=pygame.image.load("assets/imagenes/fondo.jpg")
        #sonidos
        sonido_correcto = pygame.mixer.Sound("assets/sonidos/correct-ding.mp3")
        sonido_error = pygame.mixer.Sound("assets/sonidos/Error.mp3")
        #musica
        #musica = pygame.mixer.Sound("assets/sonidos/musica.mp3")
        #musica.play()
        
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
        palabras_acertadas = []
        
        
        facil= Rect(600,200,150,50) #hace rectangulo 1000 es el eje x 100 el eje y
        medio= Rect(600,300,150,50)
        dificil= Rect(600,400,150,50)
        #Crear botones
        def pintar_botones(screen,boton,palabra):
                if boton.collidepoint(pygame.mouse.get_pos()):
                    pygame.draw.rect(screen,(235,232,52),boton,0)
                else:
                    pygame.draw.rect(screen,(5,227,23),boton,0)
                texto=myfont.render(palabra, True, (255,255,255)) #el nombre de lo que voy a poner
                screen.blit(texto, (boton.x+(boton.width-texto.get_width())/2,  #width establece el ancho de un elemento que en este caso es el texto
                boton.y+(boton.height-texto.get_height())/2)) #, get_width obtiene los pixeles de boton en eje x, get_height en y
            

        
        #lee el diccionario
        lectura(diccionario)

        #elige las 7 letras al azar y una de ellas como principal
        letras_en_pantalla = dame_7_letras()
        letra_principal = dame_letra(letras_en_pantalla)

        #se queda con 7 letras que permitan armar muchas palabras, evita que el juego sea aburrido
        while(len(dame_algunas_correctas(letra_principal, letras_en_pantalla, diccionario, palabras_acertadas))< MINIMO):
            letras_en_pantalla = dame_7_letras()
            letra_principal = dame_letra(letras_en_pantalla)

        print(dame_algunas_correctas(letra_principal, letras_en_pantalla, diccionario, palabras_acertadas))
        #dibuja la pantalla la primera vez
        dibujar(screen, letra_principal, letras_en_pantalla, candidata, puntos, segundos, palabras_acertadas, seleccion_dificultad)
        
        
        while segundos > fps/1000:
            if seleccion_dificultad == False:
                pintar_botones(screen,facil,"Facil")
                pintar_botones(screen,medio,"Medio")
                pintar_botones(screen,dificil,"Dificil") 
            if True:
                fps = 3000
            #Buscar la tecla apretada del modulo de eventos de pygame
            for e in pygame.event.get():
                if e.type == MOUSEBUTTONDOWN and e.button==1:
                    if facil.collidepoint(pygame.mouse.get_pos()):
                        imagen_fondo = futuro
                        TIEMPO_MAX = 60
                        seleccion_dificultad = True
                    if medio.collidepoint(pygame.mouse.get_pos()):
                        imagen_fondo = imagen2
                        TIEMPO_MAX = 40
                        seleccion_dificultad = True
                    if dificil.collidepoint(pygame.mouse.get_pos()):
                        imagen_fondo = huawei
                        TIEMPO_MAX = 20
                        seleccion_dificultad = True
                #QUIT es apretar la X en la ventana
                if e.type == QUIT:
                    pygame.quit()
                    return()
                if seleccion_dificultad == True:
                    # 1 frame cada 1/fps segundos
                    gameClock.tick(fps)
                    totaltime += gameClock.get_time()
                    screen.blit(imagen_fondo,[0,0])
                    segundos = TIEMPO_MAX - pygame.time.get_ticks()/1000
                    #Ver si fue apretada alguna tecla
                    if e.type == KEYDOWN:
                        letra = dame_letra_apretada(e.key)
                        candidata += letra   #va concatenando las letras que escribe
                        if e.key == K_BACKSPACE:
                            candidata = candidata[0:len(candidata)-1] #borra la ultima
                        if e.key == K_RETURN:  #presionó enter
                            puntos += procesar(letra_principal, letras_en_pantalla, candidata, diccionario , palabras_acertadas)
                            
                            #Verificamos el numero que retorna la función procesar y dependiendo de eso emitimos un sonido
                            if (procesar(letra_principal, letras_en_pantalla , candidata, diccionario, palabras_acertadas) > 0):
                                sonido_correcto.play()
                            else:
                                sonido_error.play()
                            #Verificamos si la palabra candidata es valida, si es valida la guardamos en la lista de palabras_acertadas   
                            if (es_valida(letra_principal, letras_en_pantalla, candidata , diccionario, palabras_acertadas) == True):
                                palabras_acertadas.append(candidata)        
                            candidata = ""
            
            
            
            
            
            #Dibujar de nuevo todo
            dibujar(screen, letra_principal, letras_en_pantalla, candidata, puntos, segundos, palabras_acertadas,seleccion_dificultad)

            pygame.display.flip()
            screen.blit(imagen_fondo,[0,0])
        while 1:
            #Esperar el QUIT del usuario
            for e in pygame.event.get():
                if e.type == QUIT:
                    pygame.quit()
                    return
                
        

#Programa Principal ejecuta Main
if __name__ == "__main__":
    main()