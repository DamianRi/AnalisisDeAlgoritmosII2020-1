#! usr/bin/python3
# -*- coding: utf-8 -*-

import random

'''
    Clase para hacer la representación de cada objeto Heap
'''
class Heap:
    
    def __init__(self, llave):
        self.padre = None
        self.llave = llave
        self.marcado = False
        self.hijo = None
        self.grado = 0
        self.s_hrn = llave  # Su siguiente hermano es el mismo
        self.p_hrn = llave  # Su previo hermano es el mismo

    def toString(self):
        print(
            "- - - - - - - -",
            "\nPadre:\t\t"+str(self.padre),
            "\nLave:\t\t"+str(self.llave),
            "\nMarcado:\t"+str(self.marcado),
            "\nGrado:\t\t"+str(self.grado),
            "\nHijo:\t\t"+str(self.hijo),
            "\nS Hrn:\t\t"+str(self.s_hrn),
            "\nP Hrn:\t\t"+str(self.p_hrn),
            "\n- - - - - - - -")

    def shortToString(self):
        info =  "[P:"+str(self.padre)+"|LL:"+str(self.llave)+"|SH:"+str(self.s_hrn)+"|PH:"+str(self.p_hrn)+"|M:"+str(self.marcado)+"]"
        return info

'''
    Clase para hacer la representación de una estructura Fibonacci Heap
    que tiene como elementos objetos de tipo Heap
'''
class Fibonacci_Heap:

    '''
        Constructor para una Fibonacci Heap nueva vacía
    '''
    def __init__(self):
        self.elementos_heap = {}
        self.elemento_minimo = None


    '''
        Constructor para una Fibonacci Heap dada una lista de elementos
    '''
    def __init__(self, lista_elementos):
        
        self.elementos_heap = {}    # Diccionario para guardar los Heaps de toda la estructura
        self.elemento_minimo = None

        # Resumen de los valores que tiene la Cola Binomal al creala
        print("\nElementos a agregar: ",
            lista_elementos,
            "\nNúmero de elementos: ",
            len(lista_elementos))

        for e in lista_elementos:   # Creamos los heaps para cada elemento de la lista de elementos            
            self.insertar(e)    # Insertamos cada elemento de la lista
            

    '''
        Método que regresa el índice del siguiente Bk al índice del bk 
        que se da como parametro
    '''
    def siguiente_bk(self, indice):
        pass

    '''
        Imprime todos los elementos como HEAP dentro de la estructura
    '''
    def imprime_elementos_heap(self):
        for e in self.elementos_heap:
            self.elementos_heap[e].toString()

    '''
        Método que regresa los elementos que están debajo de un Heap
        @param bk - heap raíz del bk
    '''
    def elementos_en_bk(self, bk):
        stack = []  # lista para ir recorriendo todo el bk
        stack.append(bk.llave)    # agregamos el bk raíz
        
        lista = []  # lista de elementos en bk
        while len(stack) != 0:    # mientras que haya elementos
            actual = stack.pop()    #   tomamos el tope de la lista elementos
            lista.append(actual)  #   agregamos la llave a la lista

            hijo_actual = self.elementos_heap[actual].hijo  # Iniciamos con la referencia del hijo
            
            if hijo_actual != None: # Si tiene al menos un hijo

                hijos = []  # lista de hijos
                hijos.append(hijo_actual)   #   Agregamos al hijo directo a la lista de hijos
                hermano = self.elementos_heap[hijo_actual].s_hrn    # Hermano del la referencia al hijo
                
                while hermano not in hijos:
                    hijos.append(hermano)   # Agregamos al hermano    
                    hijo_actual = hermano
                    hermano = self.elementos_heap[hijo_actual].s_hrn

                for nodo in hijos: # para cada elemento hijo del heap actual
                    if nodo not in lista:
                        stack.append(nodo)

        return lista


    '''
        Dado un heap raíz del Bk
        muestra la impresión de como esta formado el Bk
    '''
    def generar_bks(self):
        print("\n= BK's EN LA C.B. =")
        Bks = []
        Raices = []

        raiz_inicial = self.elementos_heap.get(self.elemento_minimo, None)
        Raices.append(raiz_inicial)   #   Agregamos al hijo directo a la lista de hijos
        hermano = self.elementos_heap.get(raiz_inicial.s_hrn, None)    # Hermano del la referencia al hijo

        # Generamos la lista de raices
        while hermano not in Raices:
            Raices.append(hermano)
            raiz_inicial = hermano
            hermano = self.elementos_heap.get(raiz_inicial.s_hrn, None)


        for heap in Raices: # Para cada Heap en la estructura 
            if heap != None:    # Si no es nulo (si hay raíz del heap bk)
                
                grado_bk = heap.grado   # Obtenemos el grado del bk actual
                l_heap = self.elementos_en_bk(heap) # Obtenemos los elementos del heap actual
                info = ""   # Generaremos la información del heap actual
                
                for h in l_heap:    # Para cada elemento de los elementos del bk
                    info += self.elementos_heap[h].shortToString()+".."  # Agregamos la info del elemento
                Bks.append((grado_bk, info[0:len(info)-2]))    # Guardamos la info del Bk actual en la lista de Bk's
        
        for bk in Bks:   # Para cada Bk en la lista imprimiremos su información
            print("B"+str(bk[0])+": "+bk[1])


    '''
        Método para agregar un nuevo elemento (entero) a la estructura de datos
        nuevo_elemento : heap B0 con el valor del nuevo elemento como llave
    '''
    def insertar(self, nuevo_elemento):

        if self.elemento_minimo == None:    # Revisamos si el Heap es Vacío 

            self.elementos_heap[nuevo_elemento] = Heap(nuevo_elemento)    # Creamos el Heap del elemento nuevo_elemento y lo agregamos al diccionario
            self.elemento_minimo = nuevo_elemento   # El elemento mínimo será el primero en agregarse
        
        else:

            self.elementos_heap[nuevo_elemento] = Heap(nuevo_elemento)    # Creamos el Heap del elemento nuevo_elemento y lo agregamos al diccionario
    
            min = self.fundir(self.elemento_minimo, nuevo_elemento)
            self.elemento_minimo = min
        

    '''
        Método para fundir dos listas de Heaps
        Recibe la raiz (elemento mínimo) de cada lista
        y regresa el elemento mínimo de estas dos
    '''
    def fundir(self, R1, R2):
        # Suponemos que las dos raices no son None


        hermano_anterior_r1 = self.elementos_heap[R1].p_hrn
        hermano_anterior_r2 = self.elementos_heap[R2].p_hrn

        self.elementos_heap[R1].p_hrn = self.elementos_heap[R2].p_hrn
        self.elementos_heap[R2].p_hrn = hermano_anterior_r1

        self.elementos_heap[hermano_anterior_r1].s_hrn = R2
        self.elementos_heap[hermano_anterior_r2].s_hrn = R1

        # Regresamos la nueva raíz del nuevo F-heap
        if R1 < R2:
            return R1
        elif R2 < R1:
            return R2
        else:
            return R1


    '''
        Método que regresa la llave del nodo de llave menor global
    '''
    def encuentra_min(self):
        print("Mínimo Global:",self.elemento_minimo)
        return self.elemento_minimo


    # HAY QUE REDEFINIR ESTA FUNCIÓN
    '''
        Función para eliminar el mínimo global de la estructura
    '''
    def eliminar_minimo_global(self):
        print("\n - ELIMINAR MÍNIMO GLOBAL")
        tupla_minimo = self.encontrar_minimo()  # Obtenemos la tupla del indice, llave del mínimo
        indice_eliminar = tupla_minimo[0]   # índice de la raíz mínima
        llave_eliminar = tupla_minimo[1]    # llave de la raíz mínima

        heap = self.array_estructura[indice_eliminar]   # Heap raíz que se eliminará
        self.array_estructura[indice_eliminar] = None   # Eliminamos el heap de las raices Bk's

        heap_eliminar = self.elementos_heap[heap.llave]   # Obtenemos los valores del heap a eliminar
        huerfanos = heap_eliminar.hijos # Obtenemos los BK's huerfanos
        huerfanos.reverse() # Ordenamos para reorganizar cada BK huerfano
        
        del self.elementos_heap[heap_eliminar.llave]    # Eliminamos el heap de la colección

        for huerfano in huerfanos:
            h = self.elementos_heap[huerfano]   # Heap huerfano para reacomodar
            h.padre = None
            self.insertar(huerfano)    # Insertando cada nodo huerfano se reacomodará la Fibonacci Heap

        print("Se eliminó la raíz del B"+str(indice_eliminar)+" Llave: "+str(llave_eliminar))
        return(heap.llave)



if __name__ == "__main__":
    
    try:
        print("\n < FIBONACCI HEAPS >")
        lista = []
        #if len(sys.argv) < 2:
        # VALORES RANDOM PARA GENERAR UNA LISTA DE 10 ELEMENTOS
        longitud_lista = 5#random.randrange(1, 10)
        for i in range(longitud_lista):
            x = random.randrange(1, 100)
            if x not in lista:   # Evitamos que se agreguen elementos repetidos
                lista.append(x)

        cola = Fibonacci_Heap(lista) # Creamos una nueva estructura con los elementos de l
        cola.imprime_elementos_heap()
        #cola.generar_bks()
        cola.encuentra_min()
        '''
        elif sys.argv[1] == "-m":
            # INGRESAMOS LOS ELEMENTOS PARA AGREGAR EN LA ESTRUCTURA
            ELEMENTOS = input("Ingresa los elementos para agregar (enteros separados por una ','[coma]):  ")
            ELEMENTOS = ELEMENTOS.split(',')
            lista = []
            try:

                for n in ELEMENTOS: # Convertimos los elementos a enteros
                    lista.append(int(n))

            except ValueError:
                print(" x ERROR DE ENTRADA: algún valor no era un número")
                quit()

            cola = Fibonacci_Heap(lista) # Creamos una nueva estructura con los elementos de l

        else:
            print("Uso: $ python3 Colas_Binomiales.py <arg>", "\n<arg>: -m: manual  (opcional)")
        '''
    except KeyboardInterrupt:
        print("\n - PROGRAMA CANCELADO")
        quit()
