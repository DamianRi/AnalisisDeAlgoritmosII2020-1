## Práctica 04: Colas Binomiales

### Descripción
Implementación de una estructura de datos de colas binomiales en Python (versión 3.7.3). Cada elemento de la estructura lo denominaremos como **heap**, el cual tendrá las 
siguientes propiedades:
| Propiedad  |
| - - - |
| 1. Padre  |
| 2. Llave  |
| 3. Grado  |
| 4. Hijos  |
| 5. Siguiente Hermano  |

A continuación describimos cada propiedad:

	1. Padre : int, número entero, referencia al heap que tiene como padre el heap.
	2. Llave : int, el valor que contiene el heap
	3. Grado : int, grado que tiene el heap, en caso de ser la raíz indica el índice k del heap B<sub>k</sub>
	4. Hijos : list, lista de los elementos de heaps que tienen como raíz al heap.
	5. Siguiente hermano : int, referencia al siguiente nodo raíz

Se tiene la implementación de las siguientes funciones sobre las estructuras:

	1. Insertar(x, T) : donde x es un elemento (int) a insertar en la colección de datos Q
	2. Fundir(T, Q) : mezclar todos los datos de T con los datos de Q, dejándolos en Q.

### Contenido




### Ejecución

 

	
