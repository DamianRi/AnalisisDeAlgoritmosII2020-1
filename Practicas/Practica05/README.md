## Práctica 05: Fibonacci Heaps

---
**NOTA:**
El código fue desarrollado en Python 3.7.5(versión que se tiene por defecto Kubuntu), así que se recomienda tener instalada al menos esa versión del lenguaje.

---

### Descripción
Implementación de la estructura de datos Fibonacci Heaps. Con sus funciones principales:

+ Inserta
+ Funde
+ Encuentra Min
+ Link
+ Borra Min
+ Decrementa Llave
+ Corte en Cascada
+ Elimina

La forma en que se hace la impresión de los árboles heaps es **Lave(HermanoAnterior, HermanoSiguiente)[Lista de Hijos]** Ejemplo **6(6,6)[30,18,12,9]** donde sería el nodo 6, sin hermanos e hijos 30,18,12,9. Cuando un Nodo está marcado se indica con un asterísco (*) luego de su llave. Se muestra un caso en la generación de los árboles luego de la acción _>>>>>  DECREMENTANDO 48-7=41_ para el nodo **42**:

```
    ...
    >>>>>    DECRETEMENTANDO  48 - 7 = 41

        == Árboles en F-Heap ==
    B4: 6(41,41)[30, 18, 12, 9] ..9(12,30)[] ..12(18,9)[15] ..15(15,15)[] ..18(30,12)[24, 21] ..21(24,24)[] ..24(21,21)[27] ..27(27,27)[] ..30(9,18)[42, 36, 33] ..33(36,42)[] ..36(42,33)[39] ..39(39,39)[] ..42*(33,36)[45] ..45(45,45)[] 
    B1: 41(6,6)[51] ..51(51,51)[]
    ...
```

### Contenido
La carpeta tiene la siguiente estructura:
- [DamianRivera]()
	- [src](src/)
		- [Fibonacci_Heap.py](src/Fibonacci_Heap.py)
    - [img](img/)
        - [fibo-heaps.png](img/fibo-heaps.png)
	- [README.md](README.md)

El código principal se encuentra en el archivo **Fibonacci_Heap.py**. Dentro de la Carpeta *__img__* se encuentra una imagen del programa ejecutado en terminal.

### Ejecución
El método **main** del programa realiza la llamada de las funciones principales sobre una estrucutra de F-Heaps, con el fin de mostrar el funcionamiento de cada una de ellas.

Para ver el funcionamiento en la terminal basta con estar posicionado dentro de la carpeta **[src](src/)** y ejecutar el siguiente comando:
```
    .../src$ python3 Fibonacci_Heap.py
```

Cada que se hace una modificación sobre los árboles, se imprime **== Árboles en F-Heap ==**, para cada función que se manda a llamar se muestra iniciando con **>>>>>** y el nombre de la acción. Las funciones **Inserta, Funde, Link, Corte en Cascada** están implicitas dentro de la adición de elementos al inicio del programa así como en la reorganización de los nodos al eliminar el elemento mínimo y al decrementar llave (para el caso de Decrementar Llave). Las funciones **Encuentra Min, Borra Min, Decrementa Llave, Elimina** se imprime su llamada de manera explicita.
