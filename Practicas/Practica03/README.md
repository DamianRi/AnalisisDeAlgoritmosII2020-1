## Práctica 3: Algoritmo de capacidades escalables

#### Descripción
Se hizo una implementación del **Algoritmo de Capacidades Escalables**, sobre gráficas con represencación de 
matriz de adyacencias; las cuales en un inicio tiene únicamente valores en su diagonal superior, con lo cual todas las 
aristas de la gráfica van "hacia a delante". Las gráficas que se generan de manera aleatoria, tienen por nombre 
un valor numérico, del cual se enviará flujo de un nodo origen a un nodo destino (Siempre se tomará como nodo origen 
al nodo '0', y nodo destino 'n-1')


#### Contenido
Dentro de la carpeta **src** se encuentra el archivo **Algoritmo_Capacidades_E.py**. El cual contiene la
implementación del **Algoritmo de Capacidades Escalables** en Python, versión 2.7. El programa inicia
esperando un número entero como entrada, para así generar una gráfica, creando una matriz cuadrada de *n x n*
con valores aleatorios en las aristas entre los nodos.

#### Ejecución
* * * 
NOTAS: 
+ Para poder correr el código en python es necesario usar la versión de Python 2.7

+ Tener instalado el paquete <numpy> se puede instalar con el siguiente comando via <pip> python 2.7:
```
	$ python -m pip install --user numpy
```
* * *

Basta con abrir una terminal de preferencia, posicionarse dentro de la carpeta **src** y ejecutar el código 
con el siguiente comando:

```
	$ python Algoritmo_Capacidades_E.py
```

Luego de ello inicia el programa, esperando como entra un número entero que hará referencia a la cantidad de 
nodos que contiene la gráfica.

Ejemplo:
```
	= = = ALGORITMO DE CAPACIDADES ESCALABLES = = = 
	 > Ingresa un número de nodos para la gráfica (matriz de adyacencias) : 5
```

Con lo cual inicia el programa, generando el despliegue de la impresión de cada matriz con su modificación y 
su ruta aumentante tomada en dado caso de enviar flujo a través de ella.

El programa termina mostrando la matriz original residual y el flujo total que se envió del nodo origen al nodo destino.
