#   1 - librerías necesarias para el proyecto
#from tkinter.constants import FALSE, TRUE
import easygui as eg, numpy as np, random, re
from collections import defaultdict

#   2 - Selección del archivo fuente a partir del cual se crea el Modelo de Markov
#       La precisión del modelo aumenta con el tamaño de la entrada de texto suministrada,
#       por eso es conveniente usar un texto lo más largo posible
directorio = eg.fileopenbox()
with open(directorio, encoding = "utf8") as archivo:  # IMPORTANTE! Chequear encoding del archivo fuente
    texto = archivo.read()

#   3 - Se hace un split de las palabras contenidas en el archivo fuente
#       Posteriormente se crea un diccionario a partir de dichas palabras
regex_split = [palabra for palabra in re.split("\W+", texto) if palabra != ""]
markov = defaultdict(lambda: defaultdict(int))

ultima_palabra = regex_split[0].lower()

for palabra in regex_split[1:]:
    palabra = palabra.lower()
    markov[ultima_palabra][palabra] += 1
    ultima_palabra = palabra

#   4 - Función para desplazarse sobre la cadena de Markov
#       Donde "grafo" corresponde a la cadena, "distancia" corresponde a
#       la longitud del desplazamiento sobre la cadena (esto es, la cantidad de
#       palabras en la sentencia a formar), y "nodo_de_inicio" corresponde al
#       sitio de la cadena a tomar como semilla
def lista(grafo, distancia, nodo_de_inicio = None):
    if distancia <= 0:
        return []
    if not nodo_de_inicio:
        nodo_de_inicio = random.choice(list(grafo.keys()))  #   Se toma un nodo aleatorio
    
    pesos = np.array(list(markov[nodo_de_inicio].values()), dtype = np.float64)
    pesos /= pesos.sum()    # Normalización
    opciones = list(markov[nodo_de_inicio].keys())
    palabra_elegida = np.random.choice(opciones, None, p = pesos)
  
    return [palabra_elegida] + lista(grafo, distancia = distancia - 1, nodo_de_inicio = palabra_elegida)

#   5 - Generación de cadenas de texto 
#       Los inputos de distancia y rango son validados mediante regex y convertidos a enteros
dist = input("Inserte valor de distancia: ")
rango = input("Inserte valor de rango: ")

if(re.search("[0-9]+", dist) and re.search("[0-9]+", rango)):
    dist = int(dist)
    rango = int(rango)   
    [print(' '.join(lista(markov, distancia = dist))) for i in range(rango)]
else:
    input("Valor/es inválido/s. Pulse cualquier tecla para finalizar el programa...")