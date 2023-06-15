from principal import *
from configuracion import *

import random
import math


def cargarListas(lista, listaIzq, listaMedio, listaDer, posicionesIzq , posicionesMedio, posicionesDer):
    #elije una palabra al azar y la divide en las tres columnas al azar
    palabra=random.choice(lista)
    divisionPalabra=random.randrange(0,len(palabra),1)
    newlen=len(palabra)-divisionPalabra
    divisionPalabra2=random.randrange(0,newlen,1)

    for letra in range(0,len(palabra)):

        #generan las cordenadas x para las letras de cada columna
        xListaIzq=random.randrange(20,260,20)
        xListaMed=random.randrange(280,520,20)
        xListaDer=random.randrange(540,780,20)
        y=0

        posicion=()

        #guarda la posicion en la lista de posciones correspondiente
        if(letra<divisionPalabra):
            listaIzq.append(palabra[letra])
            posicion=(xListaIzq,y)
            posicionesIzq.append(posicion)

        elif(letra<divisionPalabra2 and letra>=divisionPalabra):
            listaMedio.append(palabra[letra])
            posicion=(xListaMed,y)
            posicionesMedio.append(posicion)

        else:
            listaDer.append(palabra[letra])
            posicion=(xListaDer,y)
            posicionesDer.append(posicion)

    #elige una palabra de la lista y la carga en las 3 listas
    # y les inventa una posicion para que aparezca en la columna correspondiente

def bajar(lista, posiciones):
    for i in range(len(lista)-1,-1,-1): #hacemos un ciclo que recorra la columna
        posicion=posiciones[i] #asigno la coordenada de la primer letra de la lista
        posicionList=list(posicion) #las paso a variable de tipo lista para poder modificar la posicion
        posicionList[1]+=30 # acumulo la coordenada en posicion 1 (y) con 30 posiciones mas para que baje en la pantalla
        posicion=tuple(posicionList) # vuelvo a pasar la lista a tupla para que no se modifique
        posiciones[i]=posicion #reasigno la nueva coordenada de la letra en la columna
        if posicionList[1]>=530: # si la posicion "y" de la coordenada llega al piso
            lista.pop(i) #borro la letra
            posiciones.pop(i) #borro la posicion en que estaba la letra

    # hace bajar las letras y elimina las que tocan el piso

def actualizar(lista, listaIzq, listaMedio, listaDer, posicionesIzq , posicionesMedio, posicionesDer):
    #llama a la funcion bajar para hacer que todas las letars de cada columna bajen
    bajar(listaIzq,posicionesIzq)
    bajar(listaMedio,posicionesMedio)
    bajar(listaDer,posicionesDer)
    #llama a la funcion cargarListas para cargar nuevas letras cada vez que bajen las anteriores
    cargarListas(lista, listaIzq, listaMedio, listaDer, posicionesIzq , posicionesMedio, posicionesDer)

    ## llama a otras funciones para bajar las letras, eliminar las que tocan el piso y
    ## cargar nuevas letras a la pantalla (esto puede no hacerse todo el tiempo para que no se llene de letras la pantalla)

def estaCerca(elem, lista):
    #es opcional, se usa para evitar solapamientos
    pass

def Puntos(candidata):
    suma=0

    #verifica cuantas vocales hay en candidata, y por cada una suma un punto
    def vocalesP(candidata):
        puntos=0
        vocales= "aeiouAEIOU"
        for pos in range(len(candidata)):
             palabra=candidata[pos]
             for i in palabra:
                if i in vocales:
                    puntos+=1
        return puntos

    #verifica cuantas letras no son vocales, y por cada una suma dos puntos
    def consonantesP(candidata):
         puntos=0
         vocales= "aeiouAEIOU"
         for pos in range(len(candidata)):
             palabra=candidata[pos]
             for i in palabra:
                 if not i in vocales:
                     puntos+=2
         return puntos

    #verifica cuantas letars son consonantes dificiles, y por cada una suma 3 puntos
    def consonantesDificil(candidata):
         puntos=0
         consonantesDifi="jkqxyzJKQXYZ"
         for pos in range(len(candidata)):
             palabra=candidata[pos]
             for i in palabra:
                if i in consonantesDifi:
                    puntos+=3
         return puntos

    #suma todos los puntajes anteriores, retornando asi el puntaje de esa palabra
    suma=int(consonantesDificil(candidata))+int(consonantesP(candidata))+int(vocalesP(candidata))
    return suma

    #devuelve el puntaje que le corresponde a candidata

def procesar(lista, candidata, listaIzq, listaMedio, listaDerecha):
    # corrobora si la palabra que ingreso el usuario es valida o no y devuelve la cantidad de puntos
    if(esValida(lista,candidata,listaIzq,listaMedio,listaDerecha)):
        return Puntos(candidata)
    else:
        return 0

    #chequea que candidata sea correcta en cuyo caso devuelve el puntaje y 0 si no es correcta

def esValida(lista, candidata, listaIzq, listaMedio, listaDerecha):
    pos=0
    palabra=""
    micolumna=0
    mipantalla=[listaIzq,listaMedio,listaDerecha] #asigno todas las letras de la pantalla en una variable

    if(candidata not in lista):
        return False
    else:
        # si lo que ingreso el usuario esta en el lemario busco las letras en cada columna y si se
        #puede formar con las letras de la pantalla significa que es valido
        while micolumna<3 and pos<len(candidata):
            if(candidata[pos] not in mipantalla[micolumna]):
                    micolumna+=1
            else:
                palabra=palabra+candidata[pos]
                pos+=1
        if palabra==candidata:
            return True

    #devuelve True si candidata cumple con los requisitos




