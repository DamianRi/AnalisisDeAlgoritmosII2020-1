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
        info = str(self.p_hrn)+str(self.llave)+str(self.s_hrn)+str(self.marcado)
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

        suma = sum(lista_elementos)
        size = len(format(len(lista_elementos), "b"))

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
        for e in range(indice+1, len(self.array_estructura)):    # Buscamos sobre los Bk en la estructura
            if self.array_estructura[e] != None:   # Obtenemos el siguiente heap
                return e    # Regresamos el indice del siguiente heap
        return None

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

            #
            #   HAY QUE MODIFICAR PARA QUE RECORRA LA LISTA DOBLEMENTE LIGADA DE LOS HEAPS
            #
            for e in self.elementos_heap[actual].hijos: # para cada elemento hijo del heap actual
                if e not in lista:
                    stack.append(e)

        return lista


    '''
        Dado un heap raíz del Bk
        muestra la impresión de como esta formado el Bk
    '''
    def generar_bks(self):
        print("\n= BK's EN LA C.B. =")
        Bks = []
        for heap in self.array_estructura: # Para cada Heap en la estructura 
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

            nuevo_heap = self.elementos_heap.get(nuevo_elemento, None) # Obtenemos el heap que debemos insertar en la cola

            if nuevo_heap == None: # Si el nuevo elemento no está como Heap
                self.elementos_heap[nuevo_elemento] = Heap(nuevo_elemento)    # Creamos el Heap del elemento nuevo_elemento y lo agregamos al diccionario

            # Si hay un único elemento
            if self.elementos_heap[self.elemento_minimo].s_hrn == self.elemento_minimo and self.elementos_heap[self.elemento_minimo].p_hrn == self.elemento_minimo:
                
                self.elementos_heap[nuevo_elemento].s_hrn = self.elemento_minimo 
                self.elementos_heap[self.elemento_minimo].p_hrn = nuevo_elemento                                
                self.elementos_heap[nuevo_elemento].p_hrn = self.elemento_minimo
                self.elementos_heap[self.elemento_minimo].s_hrn = nuevo_elemento

            # Si ya hay varios elementos
            else:
                self.elementos_heap[nuevo_elemento].s_hrn = self.elemento_minimo    
                self.elementos_heap[nuevo_elemento].p_hrn = self.elementos_heap[self.elemento_minimo].p_hrn
                
                self.elementos_heap[self.elementos_heap[self.elemento_minimo].p_hrn].s_hrn = nuevo_elemento
                self.elementos_heap[self.elemento_minimo].p_hrn = nuevo_elemento                

        ## Verificamos si el nuevo elemento es menor que el mínimo actual
        if nuevo_elemento < self.elementos_heap[self.elemento_minimo].llave:    
            self.elemento_minimo = nuevo_elemento   # Actualizamos el valor del mínimo 

        '''
        ordenado = False    #   Variable para saber si ya están todos los Bk's correctos
        
        tipo_bk = heap_a_acomodar.grado  # Grado del Bk con el cual se fundirá el heap del nuevo_elemento
        
        while(not ordenado):
            heap_mismo_rango = self.array_estructura[tipo_bk]   # Obtenemos el heap con el mismo rango que el que se acomodará
            self.array_estructura[tipo_bk] = None   # Eliminamos como Bk al heap que se fundió

            nuevo_heap = self.fundir(heap_a_acomodar, heap_mismo_rango)  # raiz del nuevo Bk
            
            if heap_mismo_rango == None:    # Si no había un Bk en k+1
                indice_sHrn = self.siguiente_bk(tipo_bk)    # Obtenemos el índice del siguiente hermano del heap que se agregó
    
                if indice_sHrn != None: # Si tiene un siguiente hermano se lo asignamos
                    nuevo_heap.s_hrn = self.array_estructura[indice_sHrn].llave   # Asignamos su siguiente hermano del heap que acabamos de agregar

                else:
                    nuevo_heap.s_hrn = None # Si ya no hay un Bk+1 no tendrá siguiente hermano

                self.array_estructura[tipo_bk] = nuevo_heap # Acomodamos al nuevo heap como el actual Bk
                
                ordenado = True # Salimos del while
                continue

            heap_a_acomodar = nuevo_heap    # El heap actual a acomodar es el que se ha creado
            tipo_bk = nuevo_heap.grado  # El heap con el que se debe fundir el nuevo heap es con uno de su mismo rango
        
        #self.generar_bks()
        '''

    '''
        Método para fundir dos Bk's del mismo rango,
        recibe únicamente el Heap raíz de cada bk
    '''
    def fundir(self, bk1, bk2):
        if bk2 != None and bk1 != None: # Aseguramos que allá dos Heaps que unir
            raiz1 = bk1
            raiz2 = bk2
            
            #   Si la llave de Bk1 es mayor o igual que la de Bk2
            if raiz1.llave <= raiz2.llave:

                self.elementos_heap[raiz2.llave].padre = raiz1.llave    # Marcamos como padre a Bk1 de Bk2
                self.elementos_heap[raiz2.llave].s_hrn = None   # Marcamos como siguiente hermano None
                self.elementos_heap[raiz1.llave].hijos.append(raiz2.llave)  # Agregamos como hijo a Bk2 de Bk1
                self.elementos_heap[raiz1.llave].grado = len(self.elementos_heap[raiz1.llave].hijos)    # Actualizamos el grado del nodo raíz Bk2
                
                return raiz1    # Regreamos el Heap raíz del nuevo Bk
            
            #   Si la llve de Bk2 es mayor que la de Bk1
            else:
                self.elementos_heap[raiz1.llave].padre = raiz2.llave    # Marcamos como padre a Bk2 de Bk1
                self.elementos_heap[raiz1.llave].s_hrn = None   # Marcamos como siguiente hermano None
                self.elementos_heap[raiz2.llave].hijos.append(raiz1.llave)  # Agregamos como hijo a Bk1 de Bk2
                self.elementos_heap[raiz2.llave].grado = len(self.elementos_heap[raiz2.llave].hijos)    # Actualizamos el grado del nodo raíz Bk2

                return raiz2    # Regresamos el Heap raíz del nuevo Bk 
            

        #   Si uno de los dos Bk es vacío
        else:
            #   Regresamos bk1 si bk2 es vacio
            if bk1 != None:
                return bk1
            #   Regresamos bk2 si bk1 es vacío 
            else:
                return bk2 

    '''
        Método para encontrar el índice del heap raíz con el menos valor
    '''
    def encontrar_minimo(self):
        primerE = 0
        # Obtenemos el índice del primer elemento en los Bk's
        for i in range(len(self.array_estructura)):
            if self.array_estructura[i] != None:
                primerE = i
                break

        min = self.array_estructura[primerE].llave  # Minimo inicial
        indice = primerE    # índice del heap mínimo

        # Búscamos el mínimo global sobre los demás Bk's
        for i in range(primerE, len(self.array_estructura)):
            heapActual = self.array_estructura[i]   # Compararemos con el actual
            if heapActual != None:  # Revisamos que no sea None
                if heapActual.llave <= min:
                    min = heapActual.llave
                    indice = i

        print(
            "Mínimo Global: "+ str(self.array_estructura[indice].llave), 
            "Indice Heap: B"+ str(indice)) 
        return (indice, self.array_estructura[indice].llave)


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
        print("\n < COLAS BINOMIALES >")
        lista = []
        #if len(sys.argv) < 2:
        # VALORES RANDOM PARA GENERAR UNA LISTA DE 10 ELEMENTOS
        longitud_lista = 4#random.randrange(1, 10)
        for i in range(longitud_lista):
            x = random.randrange(1, 100)
            if x not in lista:   # Evitamos que se agreguen elementos repetidos
                lista.append(x)

        cola = Fibonacci_Heap(lista) # Creamos una nueva estructura con los elementos de l
        cola.imprime_elementos_heap()
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
