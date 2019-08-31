#!usr/bin/python3
#-*- coding:utf-8 -*-

import numpy as np
import random

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
        tam = len(vertices)
        self.matrix = np.zeros((tam, tam)) #Matriz inicial de valores en cero
        self.residual = self.matrix

        # Vaciamos la lista de de vertices que se recibe como parametros en la matriz
        for v in vertices:
            # vaciamos la lista de las aristas que se recibe como parametro en 
            for a in aristas:
                if v == a[0]: # Si la arista tiene como nodo inicial al vértices actual
                    i = vertices.index(v) # índice del nodo origen en la arista 
                    j = vertices.index(a[1]) # índice del nodo destino de la arista
                    self.matrix[i][j] = a[2]

        self.aristas_residual = self.vertices
        self.flujo_total = 0

    '''
        Método para imprimir la matriz de la gráfica
    '''
    def imprime_grafica(self):
        print(self.matrix)


    '''
        Genera un gráfica, con valores aleatorios en la diagonal superior
    '''
    def graficaRandom(self, n_nodos):
        self.vertices = []
        self.aristas = []

        self.matrix = np.zeros((n_nodos, n_nodos))
        for i in range(0, n_nodos-1):
            self.vertices.append(i)

            for j in range(i+1, n_nodos): 
                self.matrix[i][j] = random.randrange(0, 100)
                self.aristas.append([i, j, self.matrix[i][j]])
        self.vertices.append(n_nodos-1)        
        self.matrix[0][n_nodos-1] = 0
        # Valores para generar la red residual
        self.aristas_residual = []


    '''
        Método que aplica el algoritmo de etiquetado
        sobre una gráfica matricial
    '''
    def algoritmo_etiquetamiento(self, s, t):
        print(" - MATRIZ INICIAL - ")
        self.imprime_grafica()

        print("\n <<< ENVIO DE FLUJO DE s:"+s+" a t:"+t)

        vertices = self.diccionario_inicial(s, t) # Obtenemos los vertices con su distancia
        vertices[int(t)][2] = True # Etiquetamos al nodo 't'

        while vertices[int(t)][2]: # Mientras que 't' esta etiquetado
            for vertice in vertices:
                vertices[vertice][2] = False # Desetiquetamos a todos los nodos
            
            for vertice in vertices:
                vertices[vertice][1] = '' # Para cada nodo su predecesor será 0 (cero) 
            
            vertices[int(s)][2] = True # Etiquetamos al nodo 's'

            lista = []
            lista.append(int(s)) # Agregamos a 's' a LISTA

            while len(lista) != 0 and not vertices[int(t)][2]: # Mientras que la LISTA sea diferente de 0 y 't' no esta etiquetado
                i = lista.pop()

                for vecino in vertices[i][3]: # Para cada arco que emana del nodo 'i'
                    
                    if self.matrix[i][vecino] > 0 and vertices[vecino][2] == False: # Si el flujo en el arco es mayor a 0 y 'j' esta sin etiqueta 

                        vertices[vecino][1] = i # Predecesor de 'j' <- 'i'
                        vertices[vecino][2] = True # Etiquetamos a 'j'
                        lista.append(vecino) # Agregamos 'j' a la lista
            
            if vertices[int(t)][2]: # Si 't' esta etiquetado
                self.aumenta(s, t, vertices)

        print(" >>> FLUJO TOTAL: "+ str(self.flujo_total)) # Imprimimos el flujo total 
        print("\n - MATRIZ FINAL -")
        self.imprime_grafica() # Imprimimos la gráfica final

    '''
        Método Aumenta, que actualiza el flujo de la gráfica
    '''
    def aumenta(self, s, t, vertices):
        # Obtenemos una ruta aumentante P de 's' a 't'
        ruta_aumentante = []
        v = vertices[int(t)] 
        ruta_aumentante.append(int(t))
        padre = v[1]

        if padre == '':
            print("NO HAY RUTA")
            return ([], 0)

        while v[1] != '':
            ruta_aumentante.append(padre)
            v = vertices[int(padre)]
            padre = v[1]
        
        print("\nRuta Aumentante")
        ruta_aumentante.reverse()        
        print(ruta_aumentante)


        # Obtenemos el min de los flujos en la ruta P
        deltas = []
        for i in range(len(ruta_aumentante)-1):
            deltas.append(self.matrix[ruta_aumentante[i]][ruta_aumentante[i+1]])
        min_delta = min(deltas)
        print("Delta minima: "+str(min_delta)+"\n")


        for x in range(len(ruta_aumentante)-1): # Recorremos las aristas de la ruta P 
            i = ruta_aumentante[x]
            j = ruta_aumentante[x+1]
            self.matrix[i][j] = self.matrix[i][j] - min_delta # Actualizamos delta unidades de flujo sobre P
            self.matrix[j][i] = self.matrix[j][i] + min_delta # Actualizamos las capacidades residuales

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
                
                if self.matrix[vertice][vecino] != 0:   # Sabemos que es vecino si tiene un valor en la arista
                    vecinos.append(vecino)  # Lo agregamos en la lista de vecinos de cada vertice                
            
            vertices[vertice] = [None, '', False, vecinos] # Distancia, predecesor, etiquetado, vecinos 
        
        vertices[len(self.vertices)-1] =[None, '', False, []]  # Agregamos el nodo final con valores nulos        

        return vertices



grafica = GraficaMatriz([], [])
n_nodos = input(" Ingresa un número de nodos para la gráfica (matriz de adyacencias) : ")
s = '0'
t = str(n_nodos-1)
grafica.graficaRandom(n_nodos)
grafica.algoritmo_etiquetamiento(s, t)