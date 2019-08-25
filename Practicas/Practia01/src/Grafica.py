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
            self.vertices.append(str(i))
            for j in range(i+1, n_nodos): 
                self.matrix[i][j] = random.randrange(20)
                self.aristas.append((str(i), str(j), self.matrix[i][j]))
        self.vertices.append(str(n_nodos-1))        

        self.matrix[0][n_nodos-1] = 0



    '''
        Método donde se implementa el algoritmo de Ford Fulkerson
        Recibe como parámetros un nodo S (fuente) y T (pozo) en la gráfica
    '''
    def FordF(self, s, t):
        ruta = self.rutaAumentante(s, t)
        max_flujo = 0

        while ruta[0] != []:#Mientas exista una ruta de s a t
            
            print("RUTA: "+str(ruta))
            delta = ruta[1] #Obtenemos el valor delta de la ruta encontrada
            print("Delta Actual: "+str(delta))
            max_flujo += delta
            #Actualizamos los valores de las aristas dentro de la ruta

            for x in range(0, len(ruta)):

                print("Actualizamos la casilla ("+str(ruta[0][x])+","+str(ruta[0][x+1])+")" )
                self.matrix[ruta[0][x]][ruta[0][x+1]] -= delta #Actualizamos los flujos de las aristas de la ruta
                self.matrix[ruta[0][x+1]][ruta[0][x]] += delta
                print(self.matrix)
                

            ruta = self.rutaAumentante(s, t) # Actualizamos la ruta aumentante

        print("MATRIZ FINAL CON FLUJO MÁXIMO: "+str(max_flujo))
        print(self.matrix)


    '''
        Método para encontrar una ruta aumentante 
        desde un vértice origen 's' hasta un vértices destino 't'
        Recibe como parametro el nombre de los vértices de inicio 's' y final 't'
        Devuelve una lista con los nombres de los vértices de la ruta.
    '''
    def rutaAumentante(self,s, t):
        i_s = self.vertices.index(s)
        i_t = self.vertices.index(t)
        print("ORIGEN: "+str(i_s)+" - DESTINO: "+str(i_t))
        stack = []
        stack.append(i_s)
        visitados = []
        while stack != []:
            print("")
            print("- Stack: "+str(stack))
            print("< Visitados: "+str(visitados))
            actual = stack.pop()
            print("o Actual: "+ str(actual))
            if actual == i_t:
                print("LLegamos al destino")

            if actual not in visitados:
                visitados.append(actual)

                for vecino in range(actual, len(self.vertices)-1):
                    if self.matrix[actual][vecino] != 0:
                        stack.append(vecino)
        return []                        
                



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
        
        for v in vertices: # para cada vértice agregamos su lista de vecinos
            vecinos = []
            vecinos.append([v, 0])
            for a in aristas: # buscamos sobre las aristas la que inicie con el vértice actual
                if v == a[0]:
                    vecinos.append([a[1], a[2]]) # agregamos el vértice vecino a su lista de vecinos

            self.lista.append([vecinos]) # guardamos la lista con el nodo y su lista de vecinos
        
        self.residual = self.lista

    '''

    '''
    def imprime_grafica(self):
        for vertice in self.lista:
            print(str(vertice)+"\n")
    
    '''
    
    '''
    def graficaRandom(self, n_nodos):
        
        vertices = []
        aristas = []

        matrix = np.zeros((n_nodos, n_nodos))
        for i in range(0, n_nodos-1):
            vertices.append(str(i))
            for j in range(i+1, n_nodos): 
                matrix[i][j] = random.randrange(2, 20)
                aristas.append((str(i), str(j), matrix[i][j]))
        vertices.append(str(n_nodos-1))

        self.lista = [] #lista para la listas de los nodos con sus tuplas de aristas
        
        for v in vertices: # para cada vértice agregamos su lista de vecinos
            vecinos = []
            vecinos.append([v, 0])
            for a in aristas: # buscamos sobre las aristas la que inicie con el vértice actual
                if v == a[0]:
                    vecinos.append([a[1], a[2]]) # agregamos el vértice vecino a su lista de vecinos

            self.lista.append([vecinos]) # guardamos la lista con el nodo y su lista de vecinos


    '''
        Método donde se implementa el algoritmo de Ford Fulkerson
        Recibe como parámetros un nodo S (fuente) y T (pozo) en la gráfica
    '''    
    def FordF(self, s, t):
        self.rutaAumentante(s, t)


    '''
        Método que encuentra una ruta dentro de la gráfica de S a T, 
        donde es la ruta con las aristas de capacidad máxima. 
        Regresa un tupla que tiene una lista de los indices de los nodos y 
        un valor 'delta' el mínimo de las máximas capacidades
    '''
    def rutaAumentante(self, s, t):
        vertices = {}
        for vertice in self.lista:
            print(str(vertice))
            vertices[vertice[0][0][0]] = [None, '', False, vertice[0][1:]] #distancia, padre, visitado
        
        vertices[s][0] = 0
        cola = deque([])
        cola.append([s, 0])
        print(str(vertices))
        print(str(cola))

        while len(cola) != 0:
            actual = cola.popleft()
            vertices[actual[0]][2] = True

            if actual[0] == t:
                print("LLEGAMOS A T")
                break

            for vecino in vertices[actual[0]][3]:
                print (str(vecino))
                if vertices[vecino[0]][2] == False:
                    print("Vecinos no visitados "+str(vecino[0]))
                    if vertices[vecino[0]][0] < actual[1] + vecino[1]:
                        vertices[vecino[0]][0] = vertices[actual[0]][0] + vecino[1]
                        vertices[vecino[0]][1] = actual[0]
                        cola.append([vecino[0], vertices[vecino[0]][0]])

        for x in vertices:
            print(x+":"+str(vertices[x]))

        ruta = []
        v = vertices[t] 
        print("PADRE DE T:"+str(v[1]))
        ruta.append(t)
        padre = v[1]

        if padre == '':
            print("NO HAY RUTA")
            return ([], 0)

        while v[1] != '':
            ruta.append(padre)
            print("Padre"+str(padre))
            v = vertices[padre]
            print("Siguinte: "+ str(v[1]))
            padre = v[1]
        
        print("RUTA CREADA")
        ruta.reverse()
        print(ruta)
        return(ruta, 0)

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
    nx.draw(G, node_color = '#ffa987')
    plt.show()
'''


    pos=nx.spring_layout(G) # positions for all nodes
    # nodes
    nx.draw_networkx_nodes(G,pos,
                        nodelist=grafica.vertices,
                        node_color='#ffa987',
                        node_size=500,
                    alpha=0.8)
    nx.draw_networkx_edges(G,pos,width=1.0,alpha=0.5)                
    nx.draw_networkx_edges(G,pos,
                        edgelist=grafica.aristas,
                        width=3,alpha=0.5,edge_color='#444140')                   
    #nx.draw(G)
    nx.draw_networkx_labels(G,pos,font_size=16)
    plt.axis('off')
    #plt.savefig("grafica.png")
    plt.show()
'''

'''
D = nx.gn_graph(10)  # the GN graph
nx.draw(D)
plt.show()
'''

'''
Grafica = GraficaListas(['s', 'u', 'v', 'w','x', 'y', 'z', 't'], 
[('s', 'u', 1),
('s', 'w', 3),
('u', 'w', 5),
('v', 'u', 3),
('w', 'v', 2),
('w', 'x', 8),
('w', 't', 2),
('x', 's', 2),
('x', 'y', 6),
('y', 'w', 3),
('y', 'z', 5),
('z', 'w', 3),
('z', 't', 4),
('t', 'v', 3)])
'''
#Grafica.imprime_grafica()
Grafica = GraficaListas([], [])
Grafica.graficaRandom(6)
Grafica.imprime_grafica()
#Grafica.rutaAumentante('0','5')
Grafica.FordF('0', '5')

'''
AQUI VA LA GRAFICA DE MATRICES
GraficaRandom = GraficaMatriz([],[])
n_nodos = input("Ingresa una Cantidad de nodos: ")
GraficaRandom.graficaRandom(n_nodos)
GraficaRandom.imprime_grafica()
nodo_fuente = '0'
nodo_pozo = str(n_nodos-1)
GraficaRandom.rutaAumentante(nodo_fuente, nodo_pozo)
#GraficaRandom.FordF(nodo_fuente, nodo_pozo)
visualizarGrafica(GraficaRandom)
#print(GraficaRandom.vertices)

#Grafica.rutaAumentante('s', 't')
'''



'''
G_listas = GraficaListas(['A', 'B', 'C'], [('A', 'B', 1), ('B', 'C', 2), ('C', 'A', 3)])
G_listas.imprime_grafica()
'''
