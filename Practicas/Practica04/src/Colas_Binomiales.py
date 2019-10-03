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
        self.hijos = []
        self.grado = len(self.hijos)
        self.s_hrn = None

    def toString(self):
        print(
            "- - - - - - - -",
            "\nPadre:\t"+str(self.padre),
            "\nLave:\t"+str(self.llave),
            "\nGrado:\t"+str(self.grado),
            "\nHijos:\t"+str(self.hijos),
            "\nS Hrn:\t"+str(self.s_hrn),
            "\n- - - - - - - -")

    def shortToString(self):
        info = str(self.llave)+str(self.hijos)
        #print(info)
        return info

'''
    Clase para hacer la representación de una estructura Cola Binomial
    que tiene como elementos objetos de tipo Heap
'''
class Cola_Binomial:

    def __init__(self, lista_elementos):
        
        suma = sum(lista_elementos)
        size = len(format(len(lista_elementos), "b"))

        print("\nElementos a agregar: ",
            lista_elementos,
            "\nSuma de los elementos: ",
            suma,
            "\nNúmero de elementos: ",
            len(lista_elementos),
            "\nSuma en binario: ",
            (format(len(lista_elementos), "b"))[::-1] )

        self.lista_elementos = lista_elementos
        self.array_estructura = [None]*(size+1)   # GUARDAMOS ÚNICAMENTE LAS RAICES DE LAS BK

        self.elementos_heap = {}    # Diccionario para guardar los Heaps de toda la estructura

        for e in lista_elementos:   # Creamos los heaps para cada elemento de la lista de elementos
            
            self.elementos_heap[e] = Heap(e)    # Creamos el Heap del elemento e y lo agregamos al diccionario
            self.insertar(self.elementos_heap[e])   # Tomamos el Heap del elemento y lo agregamos a la estructura

    '''
        Recibe una lista bk de Bk's
        Nos devuelte el Heap raíz del Bk
    '''
    def get_raiz(self, bk):
        for nodo in bk:
            if nodo.padre == None:
                return nodo

    '''
        Método que regresa el índice del siguiente Bk al índice del bk 
        que se da como parametro
    '''
    def siguiente_bk(self, indice):
        for e in range(indice+1, len(self.array_estructura)):    # Buscamos sobre los Bk en la estructura
            if self.array_estructura[e] != None:   # Obtenemos el siguiente heap
                return e    # Regresamos el indice del siguiente heap


    '''
        Imprime todos los elementos como HEAP dentro de la estructura
    '''
    def imprime_elementos_heap(self):
        for e in self.elementos_heap:
            self.elementos_heap[e].toString()


    '''
        Método para agregar un nuevo elemento (entero) a la estructura de datos
        nuevo_elemento : heap B0 con el valor del nuevo elemento como llave
    '''
    def insertar(self, nuevo_elemento):
        ordenado = False    #   Variable para saber si ya están todos los Bk's correctos
        
        heap_a_acomodar = nuevo_elemento    # Este nuevo elemento es el que se debe agregar a la estructura
        tipo_bk = nuevo_elemento.grado  # Grado del Bk con el cual se fundirá el heap del nuevo_elemento
        
        while(not ordenado):
            heap_mismo_rango = self.array_estructura[tipo_bk]   # Obtenemos el heap con el mismo rango que el que se acomodará
            self.array_estructura[tipo_bk] = None   # Eliminamos como Bk al heap que se fundió

            nuevo_heap = self.fundir(heap_a_acomodar, heap_mismo_rango)  # raiz del nuevo Bk
            
            if heap_mismo_rango == None:    # Si no había un Bk en k+1
                indice_sHrn = self.siguiente_bk(tipo_bk)    # Obtenemos el índice del siguiente hermano del heap que se agregó
    
                if indice_sHrn != None: # Si tiene un siguiente hermano se lo asignamos
                    nuevo_heap.s_hrn = self.array_estructura[indice_sHrn].llave   # Asignamos su siguiente hermano del heap que acabamos de agregar
                    
                self.array_estructura[tipo_bk] = nuevo_heap # Acomodamos al nuevo heap como el actual Bk
                
                ordenado = True # Salimos del while
                continue

            heap_a_acomodar = nuevo_heap    # El heap actual a acomodar es el que se ha creado
            tipo_bk = nuevo_heap.grado  # El heap con el que se debe fundir el nuevo heap es con uno de su mismo rango
        
        



    '''
        Método para fundir dos Bk's del mismo rango,
        recibe únicamente el Heap raíz de cada bk
    '''
    def fundir(self, bk1, bk2):
        if bk2 != None and bk1 != None: # Aseguramos que allá dos Heaps que unir
            raiz1 = bk1
            raiz2 = bk2
            
            #   Si la llave de Bk1 es mayor o igual que la de Bk2
            if raiz1.llave >= raiz2.llave:

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
        Método que regresa los elementos que están debajo de un Heap
        @param bk - heap raíz del bk
    '''
    def elementos_en_bk(self, bk, elementos):
        elementos.append(bk.llave)
        for h in bk.hijos:
            self.elementos_en_bk(self.elementos_heap[h], elementos)
        return elementos
    
    '''
        Dado un heap raíz del Bk
        muestra la impresión de como esta formado el Bk
    '''
    def imprime_bk_generado(self):
        Bks = []
        for heap in self.array_estructura: # Para cada Heap en la estructura 
            if heap != None:    # Si no es nulo (si hay raíz del heap bk)
                
                grado_bk = heap.grado   # Obtenemos el grado del bk actual
                l_heap = self.elementos_en_bk(heap, []) # Obtenemos los elementos del heap actual
                #print(l)
                info = ""   # Generaremos la información del heap actual
                
                for h in l_heap:    # Para cada elemento de los elementos del bk
                    info += self.elementos_heap[h].shortToString()+"."  # Agregamos la info del elemento
                Bks.append((grado_bk, info[0:len(info)-1]))    # Guardamos la info del Bk actual en la lista de Bk's
        
        for bk in Bks:   # Para cada Bk en la lista imprimiremos su información
            print("B"+str(bk[0])+": "+bk[1])
            



if __name__ == "__main__":

    # INGRESAMOS LOS ELEMENTOS PARA AGREGAR EN LA ESTRUCTURA
    '''
    ELEMENTOS = input("Elementos para agregar:  ")
    ELEMENTOS = ELEMENTOS.split(',')
    l = []
    for n in ELEMENTOS: # Convertimos los elementos a enteros
        l.append(int(n))
    '''

    # VALORES RANDOM PARA GENERAR UNA LISTA DE 10 ELEMENTOS
    longitud_lista = random.randrange(1, 10)
    lista_random = []
    for i in range(longitud_lista):
        lista_random.append(random.randrange(100))


    cola = Cola_Binomial(lista_random) # Creamos una nueva estructura con los elementos de l
    #cola.imprime_elementos_heap()
    #print(cola.array_estructura)
    cola.imprime_bk_generado()
