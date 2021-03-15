#
# Module: cidades
# 
# Implements a SearchDomain for find paths between cities
# using the tree_search module
#
# (c) Luis Seabra Lopes
# Introducao a Inteligencia Artificial, 2012-2020
# Inteligência Artificial, 2014-2020
#

import math

from tree_search import *
from timeit import timeit

class Cidades(SearchDomain):
    def __init__(self,connections, coordinates):
        self.connections = connections
        self.coordinates = coordinates
        
    def actions(self,city):
        actlist = []
        for (C1,C2,D) in self.connections:
            if (C1==city):
                actlist += [(C1,C2)]
            elif (C2==city):
               actlist += [(C2,C1)]
        return actlist 
    def result(self,city,action):
        (C1,C2) = action
        if C1==city:
            return C2
    
    def cost(self, city, action):
        for (c1,c2,d) in self.connections:
            if (c1,c2) == action or (c2,c1) == action:
                return d
        return None    
        
    def heuristic(self, city, goal_city):
        (c1_x,c1_y) = self.coordinates[city] 
        (c2_x,c2_y) = self.coordinates[goal_city]
        
        return math.hypot(c1_x - c2_x, c1_y - c2_y)
    
    def satisfies(self, city, goal_city):
        return goal_city==city


cidades_portugal = Cidades( 
                    # Ligacoes por estrada
                    [
                      ('Coimbra', 'Leiria', 73),
                      ('Aveiro', 'Agueda', 35),
                      ('Porto', 'Agueda', 79),
                      ('Agueda', 'Coimbra', 45),
                      ('Viseu', 'Agueda', 78),
                      ('Aveiro', 'Porto', 78),
                      ('Aveiro', 'Coimbra', 65),
                      ('Figueira', 'Aveiro', 77),
                      ('Braga', 'Porto', 57),
                      ('Viseu', 'Guarda', 75),
                      ('Viseu', 'Coimbra', 91),
                      ('Figueira', 'Coimbra', 52),
                      ('Leiria', 'Castelo Branco', 169),
                      ('Figueira', 'Leiria', 62),
                      ('Leiria', 'Santarem', 78),
                      ('Santarem', 'Lisboa', 82),
                      ('Santarem', 'Castelo Branco', 160),
                      ('Castelo Branco', 'Viseu', 174),
                      ('Santarem', 'Evora', 122),
                      ('Lisboa', 'Evora', 132),
                      ('Evora', 'Beja', 105),
                      ('Lisboa', 'Beja', 178),
                      ('Faro', 'Beja', 147),
                      # extra
                      ('Braga', 'Guimaraes', 25),
                      ('Porto', 'Guimaraes', 44),
                      ('Guarda', 'Covilha', 46),
                      ('Viseu', 'Covilha', 57),
                      ('Castelo Branco', 'Covilha', 62),
                      ('Guarda', 'Castelo Branco', 96),
                      ('Lamego','Guimaraes', 88),
                      ('Lamego','Viseu', 47),
                      ('Lamego','Guarda', 64),
                      ('Portalegre','Castelo Branco', 64),
                      ('Portalegre','Santarem', 157),
                      ('Portalegre','Evora', 194) ],

                    # City coordinates
                     { 'Aveiro': (41,215),
                       'Figueira': ( 24, 161),
                       'Coimbra': ( 60, 167),
                       'Agueda': ( 58, 208),
                       'Viseu': ( 104, 217),
                       'Braga': ( 61, 317),
                       'Porto': ( 45, 272),
                       'Lisboa': ( 0, 0),
                       'Santarem': ( 38, 59),
                       'Leiria': ( 28, 115),
                       'Castelo Branco': ( 140, 124),
                       'Guarda': ( 159, 204),
                       'Evora': (120, -10),
                       'Beja': (125, -110),
                       'Faro': (120, -250),
                       #extra
                       'Guimaraes': ( 71, 300),
                       'Covilha': ( 130, 175),
                       'Lamego' : (125,250),
                       'Portalegre': (130,170) }
                     )




p = SearchProblem(cidades_portugal,'Viseu','Faro')

t = SearchTree(p,'depth')
t2 = SearchTree(p,'breadth')
t3 = SearchTree(p,'uniform')
t4 = SearchTree(p, 'greedy')
t5 = SearchTree(p, 'a*')

print("\n=== depth ===")
print(t.search())
print(timeit(lambda: t.search(), number=10))
print(t.length, t.cost, t.avg_ramification)

print("\n=== breadth ===")
print(t2.search())
print(timeit(lambda: t2.search(), number=10))
print(t2.length, t2.cost, t2.avg_ramification)

print("\n=== uniform ===")
print(t3.search())
print(timeit(lambda: t3.search(), number=10))
print(t3.length, t3.cost, t3.avg_ramification)

print("\n=== greedy ===")
print(t4.search())
print(timeit(lambda: t4.search(), number=10))
print(t4.length, t4.cost, t4.avg_ramification)

print("\n=== a* ===")
print(t5.search())
print(timeit(lambda: t5.search(), number=10))
print(t5.length, t5.cost, t5.avg_ramification)

# Atalho para obter caminho de c1 para c2 usando strategy:
def search_path(c1,c2,strategy):
    my_prob = SearchProblem(cidades_portugal,c1,c2)
    my_tree = SearchTree(my_prob)
    my_tree.strategy = strategy
    return my_tree.search()


