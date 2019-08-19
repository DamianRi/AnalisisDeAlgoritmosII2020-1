#!usr/bin/python3
#-*- coding:utf-8 -*-

import numpy as np

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
        self.residual = np.zeros((tam, tam))
        for v in vertices:
            for a in aristas:
                if v == a[0]:
                    self.matrix[vertices.index(v)][vertices.index(a[1])] = a[2] 


    def imprime_grafica(self):
        print(self.matrix)

    '''
    '''
    def FordF(self, s, t):
        camino = []
        inicio = self.vertices.index(s)
        destino = self.vertices.index(t)
        i = self.vertices.index(s)
        while i != destino:
            vecino = i
            mayor = 0
            indice  = 0
            for v in self.matrix[i]: #recorremos el renglon i-ésimo
                if mayor < v: #Obtenemos el valor más grande de las aristas
                    mayor = v
                    vecino = self.vertices[indice]
                indice+=1
            camino.append(vecino)
            i = self.vertices.index(vecino)
        return camino

    def rutaAumentante(self,s, t):
       pass

'''
Clase para la representación abstracta de Gráficas dirigidas 
mediante una lista de listas, de nodos con sus nodos vecinos y pesos de las aristas
'''
class GraficaListas:

    '''
    Recibe un parametro 'vertices', una lista del nombre de los vertices.
    Una lista de tuplas 'aristas', con su capacidad
    '''
    def __init__(self, vertices, aristas):
        self.vertices = vertices #lista de los nombres de los vértices
        self.aristas = aristas #lista de tuplas de las aristas y sus pesos
        self.lista = [] #lista para la listas de los nodos con sus tuplas de aristas
        for v in vertices:
            vecinos = []
            for a in aristas:
                if v == a[0]:
                    vecinos.append((a[1], a[2]))
            self.lista.append([v, vecinos])
        
        self.residual = self.lista


    def imprime_grafica(self):
        print(self.lista)
    
    def FordF(self):
        pass

    def rutaAumentante(self, s, t):
        pass





Grafica = GraficaMatriz(['A', 'B', 'C', 'D'], [('A', 'B', 1), ('B', 'C', 2), ('C', 'A', 3), ('D', 'B', 10)])
Grafica.imprime_grafica()
print(Grafica.FordF('A', 'B'))

g_listas = GraficaListas(['A', 'B', 'C'], [('A', 'B', 1), ('B', 'C', 2), ('C', 'A', 3)])
g_listas.imprime_grafica()