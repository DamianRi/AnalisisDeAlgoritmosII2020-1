#!usr/bin/python3
#-*- coding:utf-8 -*-

import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import random
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
                self.matrix[i][j] = random.randrange(20)
                self.aristas.append([i, j, self.matrix[i][j]])
        self.vertices.append(n_nodos-1)        

        # Valores para generar la red residual
        self.aristas_residual = []



    '''
        Método donde se implementa el algoritmo de Ford Fulkerson
        Recibe como parámetros un nodo S (fuente) y T (pozo) en la gráfica
    '''
    def FordF(self, s, t):

        ruta_delta = self.rutaAumentante(s, t)
        ruta = ruta_delta[0]
        delta = ruta_delta[1]
        flujo_maximo = 0

        x = 0
        while ruta != []:
            x+=1
            flujo_maximo += delta
            print("\nFLUJO MAXIMO: "+str(flujo_maximo))
            print("RUTA ACTUAL: "+str(ruta))
            print("DELTA ACTUAL: "+str(delta))

            for i in range(len(ruta)-1):
                print("Actualizando la casilla: "+str(ruta[i]) +","+str(ruta[i+1]) )
                self.matrix[ruta[i]][ruta[i+1]] = self.matrix[ruta[i]][ruta[i+1]] - delta
                self.matrix[ruta[i+1]][ruta[i]] = self.matrix[ruta[i+1]][ruta[i]] + delta
                self.aristas_residual.append((str(ruta[i+1]), str(ruta[i]), self.matrix[ruta[i+1]][ruta[i]]))
                print(self.matrix)
                

            ruta_delta = self.rutaAumentante(s, t)
            ruta = ruta_delta[0]
            delta = ruta_delta[1]

        print("MATRIZ FINAL CON FLUJO MÁXIMO: "+str(flujo_maximo))
        print(self.matrix)


    '''
        Método para encontrar una ruta aumentante 
        desde un vértice origen 's' hasta un vértices destino 't'
        Recibe como parametro el nombre de los vértices de inicio 's' y final 't'
        Devuelve una lista con los nombres de los vértices de la ruta.
    '''
    def rutaAumentante(self,s, t):
        i_s = self.vertices.index(int(s))
        i_t = self.vertices.index(int(t))
        print("ORIGEN: "+str(i_s)+" - DESTINO: "+str(i_t))
        
        vertices = {}
        #print("VERTICES: "+str(self.vertices))
        for vertice in self.vertices: # Para cada vecino en la lista de vecinos
            vecinos = []
            #print("AGREGANDO VERTICE: "+str(vertice))
            for vecino in range(vertice, len(self.vertices)): # Buscamos sobre los vecinos del vértice actual
                
                if self.matrix[vertice][vecino] != 0:   # Sabemos que es vecino si tiene un valor en la arista
                    vecinos.append(vecino)  # Lo agregamos en la lista de vecinos de cada vertice                
            
            vertices[vertice] = [None, '', False, vecinos] # Distancia, padre, visitado, vecinos 
            #print(str(vertices))
        
        vertices[len(self.vertices)-1] =[None, '', False, []]  # Agregamos el nodo final con valores nulos

        vertices[int(s)][0] = 0
        cola = deque([])
        cola.append([int(s), 0])  # Inicializamos la cola con el vértice origen con distancia cero
        print(vertices)
        while len(cola) != 0:   # Mientras la cola no este vacia
            #print(vertices)
            #print(self.matrix)
            actual = cola.popleft()
            vertices[actual[0]][2] = True

            if actual[0] == int(t):
                print("LLegamos a T")
                break


            for vecino in vertices[actual[0]][3]: # Obtenemos la lista de vecinos del vertice actual
                #print(vertices[vecino])
                
                visitado = vertices[vecino][2]
                #print(visitado)
                flujo = self.matrix[actual[0]][vecino]
                #print(flujo)
                
                if not visitado and flujo != 0:
                    #print("vertices[vecino][0]: "+str(vertices[vecino][0]))
                    if vertices[vecino][0] < actual[1] + self.matrix[actual[0]][vecino]:
                        vertices[vecino][0] = vertices[actual[0]][0] + self.matrix[actual[0]][vecino]
                        vertices[vecino][1] = actual[0]
                        cola.append([vecino, vertices[vecino][0]])

        
        

        # Recreamos la ruta iniciando desde el nodo final
        ruta = []
        v = vertices[int(t)] 
        #print("PADRE DE T:"+str(v[1]))
        ruta.append(int(t))
        padre = v[1]

        if padre == '':
            print("NO HAY RUTA")
            return ([], 0)

        while v[1] != '':
            ruta.append(padre)
            #print("Padre"+str(padre))
            v = vertices[int(padre)]
            #print("Siguinte: "+ str(v[1]))
            padre = v[1]
        
        print("RUTA CREADA")
        ruta.reverse()

        # Obtenemos la lista de deltas de la ruta obtenida
        deltas = []
        for i in range(len(ruta)-1):
            deltas.append(self.matrix[ruta[i]][ruta[i+1]])

        print(ruta)
        print(deltas)
        return((ruta, min(deltas)))            
    

'''
Clase para la representación abstracta de Gráficas dirigidas 
mediante una lista de listas, de nodos con sus nodos vecinos y pesos de las aristas
'''
class GraficaListas:

    '''
    Recibe un parametro 'vertices', una lista del nombre de los vertices.
    Una lista de listas 'aristas', con su capacidad
    La cabeza de cada lista es el nodo origen y el resto son sus vecinos
    '''
    def __init__(self, vertices, aristas):
        self.vertices = vertices #lista de los nombres de los vértices
        self.aristas = aristas #lista de tuplas de las aristas y sus pesos
        self.lista = [] #lista para la listas de los nodos con sus tuplas de aristas
        
        for v in vertices: # para cada vértice agregamos su lista de vecinos
            vecinos = []
            vecinos.append([v, 0])
            for a in aristas: # buscamos sobre las aristas la que inicie con el vértice actual
                if v == a[0]:
                    vecinos.append([a[1], a[2]]) # agregamos el vértice vecino a su lista de vecinos

            self.lista.append([vecinos]) # guardamos la lista con el nodo y su lista de vecinos
        
        self.aristas_residual = []



    '''
        Método para imprimir la lista de listas de los nodos
    '''
    def imprime_grafica(self):
        for vertice in self.lista:
            print(str(vertice)+"\n")




    '''
        Método para generar una gráfica con una cantidad 'n_nodos'
        con valores aleatorios en las aristas
    '''
    def graficaRandom(self, n_nodos):
        
        self.vertices = []
        self.aristas = []

        matrix = np.zeros((n_nodos, n_nodos))
        for i in range(0, n_nodos-1):
            self.vertices.append(str(i))
            
            for j in range(i+1, n_nodos): 
                matrix[i][j] = random.randrange(20) + 1
                self.aristas.append((str(i), str(j), matrix[i][j]))
        self.vertices.append(str(n_nodos-1))

        self.lista = [] #lista para la listas de los nodos con sus tuplas de aristas
        
        for v in self.vertices: # para cada vértice agregamos su lista de vecinos
            vecinos = []
            vecinos.append([v, 0])
            for a in self.aristas: # buscamos sobre las aristas la que inicie con el vértice actual
                if v == a[0]:
                    vecinos.append([a[1], a[2]]) # agregamos el vértice vecino a su lista de vecinos

            self.lista.append([vecinos]) # guardamos la lista con el nodo y su lista de vecinos


    '''
        Método donde se implementa el algoritmo de Ford Fulkerson
        Recibe como parámetros un nodo S (fuente) y T (pozo) en la gráfica
    '''    
    def FordF(self, s, t):
        ruta_delta = self.rutaAumentante(s, t)

        ruta = ruta_delta[0]
        delta = ruta_delta[1]
        flujo_maximo = 0

        while ruta != []:
            print("\nFLUJO MAXIMO: "+str(flujo_maximo))
            print("RUTA ACTUAL: "+str(ruta))
            print("DELTA ACTUAL: "+str(delta))
            flujo_maximo += delta

            for vertice in range(len(ruta)):
                #print("\n"+ruta[vertice])
                for v in self.lista:
                    #print(v[0][1:])
                    #print(v[0][0][0] == ruta[vertice])
                    if v[0][0][0] == ruta[vertice]:
                        #print("VECINOS ")
                        for vecino in v[0][1:]:
                            #print(vecino)
                            if vecino[0] == ruta[vertice+1]:
                                #print("Vecino siguiente")
                                #print(vecino)
                                #print(vecino[1])
                                vecino[1] = vecino[1] - delta
                                #print(vecino[1])
                                

            self.imprime_grafica()
            ruta_delta = self.rutaAumentante(s, t)
            ruta = ruta_delta[0]
            delta = ruta_delta[1]

        print("FLUJO MAXIMO: "+str(flujo_maximo))
        self.imprime_grafica()



    '''
        Método que encuentra una ruta dentro de la gráfica de S a T, 
        donde es la ruta con las aristas de capacidad máxima. 
        Regresa un tupla que tiene una lista de los indices de los nodos y 
        un valor 'delta' el mínimo de las máximas capacidades
    '''
    def rutaAumentante(self, s, t):
        vertices = {}
        for vertice in self.lista:
            #print(str(vertice))
            vertices[vertice[0][0][0]] = [None, '', False, vertice[0][1:]] #distancia, padre, visitado
        
        vertices[s][0] = 0
        cola = deque([])
        cola.append([s, 0])
        #print(str(vertices))
        #print(str(cola))

        while len(cola) != 0:
            actual = cola.popleft()
            vertices[actual[0]][2] = True

            if actual[0] == t:
                #print("LLEGAMOS A T")
                break

            for vecino in vertices[actual[0]][3]:
                #print (str(vecino))
                if vertices[vecino[0]][2] == False and vecino[1] != 0:
                    #print("Vecinos no visitados "+str(vecino[0]))
                    if vertices[vecino[0]][0] < actual[1] + vecino[1]:
                        vertices[vecino[0]][0] = vertices[actual[0]][0] + vecino[1]
                        vertices[vecino[0]][1] = actual[0]
                        cola.append([vecino[0], vertices[vecino[0]][0]])


        # Recreamos la ruta iniciando desde el nodo final
        ruta = []
        v = vertices[t] 
        #print("PADRE DE T:"+str(v[1]))
        ruta.append(t)
        padre = v[1]

        if padre == '':
            print("NO HAY RUTA")
            return ([], 0)

        while v[1] != '':
            ruta.append(padre)
            #print("Padre"+str(padre))
            v = vertices[padre]
            #print("Siguinte: "+ str(v[1]))
            padre = v[1]
        
        print("RUTA CREADA")
        ruta.reverse()

        # Obtenemos la lista de deltas de la ruta obtenida
        deltas = []
        for vertice in range(len(ruta)):
            #print("\n"+ruta[vertice])
            for v in self.lista:
                if v[0][0][0] == ruta[vertice]:
                    for vecino in v[0][1:]:
                        if vecino[0] == ruta[vertice+1]:
                            deltas.append(vecino[1])          

        print(ruta)
        print(deltas)
        return(ruta, min(deltas))






'''
    Método para desplegar una visualización de las gráficas
'''
def visualizarGrafica(grafica):
    #Código para visualizar la gráfica
    G = nx.DiGraph()
    for item in grafica.vertices:
        G.add_node(item, color='blue')
    for item in grafica.aristas:
        G.add_edge(item[0], item[1])
    #nx.draw(G, node_color = '#ffa987')
    #plt.show()

    pos = nx.spring_layout(G) # positions for all nodes
    nx.draw_networkx_nodes(G,pos,
                        nodelist=grafica.vertices,
                        node_color='#ffa987',
                        node_size=200,
                        alpha=0.8)                        
    nx.draw_networkx_edges(G,pos,width=1.0,alpha=0.5)                
    nx.draw_networkx_labels(G,pos,font_size=10)
    plt.axis('off')
    plt.show()

    # VISUALIZAR LA GRAFICA RESIDUAL
    if grafica.aristas_residual != []:
        G.clear()
        for item in grafica.aristas_residual:
            G.add_edge(item[0], item[1])    

        pos = nx.spring_layout(G) # positions for all nodes
        nx.draw_networkx_edges(G,pos,width=1.0,alpha=0.5)                
        nx.draw_networkx_labels(G,pos,font_size=10)                

        plt.axis('off')
        plt.show()





'''
'''
# Implementación de una lista ingresando vértices y aristas, uno por uno
Grafica = GraficaListas(['s', 'a', 'b', 'c','d', 'e', 'f', 'u', 'v', 'w', 'x', 't'], 
[('s', 'a', 14),
('s', 'u', 12),
('s', 'd', 14),
('a', 'b', 4),
('a', 'w', 12),
('a', 'v', 12),
('b', 'c', 5),
('b', 'x', 8),
('c', 't', 12),
('c', 'x', 7),
('d', 'e', 4),
('d', 'u', 12),
('d', 'v', 12),
('e', 'f', 12),
('e', 'x', 4),
('f', 't', 14),
('u', 'a', 12),
('u', 'w', 10),
('u', 'e', 4),
('w', 'v', 10),
('w', 'd', 12),
('w', 'b', 7),
('w', 'e', 8),
('v', 'f', 4),
('v', 'b', 7),
('v', 'e', 12),
('v', 'c', 10),
('v', 'x', 12),
('x', 't', 14),
('x', 'f', 6)])

Grafica.FordF('s', 't')
#Grafica.imprime_grafica()


'''
# USO PARA GRAFICA CON LISTAS
GraficaL = GraficaListas([], [])
n_nodos = input("Ingresa un número de nodos para la Gráfica con LISTAS: ")
s = '0'
t = str(n_nodos-1)
GraficaL.graficaRandom(n_nodos)
GraficaL.imprime_grafica()
GraficaL.FordF(s, t)
visualizarGrafica(GraficaL)

# USO PARA GRAFICA CON MATRICES
GraficaM = GraficaMatriz([], [])
n_nodos = input("Ingresa un número de nodos para la Gráfica con MATRICES: ")
s = '0'
t = str(n_nodos-1)
GraficaM.graficaRandom(n_nodos)
GraficaM.imprime_grafica()
GraficaM.FordF(s, t)
visualizarGrafica(GraficaM)
'''
