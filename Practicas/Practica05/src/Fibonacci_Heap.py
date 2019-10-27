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
    def FibonacciEmpty(self):
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
        Auxiliar
        Encuentra la lista de hijos de un nodo dado su llave
    '''
    def lista_hijos(self, llave):
        hijos = []
        if  self.elementos_heap[llave].hijo != None:            
            h = self.elementos_heap[llave].hijo
            hijos.append(h)            
            while self.elementos_heap[h].s_hrn not in hijos:                
                hijos.append(self.elementos_heap[h].s_hrn)
                h = self.elementos_heap[h].s_hrn
        return hijos

    '''
        Extra
        Imprime todos los elementos como HEAP dentro de la estructura
    '''
    def imprime_elementos_heap(self):
        print(">>>>>    IMPRIMIENDO HEAPS ALMACENADOS")
        for e in self.elementos_heap:
            self.elementos_heap[e].toString()

    '''
        Auxiliar para impresión de árboles
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
        Auxiliar para impresión de árboles
        Función para generar una cadena con la información de cada nodo
        Será usada para imprimir los árboles en el F-Heap
    '''
    def info_heap(self, llave):
        if self.elementos_heap[llave].marcado:
            return str(llave)+"*("+str(self.elementos_heap[llave].p_hrn)+","+str(self.elementos_heap[llave].s_hrn)+")"+str(self.lista_hijos(llave))
        else:
            return str(llave)+"("+str(self.elementos_heap[llave].p_hrn)+","+str(self.elementos_heap[llave].s_hrn)+")"+str(self.lista_hijos(llave))
    
    
    '''
        Impresión de árboles
        Dado un heap raíz del Bk
        muestra la impresión de como esta formado el Bk
    '''
    def generar_bks(self):
        print("\n\t== Árboles en F-Heap ==")
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
                    #info += self.elementos_heap[h].shortToString()+".."  # Agregamos la info del elemento
                    info += self.info_heap(h)+" .."
                Bks.append((grado_bk, info[0:len(info)-2]))    # Guardamos la info del Bk actual en la lista de Bk's
        
        for bk in Bks:   # Para cada Bk en la lista imprimiremos su información
            print("B"+str(bk[0])+": "+bk[1])


    '''
        Método para agregar un nuevo elemento (entero) a la estructura de datos
        nuevo_elemento : heap B0 con el valor del nuevo elemento como llave
    '''
    def insertar(self, nuevo_elemento):
        #print(">>>>>    INSERTANDO ", nuevo_elemento)
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
        #print(">>>>>    FUNDIENDO ", R1, " con ", R2)
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
        print(">>>>>    ENCONTRANDO MÍNIMO ",self.elemento_minimo)
        return self.elemento_minimo


    '''
        Liga dos árboles del mismo rango
    '''
    def link(self, R1, R2):
        #print(">>>>>    LIGANDO ", R1, " CON ", R2)
        if R1 <= R2:
            self.elementos_heap[R2].padre = R1  # Ponemos como padre a R1 de R2
            hijo_r1 = self.elementos_heap[R1].hijo
            self.elementos_heap[R1].hijo = R2   # Ponemos como hijo a R2 de R1

            # Cambiamos las referencias para quitar a R2 como raíz
            self.elementos_heap[self.elementos_heap[R2].p_hrn].s_hrn = self.elementos_heap[R2].s_hrn
            self.elementos_heap[self.elementos_heap[R2].s_hrn].p_hrn = self.elementos_heap[R2].p_hrn            
            # Preparamos a R2 para fundir con los hijos de R1
            self.elementos_heap[R2].s_hrn = R2
            self.elementos_heap[R2].p_hrn = R2
            # Si R1 tiene hijo los enlazamos
            if hijo_r1 != None:
                self.fundir(hijo_r1, R2)

            self.elementos_heap[R1].grado += 1  # Aumentamos el rango             
            return R1
        elif R1 > R2:

            self.elementos_heap[R1].padre = R2  # Ponemos como padre a R2 de R1
            hijo_r2 = self.elementos_heap[R2].hijo
            self.elementos_heap[R2].hijo = R1   # Ponemos como hijo a R1 de R2

            # Cambiamos las referencias para quitar a R1 como raíz
            self.elementos_heap[self.elementos_heap[R1].p_hrn].s_hrn = self.elementos_heap[R1].s_hrn
            self.elementos_heap[self.elementos_heap[R1].s_hrn].p_hrn = self.elementos_heap[R1].p_hrn            
            # Preparamos a R1 para fundir con los hijos de R2
            self.elementos_heap[R1].s_hrn = R1
            self.elementos_heap[R1].p_hrn = R1
            # Si R2 tiene hijo los enlazamos
            if hijo_r2 != None:
                self.fundir(hijo_r2, R1)

            self.elementos_heap[R2].grado += 1  # Aumentamos el rango
            return R2


    '''
        Función para eliminar el mínimo global de la estructura
    '''
    def borra_min(self):
        print(">>>>>    BORRANDO MÍNIMO", self.elemento_minimo)
        min = self.elemento_minimo
        hijo = self.elementos_heap[self.elemento_minimo].hijo   # Obtenemos el hijo del elemento mínimo
        s_hermano = self.elementos_heap[self.elemento_minimo].s_hrn # Obtenemos el valor del siguiente hermano
        
        # Si el mínimo no es una raíz única, entonces eliminamos        
        if self.elementos_heap[min].s_hrn != min and self.elementos_heap[min].p_hrn != min:

            self.elementos_heap[self.elementos_heap[min].p_hrn].s_hrn = self.elementos_heap[min].s_hrn  
            self.elementos_heap[self.elementos_heap[min].s_hrn].p_hrn = self.elementos_heap[min].p_hrn
        
            self.elemento_minimo = self.buscar_min(s_hermano)   # Obtenemos el nuevo mínimo

        # Eliminamos el Heap mínimo
        del self.elementos_heap[min]   


        # Verificamos que tenga un hijo
        if hijo != None:
            huerfanos = []
            huerfanos.append(hijo)
            # Creamos la lista de huerfanos del nodo eliminado
            while(self.elementos_heap[hijo].s_hrn not in huerfanos):
                self.elementos_heap[hijo].padre = None  # Le quitamos el padre a cada nodo huerfano
                huerfanos.append(self.elementos_heap[hijo].s_hrn)   # Lo agregamos a la lista de hermanos
                hijo = self.elementos_heap[hijo].s_hrn  # Continuamos con su hermano


            # Para cada huerfano lo agregamos como nodo raíz
            for h in huerfanos:
                self.elemento_minimo = self.fundir(self.elemento_minimo, h)

        raices_actuales = []
        rangos = []
        nuevo_min = self.elemento_minimo
        raices_actuales.append(nuevo_min)
        # Creamos la lista de todas las raices
        while(self.elementos_heap[nuevo_min].s_hrn not in raices_actuales):
            rangos.append(self.elementos_heap[nuevo_min].grado )
            raices_actuales.append(self.elementos_heap[nuevo_min].s_hrn)   # Lo agregamos a la lista de hermanos
            nuevo_min = self.elementos_heap[nuevo_min].s_hrn  # Continuamos con su hermano        

        raices_acomodadas = {}
        
        # Para cada raíz luego de quitar el mínimo
        for raiz in raices_actuales:
            rango_actual = self.elementos_heap[raiz].grado  # Tomamos el rango actual de heap
            almacenado = raices_acomodadas.get(rango_actual, None)  # Tomamos el que tenga el mismo rango
            # Si no hay un heap con el mismo rango
            if almacenado == None:
                raices_acomodadas[rango_actual] = self.elementos_heap[raiz].llave # Colocamos el nodo actual
            else:
                ligado = self.link(raiz, self.elementos_heap[almacenado].llave)    # Fundimos dos del mismo rango k

                ordenado = False
                # Mientras que no este un único árbol con un rango
                while not ordenado:
                    # Si ya no hay un siguiente árbol con el mismo rango
                    if raices_acomodadas.get(rango_actual+1, None) == None:
                        raices_acomodadas[rango_actual+1] = ligado # Almacenamos la raíz en el k+1
                        raices_acomodadas[rango_actual] = None  # Liberamos el espacio del rango k
                        ordenado = True
                        continue
                    # Actualizamos el rango actual
                    raices_acomodadas[rango_actual] = None  # Liberamos el espacio del rango k

                    rango_actual = self.elementos_heap[ligado].grado
                    ligado = self.link(ligado, raices_acomodadas[rango_actual]) # Ligamos los dos árboles del mismo rango


    ''' 
        Auxiliar:
        Función que al eliminiar el mínimo global, buscará el nuevo mínimo entre las raices.
    '''
    def buscar_min(self, inicio):
        candidatos = [] # Nodos raiz
        candidatos.append(inicio)

        siguiente_hermano = self.elementos_heap[inicio].s_hrn          
        while(siguiente_hermano not in candidatos): # Mientras un nodo raíz no este lo agregamos
            candidatos.append(siguiente_hermano)
            # Recorremos sobre el nodo siguiente hasta que uno se repita
            siguiente_hermano = self.elementos_heap[siguiente_hermano].s_hrn

        # Regresamos el mínimo de todas la raices
        return min(candidatos)


    '''
        Función para decrementar el valor de la llave de un elemento específico
        param llave - llave del elemento a decrementar
        param delta - delta valor a decrementar la llave
    '''
    def decrementa_llave(self, llave, delta):
        print(">>>>>    DECRETEMENTANDO ", llave, "-", delta,"=", llave-delta)
        nueva_llave = llave-delta   # Nueva llave
        # Si se creando dos nodos con la misma llave terminamos el programa
        if self.elementos_heap.get(nueva_llave, None) != None:
            print("ERROR: SE GENERARON DOS NODOS CON EL MISMO VALOR AL DECREMENTAR")
            quit()

        # Se decremeneta la llave con delta unidades
        self.elementos_heap[nueva_llave] = self.elementos_heap[llave]   # Agrecamos el elemento de "nueva_llave"
        self.elementos_heap[nueva_llave].llave = nueva_llave
        del self.elementos_heap[llave]  # Eliminamos el heap con la llave "llave"

        self.actualizar_valores(llave, nueva_llave)

        # Si la llave a decrementar es una raíz r
        if self.elementos_heap[nueva_llave].padre == None:
            # Si la nueva_llave es menor que la llave mínima
            if (nueva_llave) < self.elemento_minimo:
                self.elemento_minimo = nueva_llave  # Actualizamos el mínimo heap

        # Si no es una raíz
        else:
            # Si la llave del padre es mayor que la del hijo
            if (nueva_llave) < self.elementos_heap[nueva_llave].padre:
                self.elemento_minimo = self.buscar_min(self.elemento_minimo)
                self.corte_en_cascada(nueva_llave)


    '''
        Auxiliar para decrementar llave
        Función que dado un valor de llave nuevo y uno viejo
        actualiza todas las apariciones del valor viejo por el nuevo
    '''
    def actualizar_valores(self, llave, nueva_llave):
        ## Cambiamos el valor de la llave antigua por la nueva llave sobre todos los heaps
        for n in self.elementos_heap:
            if self.elementos_heap[n].padre == llave:
                self.elementos_heap[n].padre = nueva_llave
            if self.elementos_heap[n].llave == llave:
                self.elementos_heap[n].llave = nueva_llave
            if self.elementos_heap[n].hijo == llave:
                self.elementos_heap[n].hijo = nueva_llave
            if self.elementos_heap[n].s_hrn == llave:
                self.elementos_heap[n].s_hrn = nueva_llave
            if self.elementos_heap[n].p_hrn == llave:
                self.elementos_heap[n].p_hrn = nueva_llave
        

    '''
        Función para realizar el corte en cascada de un nodo
        param llave - llave del heap sobre el cual se hará el corte en cascada
    '''
    def corte_en_cascada(self, llave):
        #print(">>>>>    CORTE EN CASCADA SOBRE ", llave)
        # Quitamos la liga que une a p(i) con i        
        # Si es el hijo que tiene como refencia directa el padre
        if self.elementos_heap[self.elementos_heap[llave].padre].hijo == llave:
            # Si es hijo único
            if self.elementos_heap[llave].s_hrn == llave and self.elementos_heap[llave].p_hrn == llave:
                # Quitamos su referencia a tener hijo
                self.elementos_heap[self.elementos_heap[llave].padre].hijo = None
        
            # Si no es hijo único
            else:
                # Le ponemos la referencia de otro hijo al padre
                self.elementos_heap[self.elementos_heap[llave].padre].hijo = self.elementos_heap[llave].s_hrn

        padre_i = self.elementos_heap[llave].padre  # Guardamos el p(i)
        # Quitamos referencia a su padre
        self.elementos_heap[llave].padre = None
        # Garantizamos que i queda desmarcado
        self.elementos_heap[llave].marcado = False
        # Decrementamos en uno el rando de p(i)
        self.elementos_heap[padre_i].grado -= 1

        # Si tiene otro hijo, lo quitamos de la lista de hijo
        if self.elementos_heap[padre_i].hijo != None:
            # Quitamos las referencias al nodo de los hermanos
            self.elementos_heap[self.elementos_heap[llave].p_hrn].s_hrn = self.elementos_heap[llave].s_hrn
            self.elementos_heap[self.elementos_heap[llave].s_hrn].p_hrn = self.elementos_heap[llave].p_hrn

        self.elementos_heap[llave].s_hrn = llave
        self.elementos_heap[llave].p_hrn = llave

        # Añadimos a "i" a la lista de hijos
        self.fundir(self.elemento_minimo, llave)

        # Si p(i) esta marcado
        if self.elementos_heap[padre_i].marcado:
            self.elementos_heap[padre_i].marcado = False   # Desmarcamos a p(i)
            # Aplicamos "Corte en Cascada" a p(i)
            self.corte_en_cascada(padre_i)
        else:
            if self.elementos_heap[padre_i].padre != None:
                # Si el p(p(i)) no es una raíz
                if self.elementos_heap[self.elementos_heap[padre_i].padre].padre != None:
                    self.elementos_heap[padre_i].marcado = True


    '''
        Función que dada una llave cualquiera, elimina el nodo con la llave
    '''
    def elimina(self, llave):
        print(">>>>>    ELIMINANDO NODO ", llave)
        nodo_eliminar = self.elementos_heap[llave]

        # Lo quitamos de su referencias a hermanos
        self.elementos_heap[self.elementos_heap[llave].p_hrn].s_hrn = self.elementos_heap[llave].s_hrn
        self.elementos_heap[self.elementos_heap[llave].s_hrn].p_hrn = self.elementos_heap[llave].p_hrn

        # Si es un nodo con padre
        if nodo_eliminar.padre != None:
            self.elementos_heap[nodo_eliminar.padre].grado -= 1 # Decrementamos en uno el grado de su padre
            # Quitamos la liga que une a p(i) con i        
            # Si es el hijo que tiene como refencia directa el padre
            if self.elementos_heap[nodo_eliminar.padre].hijo == llave:
                # Si es hijo único
                if nodo_eliminar.s_hrn == llave and nodo_eliminar.p_hrn == llave:
                    # Quitamos su referencia a tener hijo
                    self.elementos_heap[nodo_eliminar.padre].hijo = None
            
                # Si no es hijo único
                else:
                    # Le ponemos la referencia de otro hijo al padre
                    self.elementos_heap[nodo_eliminar.padre].hijo = nodo_eliminar.s_hrn

            # Quitamos referencia a su padre
            self.elementos_heap[llave].padre = None

        # Si es un nodo raíz
        else:
            self.elemento_minimo = self.buscar_min(nodo_eliminar.s_hrn)

        huerfanos = self.lista_hijos(llave)
        for h in huerfanos:
            self.elementos_heap[h].padre = None
            self.elementos_heap[h].s_hrn = h
            self.elementos_heap[h].p_hrn = h
            self.fundir(self.elemento_minimo, h)
            
        del self.elementos_heap[llave]
        


if __name__ == "__main__":
    
    try:
        print("\n < FIBONACCI HEAPS >")
        lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
        for i in range(len(lista)):
            lista[i] = lista[i]*3
        print(lista)

        cola = Fibonacci_Heap(lista) # Creamos una nueva estructura con los elementos de una lista
        cola.generar_bks()  # Mostramos los nodos iniciales
        cola.borra_min()    # Borramos el nodo min 3
        cola.encuentra_min()    # Mostramos el nuevo mínimo
        cola.generar_bks()  # Mostramos los árboles generados
        cola.decrementa_llave(48, 7)    # Decrementamos el nodo 48 a 42
        cola.generar_bks()
        cola.decrementa_llave(45, 5)    # Decrementamos el nodo 45 a 40
        cola.generar_bks()  # Mostramos los árboles generados
        cola.elimina(12) # Eliminamos el nodo 12
        cola.generar_bks()  # Mostramos los árboles generados
        cola.decrementa_llave(36, 2)    # Decrementamos el nodo 36 a 34
        cola.generar_bks()  # Mostramos los árboles generados
        cola.elimina(30)    # Eliminamos el nodo 30 
        cola.generar_bks()  # Mostramos los árboles generados

    except KeyboardInterrupt:
        print("\n - PROGRAMA CANCELADO")
        quit()
