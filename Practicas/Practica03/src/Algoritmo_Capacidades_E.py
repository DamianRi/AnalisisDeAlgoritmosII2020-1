#!usr/bin/python
# -*- coding:utf-8-*-

import numpy as np
import random
import math 
from collections import deque

'''
Clase para la representación abstracta de Gráficas Dirigidas
mediante matrices de adyacencia
'''
class GraficaMatriz:

    '''
    Recibe un parametro 'vertices', una lista del nombre de los vertices.
    Una lista de tuplas 'aristas', con su capacidad
    '''
    def __init__(self, vertices, aristas):
        
        self.vertices = vertices #lista para los nombres de vértices y tener su índice almacenado
        self.aristas = aristas #tuplas para las aristas y su capacidad
        self.tam = len(vertices)
        self.matrix = np.zeros((self.tam, self.tam)) #Matriz inicial de valores en cero
        self.residual = self.matrix

        # Vaciamos la lista de de vertices que se recibe como parametros en la matriz
        for v in vertices:
            # vaciamos la lista de las aristas que se recibe como parametro en 
            for a in aristas:
                if v == a[0]: # Si la arista tiene como nodo inicial al vértices actual
                    i = vertices.index(v) # índice del nodo origen en la arista 
                    j = vertices.index(a[1]) # índice del nodo destino de la arista
                    self.matrix[i][j] = a[2]

        self.flujo_total = 0
        self.delta_matrix = np.zeros((self.tam, self.tam)) # Matriz que iremos actualizando para generar la delta gráfica


    '''
        Genera un gráfica, con valores aleatorios en la diagonal superior
    '''
    def graficaRandom(self, n_nodos):
        self.vertices = []
        self.aristas = []
        self.tam = n_nodos
        self.matrix = np.zeros((self.tam, self.tam))
        for i in range(0, self.tam-1):
            self.vertices.append(i)

            for j in range(i+1, self.tam): 
                self.matrix[i][j] = random.randrange(0, 50)
                self.aristas.append([i, j, self.matrix[i][j]])
        self.vertices.append(self.tam-1)        
        self.delta_matrix = np.zeros((self.tam, self.tam))


    '''
        Generar delta gráfica
    '''
    def delta_grafica(self, delta):
        print("\n ** "+str(int(delta))+" - Delta Gŕafica **")
        self.delta_matrix = np.zeros((self.tam, self.tam))
        for i, renglon in enumerate(self.matrix):
            for j, columna in enumerate(self.matrix[i]):
                arista_actual = self.matrix[i][j] # Revisamos si la arista (i,j)
                if arista_actual >= delta: # Si la arista es tiene flujo mayor o igual a 'delta' 
                    self.delta_matrix[i][j] = arista_actual # La guardamos en la delta grafica
        print(self.delta_matrix)


    '''
        Méotodo que encuentra la arista con mayor capacidad (U)
    '''
    def encuentra_U(self):
        U = 0
        for i, renglon in enumerate(self.matrix): # Recorremos todos los renglones
            for j, columna in enumerate(self.matrix[i]): # Recorremos todas las columnas
                actual_u = self.matrix[i][j]
                if U < actual_u:
                    U = actual_u
        return U



    '''
        Algoritmo de Capacidades Escalabales
    '''
    def algoritmo_capacidades_escalables(self, s, t):
        print("\n ----- GRÁFICA ORIGINAL -----")
        print(self.matrix)

        self.flujo_total = 0
        U = self.encuentra_U() # Obtenemos la U de la gráfica
        if U != 0:
            log2_U = math.log(U, 2) # Calculamos su logaritmo base 2
        else:
            print(" x x x - No hay capacidades por donde enviar - x x x")
            return 
        piso_log2_U = math.floor(log2_U) # Calculamos el piso
        delta = math.pow(2, piso_log2_U) # 2^[log U]
        print("x = "+str(int(self.flujo_total)) , "U = "+str(int(U)), "Log2("+str(int(U))+") = "+str(int(piso_log2_U)), "Delta = 2^"+str(int(piso_log2_U)))

        while delta >= 1:
            print("================================================================================")
            print(" ----- DELTA ACTUAL: "+ str(int(delta)))

            self.delta_grafica(delta) #Generamos la delta gráfica
            vertices = self.diccionario_inicial(s, t) # Valores de vértices de la delta gráfica
            self.dijkstra(s, t, vertices) # Generamos posible ruta sobre la delta gráfica
            ruta = self.existeRuta_deltaGrafica(s, t, vertices)
            while ruta != []: # Mientras exista alguna ruta de 's' a 't'
                
                ruta_p = ruta # Identificamos la ruta P
                delta_minima = self.delta_min_ruta(ruta_p) # Obtenemos la delta mínima en P

                self.aumenta(ruta_p, delta_minima) # aumentamos delta unidades de flujo en P
                # al mismo tiempo se actualizó la delta gráfica

                print(" <<<<< "+str(int(delta))+" - Delta Residual ACTUALIZADA")
                print(self.delta_matrix)
                print("\n >>>>> Gráfica Original ACTUALIZADA")
                print(self.matrix)

                vertices = self.diccionario_inicial(s, t) # Valores de vértices de la delta gráfica
                self.dijkstra(s, t, vertices) # Generamos posible ruta sobre la delta gráfica
                ruta = self.existeRuta_deltaGrafica(s, t, vertices) # actualizamos los valores para saber si aun existe ruta


            delta = delta/2 # Sino hay ruta actualizamos la delta
            print("\n **** delta <- delta / 2")

        print("\n\n\n = = = Gráfica Original Final = = = ")
        print(self.matrix)
        print("\n = FLUJO TOTAL: "+str(int(self.flujo_total)))


    '''
        Dijkstra
    '''
    def dijkstra(self, s, t, vertices):
        
        vertices[int(s)][0] = 0
        cola = deque([])
        cola.append(int(s))  # Inicializamos la cola con el vértice origen con distancia cero
        while len(cola) != 0:   # Mientras la cola no este vacia
            actual = cola.popleft()
            vertices[actual][2] = True

            if actual == int(t):
                break

            for vecino in vertices[actual][3]: # Obtenemos la lista de vecinos del vertice actual
                
                visitado = vertices[vecino][2]
                flujo = self.delta_matrix[actual][vecino]
                
                if not visitado and flujo != 0:
                    if vertices[vecino][0] < vertices[actual][0] + self.delta_matrix[actual][vecino]:
                        vertices[vecino][0] = vertices[actual][0] + self.delta_matrix[actual][vecino]
                        vertices[vecino][1] = actual
                        cola.append(vecino)


    '''
        Método que verifica si aun existe una ruta en la gráfica
    '''
    def existeRuta_deltaGrafica(self, s, t, vertices):
        # Obtenemos una ruta P de 's' a 't'
        ruta_p = []
        v = vertices[int(t)] 
        ruta_p.append(int(t))
        padre = v[1]

        if padre == '':
            print("\n x x x - NO HAY RUTA - x x x ")
            return []

        while v[1] != '':
            ruta_p.append(padre)
            v = vertices[int(padre)]
            padre = v[1]
        
        ruta_p.reverse()        
        print("\n= Ruta P: "+str(ruta_p))
        return ruta_p



    '''
        Obtener delta minima de una ruta P
    '''
    def delta_min_ruta(self, ruta_p):
        # Obtenemos el min de los flujos en la ruta P
        deltas = []
        for i in range(len(ruta_p)-1):
            deltas.append(self.delta_matrix[ruta_p[i]][ruta_p[i+1]])
        min_delta = min(deltas)
        print(" = Delta minima: "+str(int(min_delta))+"\n")
        return min_delta


    '''
        Método Aumenta, que actualiza el flujo de la gráfica
    '''
    def aumenta(self, ruta_p, min_delta):

        for x in range(len(ruta_p)-1): # Recorremos las aristas de la ruta P 
            i = ruta_p[x]
            j = ruta_p[x+1]
            self.matrix[i][j] = self.matrix[i][j] - min_delta # Actualizamos delta unidades de flujo sobre P
            self.matrix[j][i] = self.matrix[j][i] + min_delta # Actualizamos las capacidades residuales

            self.delta_matrix[i][j] = self.delta_matrix[i][j] - min_delta # Actualizamos delta unidades de flujo sobre P en delta gráfica
            self.delta_matrix[j][i] = self.delta_matrix[j][i] + min_delta # Actualizamos las capacidades residuales en delta gráfica

        self.flujo_total = self.flujo_total + min_delta


    '''
        Método que genera un diccionario con los valores de la gráfica 
        mapeados
    '''
    def diccionario_inicial(self, s, t):        
        vertices = {}
        for vertice in self.vertices: # Para cada vecino en la lista de vecinos
            vecinos = []
            for vecino in range(vertice, len(self.vertices)): # Buscamos sobre los vecinos del vértice actual
                
                if self.delta_matrix[vertice][vecino] != 0:   # Sabemos que es vecino si tiene un valor en la arista
                    vecinos.append(vecino)  # Lo agregamos en la lista de vecinos de cada vertice                
            
            vertices[vertice] = [None, '', False, vecinos] # Distancia, predecesor, etiquetado, vecinos 
        
        vertices[len(self.vertices)-1] =[None, '', False, []]  # Agregamos el nodo final con valores nulos        

        return vertices


'''
 Ejecución del programa principal
'''
print("\n\t = = = ALGORITMO DE CAPACIDADES ESCALABLES = = = ")
nodos = input("\t > Ingresa un número de nodos para la gráfica (matriz de adyacencias) : ")
G = GraficaMatriz([], [])
G.graficaRandom(nodos)
s = '0'
t = str(nodos-1)
G.algoritmo_capacidades_escalables(s, t)
