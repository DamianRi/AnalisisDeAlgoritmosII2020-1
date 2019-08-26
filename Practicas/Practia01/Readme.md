##  Práctica 01
## Implementación de Gráficas y Ford Fulkerson

### Ventajas y Desventajas
#### Ventajas Matrices
  - Obtener los valores en cualquier dirección de la matriz es inmediato
  - Obtener los valores de la gráfica residual es más fácil
  
#### Desventajas Matrices
  - No se puede conocer los vecinos directos de cada vértice
  - El tamaño de la matriz es fijo
  - El tiempo para recorrer toda la matriz toma mucho tiempo
  
#### Ventajas Listas
  - La cantidad de elementos es dinámica
  - Es fácil conocer los vecinos directos de los vértices 
 
#### Desventajas Listas
  - El tiempo para obtener el valor de una arista toma tiempo lineal
  - Se debe crear otra lista de listas para obtner la gráfica residual
 

### Ejecución

NOTAS:
  - Se debe tener instalada la versión Python 3.6.8 como mínimo, ya que el programa fue desarrollado con este ( aunque al parecer también funciona con Python 2.7)
  - Deben instalarse los siguientes paquetes con el comando:

  Para Ubuntu
  ```
    $ sudo apt-get install python-numpy python-scipy python-matplotlib ipython ipython-notebook python-pandas python-sympy python-nose
  ```
  
  Para Mac
  ```
    $ sudo port install py35-numpy py35-scipy py35-matplotlib py35-ipython +notebook py35-pandas py35-sympy py35-nose  
  ```
  
  - Se debe instalar el siguiente paquete de para la gráficación (O en caso de no ver la gráficación, comentar la línea 5, 452, 462)
  ```
    $ pip install networkx
  ```
Un vez instalados los paquetes previamente señalados.
Dentro de la carpeta 'src' se encuentra el archivo 'Grafica.py', para correr el programa únicamente se debe ejecutar con el comando
```
  $ python Grafica.py
```


