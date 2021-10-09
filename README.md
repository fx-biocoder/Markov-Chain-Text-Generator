# Generador de texto mediante Cadenas de Markov

Este script facilita la generación automática de cadenas de texto de longitud variable, a partir de un archivo fuente con el cual se genera una cadena de Markov.
Para este proyecto he tomado como base el script del sitio personal de [Jeffrey Carpenter](https://www.linkedin.com/in/jeffcarp/), y realicé modificaciones varias.

### Highlights:
1. Uso de la librería `easygui` para seleccionar el archivo fuente de manera manual
   Esto permite seleccionar fácilmente el archivo fuente sin necesidad de escribir la ruta de archivo
2. Sintaxis más compacta y legible
3. Posibilidad de seleccionar el largo y número de sentencias generadas

### ¿Qué es una cadena de Markov?
    
>*Una cadena de Markov es un sistema en un tiempo discreto, que en cada instante se encuentra en un estado distinto. La cantidad total de estados es finita, y en cada instante se pasa de un estado a otro con unas probabilidades fijas que dependen sólo del estado actual, y no del resto de la historia del sistema.*
>**Definición extraída del sitio web de la [Universidad Autónoma de Madrid](http://matematicas.uam.es/~pablo.angulo/markov/markov.html#definicion-de-cadena-de-markov).**

Pueden probar este script usando el archivo "stallman_copypasta.txt" presente en este mismo repositorio.
