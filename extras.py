import pygame
from pygame.locals import *
from configuracion import *

def dame_letra_apretada(key):
    if key == K_a:
        return("a")
    elif key == K_b:
        return("b")
    elif key == K_c:
        return("c")
    elif key == K_d:
        return("d")
    elif key == K_e:
        return("e")
    elif key == K_f:
        return("f")
    elif key == K_g:
        return("g")
    elif key == K_h:
        return("h")
    elif key == K_i:
        return("i")
    elif key == K_j:
        return("j")
    elif key == K_k:
        return("k")
    elif key == K_l:
        return("l")
    elif key == K_m:
        return("m")
    elif key == K_n:
        return("n")
    elif key == K_o:
        return("o")
    elif key == K_p:
        return("p")
    elif key == K_q:
        return("q")
    elif key == K_r:
        return("r")
    elif key == K_s:
        return("s")
    elif key == K_t:
        return("t")
    elif key == K_u:
        return("u")
    elif key == K_v:
        return("v")
    elif key == K_w:
        return("w")
    elif key == K_x:
        return("x")
    elif key == K_y:
        return("y")
    elif key == K_z:
        return("z")
    elif key == K_1:
        return("1")
    elif key == K_2:
        return("2")
    elif key == K_3:
        return("3")
    elif key == K_SPACE:
        return(" ")
    else:
        return("")

def dibujar(screen, letra_principal, letras_en_pantalla, candidata, puntos, segundos , palabras_acertadas, seleccion_dificultad):
    #Configuración de las fuentes
    defaultFont= pygame.font.Font( pygame.font.get_default_font(), 30)
    defaultFont2= pygame.font.Font( pygame.font.get_default_font(), 20)
    defaultFontGrande= pygame.font.Font( pygame.font.get_default_font(), 80)

    pos_x_acertadas = 10
    pos_y_acertadas= 100
        
    #Linea del piso
    pygame.draw.line(screen, (255,255,255), (0, ALTO-70) , (ANCHO, ALTO-70), 5)

    ren1 = defaultFont.render(candidata, 1, COLOR_TEXTO)
    ren2 = defaultFont.render("Puntos: " + str(puntos), 1, COLOR_TEXTO)
    ren4 = defaultFont2.render("palabras acertadas: ", 1, COLOR_TEXTO)
    if seleccion_dificultad == False:
        ren0 = defaultFont.render("seleccione dificultad: " , 1 , COLOR_TEXTO)
        screen.blit(ren0,(500,100))

    """Recorremos la lista de palabras_acertadas una por una y la vamos mostrando en
    pantalla mientras que vamos moviendo la posición para que queden enlistadas
    una debajo de la otra"""
    if seleccion_dificultad == True: 
        for i in palabras_acertadas:
            ren5 = defaultFont2.render(i, 1, COLOR_TEXTO)
            palabras_acertadas.sort()
            screen.blit(ren5 , (pos_x_acertadas,pos_y_acertadas))
            pos_y_acertadas += 20

        if(segundos<15):
            ren3 = defaultFont.render("Tiempo: " + str(int(segundos)), 1, COLOR_TIEMPO_FINAL)
        else:
            ren3 = defaultFont.render("Tiempo: " + str(int(segundos)), 1, COLOR_TEXTO)
        
        #escribe grande la palabra (letra por letra) y la letra principal de otro color
        pos = 380 #posición en x de las letras
        for i in range(len(letras_en_pantalla)):
            if letras_en_pantalla[i] == letra_principal:
                screen.blit(defaultFontGrande.render(letras_en_pantalla[i], 1, COLOR_TIEMPO_FINAL), (pos, 130))
            else:
                screen.blit(defaultFontGrande.render(letras_en_pantalla[i], 1, COLOR_LETRAS), (pos, 130))
            pos = pos + TAMANNO_LETRA_GRANDE

                
        screen.blit(ren1, (500, 670))
        screen.blit(ren2, (1100, 10))
        screen.blit(ren3, (10, 10))
        screen.blit(ren4, (pos_x_acertadas , 80))
        