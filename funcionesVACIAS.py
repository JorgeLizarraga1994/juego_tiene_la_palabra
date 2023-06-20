from principal import *
from configuracion import *
import random
import math

#lee el archivo y carga en la lista diccionario todas las palabras
#la función open necesita un close, al utilizar with el close queda explicito
#agregamos el encoding, ya que teniamos un error de codificación de utf-8
def lectura(diccionario):
    archivo= open("lemario.txt","r" , encoding = "utf-8")
    for linea in archivo.readlines():
        diccionario.append(linea[0:-1])
    return diccionario

#Devuelve una cadena de 7 caracteres sin repetir con 2 o 3 vocales y a lo sumo
# con una consonante dificil (kxyz)
def no_repite(letra, cadena):
    if letra not in cadena:
        return True
#cambie el while por el for, ya que el for si encontraba una  repetida me
#dejaba la cadena en 3 caracteres
def dame7Letras():
    consonantes ="bcdfghjlmnpqrstvw"
    vocales = "aeiou"
    c_dificil = "kxyz"
    nueva = "" 
    i = 0
    o = 0
    while i < 4:
        for letra in random.choice(consonantes):
            if no_repite(letra , nueva):
                nueva = nueva + letra
                i += 1
                
    while o < 2:
        for vocal in random.choice(vocales):
            if no_repite(vocal, nueva):
                nueva = nueva + vocal
                o += 1
        
    for letra_dificil in random.choice(c_dificil):
        if no_repite(letra_dificil , nueva):
            nueva = nueva + letra_dificil

    return nueva


#elige una letra de las letras en pantalla
def dameLetra(letrasEnPantalla):
    for letra in random.choice(letrasEnPantalla):
        return letra

#si es valida la palabra devuelve puntos sino resta.
def procesar(letraPrincipal, letrasEnPantalla, candidata, diccionario):
    if esValida(letraPrincipal , letrasEnPantalla, candidata ,diccionario):
        return Puntos(candidata)
    return -1



#chequea que se use la letra principal, solo use letras de la pantalla y
#exista en el diccionario
def esValida(letraPrincipal, letrasEnPantalla, candidata, diccionario):
    cont = 0
    for letra in letrasEnPantalla:
        if letra == letraPrincipal:
            cont +=1
    
    for char in candidata:
        if char == letraPrincipal:
            cont +=1     
    
    for palabra in diccionario:
        if palabra == candidata:
            cont +=1
            
    if cont == 3:
        return True         
        

#devuelve los puntos
def Puntos(candidata):
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
def dameAlgunasCorrectas(letraPrincipal, letrasEnPantalla, diccionario):
    listaAlgunasCorrectas = []
    for palabras in diccionario:
        if letraPrincipal in palabras:
            listaAlgunasCorrectas.append(palabras)
    return listaAlgunasCorrectas


