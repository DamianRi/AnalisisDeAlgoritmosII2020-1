## Práctica 04: Colas Binomiales

---
**NOTA:** 

Se debera tener instalada la versión de Python 3.7.4 para su correcto funcionamiento, ya que fue la versión en la cual se realizaron las pruebas 

---
---
**_Nota 2 (Opcional):_**

Se pueden descomentar las líneas 284,287, y 306,309 para ver los atributos de cada Heap en toda la estructura

---



### Descripción
Implementación de una estructura de datos de colas binomiales en Python (versión 3.7.3). Cada elemento de la estructura lo denominaremos como **heap**, el cual tendrá las 
siguientes propiedades:

| Propiedades	|
| -----------	|
| 1. Padre	|
| 2. Llave	|
| 3. Grado	|
| 4. Hijos	|
| 5. S_Hrn	|

A continuación describimos cada propiedad de los **Heap's**:

	1. Padre : int, número entero, referencia al heap que tiene como padre el heap.
	2. Llave : int, el valor que contiene el heap
	3. Grado : int, grado que tiene el heap, en caso de ser la raíz indica el índice K del heap BK
	4. Hijos : list, lista de los elementos de heaps que tienen como raíz al heap.
	5. S_Hrn : int, referencia al siguiente nodo raíz

Se tiene la implementación de las siguientes funciones sobre la **Cola Binomial**:

	1. Insertar(x, T) : Agrega el dato x en la colecci ́on de datos Q. 
	2. Fundir(T, Q) : Mezcla todos los datos de T con los datos de Q dej ́andolosen Q.
	3. Eliminar Mínimo(T) : Elimina el Heap con LLAVE mínima global 

### Contenido
La carpeta tiene la siguiente estructura:
- [DamianRivera]()
	- [src](/src)
		- [Colas_Binomiales.py](/src/Colas_Binomiales.py)
	- [README.md](README.md)

El archivo principal es **Colas_Binomiales.py**. El cual contiene la implementación de _Colas Binomiales_ en Python (Version 3.7.4). Además de varios métodos auxiliares para que la implementación funcione, los principales son:

 1. **def insertar(self, nuevo_elemento)**: dado un entero, si este aun no está en los Heap's actuales, crea un nuevo Heap y lo agrega en la estructura, en este mismo método se manda a llamar el método fundir para hacer la organización de los BK's
 2. **def fundir(self, bk1, bk2)**: recibe dos raices Heap, la raíz de cada BK (del mismo rango) para raorganizar las raices y su posición en el arreglo de Heaps de la Cola Binomial, actualizando además los valores de cada raíz.
 3. **def eliminar_minimo_global(self)**: primero se encuentra el índice de la raíz con _llave_ menor de todas las raices actuales, y se elimina este heap, reinsertando los Heap's que tenía como hijos 

El el método **main** se tiene la funcionalidad del programa. Tienen nos maneras de uso que se explican en la sección de **Ejecución**


### Ejecución
La salida del programa consta de cuatro partes:
 
 1. Muestra un resumen con lo que trabajará, la lista de elementos que se agregará, cuantos elementos son y los BK's necesarios para guardar esos elementos en el arreglo. Por ejemplo: 111 significa que se necesita un B0, B1, B2. 100101 significa que se necesitan un B0, B3, B5.
 2. Muestra la formación de los BK's que se necesitaron, imprimiendolo en el formato **_Llave(Hijos)_** para cada Heap del BK. Cada "dos puntos" (..) hace la separación de cada Heap
 3. Muestra que se se eliminará el mínimo global. Imprime la llave del heap mínimo global, la raíz del heap correspondiente, y hace énfasis en que ha eliminado el elemento
 4. Muestra la impresión de los BK's luego de haber eliminado el mínimo global
 
Hay dos formas para ejecutar el programa. Para esto suponemos estar colocados en una terminal dentro de la carpeta _src_.
##### Primera Forma
Ejecutar el siguiente comando. El cual ejecuta el programa generando una lista de longitud entre 1, 20 elementos con números aleatorios enteros den entre 1 a 100
```
	$ python3 Colas_Binomiales.py
```
Por ejemplo:
```
	python3 src/Colas_Binomiales.py   

	< COLAS BINOMIALES >

	Elementos a agregar:  [86, 13, 46, 39, 96, 49, 0, 69, 90] 
	Número de elementos:  9 
	BK's necesarios:  1001

	= BK's EN LA C.B. =
	B0: 90[]
	B3: 0[69, 49, 13]..13[86, 39]..39[46]..46[]..86[]..49[96]..96[]..69[]

	- ELIMINAR MÍNIMO GLOBAL
	Mínimo Global: 0 Indice Heap: B3
	Se eliminó la raíz del B3 Lave: 0

	= BK's EN LA C.B. =
	B3: 13[86, 39, 49]..49[96, 69]..69[90]..90[]..96[]..39[46]..46[]..86[]
```
##### Segunda Forma
Ejecutar el siguiente comando. El cual ejercuta el programa esperando como entrada por el usuario una lista de números enteros separados por una coma. 
```
	$ python3 Colas_Binomiales.py -m
```
Por ejemplo: 
```
	$ python3 Colas_Binomiales.py -m
	
 	 < COLAS BINOMIALES >
	Ingresa los elementos para agregar (enteros separados por una ','[coma]):  8, 4, 1, 3, 6, 9, 15
	
	Elementos a agregar:  [8, 4, 1, 3, 6, 9, 15] 
	Número de elementos:  7 
	BK's necesarios:  111

	= BK's EN LA C.B. =
	B0: 15[]
	B1: 6[9]..9[]
	B2: 1[3, 4]..4[8]..8[]..3[]

 	- ELIMINAR MÍNIMO GLOBAL
	Mínimo Global: 1 Indice Heap: B2
	Se eliminó la raíz del B2 Lave: 1

	= BK's EN LA C.B. =
	B1: 3[15]..15[]
	B2: 4[8, 6]..6[9]..9[]..8[]
```