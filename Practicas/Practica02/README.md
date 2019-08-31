### Práctica 2: Algoritmo de etiquetamiento
- - -
##### Descripción
En está práctica se llevo a cabo la implementación del Algoritmo de Etiquetamiento sobre una gráfica con 
estructura de matriz de adyacencia.

La matriz que hacer representación de la gráfica, en un inicio se hace una matriz **diagonal superior** la cual 
sería la **matriz incial**, mientras que al terminar el algoritmo se muestra la **matriz residual** como la parte 
**diagonal inferior** de la misma matriz inicial.

##### Ejecución
* * * 
NOTAS: 
+ Para poder correr el código en python es necesario usar la versión de Python 2.7

+ Tener instalado el paquete <numpy> se puede instalar con el siguiente comando via <pip> python 2.7:
```
	$ python -m pip install --user numpy
```
* * *

Una vez instalado el paquete requerido, dentro de la carpeta <src> se ecuentra el código 
<AlgoritmoEtiquetamiento.py> el cual se corre con el siguiente comando:
```
	$ python AlgoritmoEtiquetamiento.py
```

###### Uso

Una vez que el código sea iniciado, se solicita una valor numérico para ingresar. El cual hace referencia al 
número de vértices que tendrá la gráfica, la cual se genera con valores aleatorios de entre 0 a 100.

Ejemplo:
```
	Ingresa un número de nodos para la gráfica (matriz de adyacencias) : 10
```
 Y se genera una muestra de la matriz inicial así como el trazo de cada ruta y su flujo total sobre la matriz
