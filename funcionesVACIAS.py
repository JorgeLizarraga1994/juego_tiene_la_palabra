from principal import *
from configuracion import *
import random
import math


"""lee el archivo y carga en la lista diccionario todas las palabras
la función open necesita un close, al utilizar with el close queda explicito
agregamos el encoding, para que nos reconozca los caracteres especiales del idioma español"""
def lectura(diccionario):
    with open('lemario.txt', 'r',  encoding='utf-8') as archivo:
        for linea in archivo.readlines():
            diccionario.append(linea[0:-1])
        return diccionario

#si la variable x no se encuentra en la cadena o lista ingresada nos arroja true
def no_repite(x, cadena):
    if x not in cadena:
        return True

#devuelve 4 letras de la cadena CONSONANTES         
def dame_4(nueva,CONSONANTES):
        i = 0
        while i < 4:
            for letra in random.choice(CONSONANTES):
                if no_repite(letra , nueva):
                    nueva = nueva + letra
                    i += 1
        return nueva

#devuelve 2 letras de la cadena VOCALES        
def dame_2(nueva,VOCALES):
    o = 0
    while o < 2:
        for vocal in random.choice(VOCALES):
            if no_repite(vocal, nueva):
                nueva = nueva + vocal
                
                o += 1
    return nueva

#devuelve una letra de la cadena C_DIFICIL    
def dame_1_dificil(nueva, C_DIFICIL):
    for letra_dificil in random.choice(C_DIFICIL):
        if no_repite(letra_dificil , nueva):
            nueva = nueva + letra_dificil 
            
    return nueva
#desordena una cadena     
def desordenar_cadena(nueva, desordenada):
    u = 0
    while u < 7:
        for i in random.choice(nueva):
            if no_repite(i , desordenada):
                desordenada = desordenada + i 
                u += 1
    return desordenada

#Devuelve una cadena de 7 caracteres sin repetir con 2 o 3 VOCALES y a lo sumo
# con una consonante dificil (kxyz)
def dame_7_letras():
    CONSONANTES ="bcdfghjlmnpqrstvw"
    VOCALES = "aeiou"
    C_DIFICIL = "kxyz"
    nueva = "" 
    desordenada = ""

    nueva = dame_4(nueva,CONSONANTES) 
    nueva += dame_2(nueva ,VOCALES)  
    nueva += dame_1_dificil(nueva,C_DIFICIL)
    desordenada = desordenar_cadena(nueva, desordenada)

    return desordenada

#elige una letra de las letras en pantalla
def dame_letra(letras_en_pantalla):
    for letra in random.choice(letras_en_pantalla):
        return letra

#si es valida la palabra devuelve puntos sino resta.
def procesar(letra_principal, letras_en_pantalla, candidata, diccionario , palabras_acertadas):
    if no_repite(candidata , palabras_acertadas):
        if es_valida(letra_principal , letras_en_pantalla, candidata ,diccionario , palabras_acertadas):
            return Puntos(candidata)
        else:
            return -1
    return 0

"""chequea que se use la letra principal, solo use letras de la pantalla y
exista en el diccionario"""
def es_valida(letra_principal, letras_en_pantalla, candidata, diccionario , palabras_acertadas):
    
    # Verifica si la letra principal está en las letras disponibles en la pantalla
    if letra_principal not in letras_en_pantalla:
        return False
    
    # Verifica si todas las letras de la palabra candidata están presentes en las letras disponibles en la pantalla
    for letra in candidata:
        if letra not in letras_en_pantalla:
            return False
    
    # Verifica si la palabra candidata contiene la letra principal
    if letra_principal not in candidata:
        return False
    
    # Verifica si la palabra candidata está en el diccionario
    if candidata not in diccionario:
        return False
    
    # Verifica si la palabra candidata ya ha sido ingresada previamente
    if candidata in palabras_acertadas:
        return False
    
    # Verifica si la cantidad de letras de la palabra es menor a 3
    if len(candidata) < 3:
        return False
    
    # Si pasa todas las verificaciones anteriores, la palabra es válida
    return True    
        

#devuelve los puntos
def Puntos(candidata):
    if len(candidata) < 3:
        return 0
    if len(candidata) == 3:
        return 1
    elif len(candidata) == 4:
        return 2
    elif len(candidata) >= 5 and len(candidata) < 7:
        return (len(candidata))
    elif len(candidata) >=8:
        return (len(candidata))
    elif len(candidata) == 7:
        return 10

#busca en el diccionario palabras correctas y devuelve una lista de estas
def dame_algunas_correctas(letra_principal, letras_en_pantalla, diccionario, palabras_acertadas):
    lista_algunas_correctas = []
    for palabras in diccionario:
        if es_valida(letra_principal, letras_en_pantalla, palabras, diccionario , palabras_acertadas):
            lista_algunas_correctas.append(palabras)
    return lista_algunas_correctas


