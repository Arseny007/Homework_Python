import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from pprint import pprint
###########################################################################################
# рисование обычного графа
graph = nx.Graph()              # создание объекта граф
# С направленным графом то же самое, только объект создается nx.DiGraph()
for i in range(1, 6):
    graph.add_node(i)           # создание пяти узлов циклом

graph.add_edge(1, 2)            # связывает 1 и 2 узел
graph.add_edge(2, 3)            # - 2 и 3
graph.add_edge(4, 5)

adjency_matrix = nx.to_numpy_matrix(graph)  # матрица смежности для графа в виде списка списков numpy
print('матрица смежности 1 графа\n', adjency_matrix)

nx.draw_circular(graph, node_size=2000, with_labels=True)   # рисует граф, with_abels - подписывает узлы

plt.show()                      # выводит нарисованное
#############################################################################################
# создание графа из матрицы смежности

matrix_for_g = np.array([[1]*(5-i)+[0]+[1]*i for i in range(5, -1, -1)])

print('\n\nматрица полносвязного графа\n', matrix_for_g)
g_from_list = nx.from_numpy_matrix(matrix_for_g)    # полносвязный граф из 6 узлов
nx.draw_circular(g_from_list)

plt.show()
##############################################################################################
# алгоритм дейкстры для кратчайшего пути и добавление взвешенных граней из списка кортежей

dirgraph = nx.DiGraph()
for i in ['a', 'b', 'c', 'd', 'e', 'f', 'g']:
    dirgraph.add_node(i)

# Обозначаем связи и вес
e = [('a', 'b', 2),
     ('a', 'c', 5),
     ('b', 'c', 2),
     ('b', 'f', 8),
     ('c', 'd', 3),
     ('c', 'e', 4),
     ('d', 'f', 3),
     ('d', 'e', 2),
     ('e', 'g', 4),
     ('f', 'g', 2)]
for i in e:
     dirgraph.add_weighted_edges_from(i[0], i[1], capacity=i[2], weight=i[2]) # подаем список

print('\n\nближайший путь: ', nx.dijkstra_path(dirgraph, 'a', 'g'), '\nвес этого пути: ', nx.dijkstra_path_length(dirgraph, 'a', 'g'))

flow_value, flow_dict = nx.maximum_flow(dirgraph, 'a', 'g')
print(flow_value)
pprint(flow_dict)

pos = nx.spring_layout(dirgraph)
nx.draw(dirgraph, pos, with_labels=True)
labels = nx.get_edge_attributes(dirgraph, 'weight')
nx.draw_networkx_edge_labels(dirgraph, pos, edge_labels=labels)     # подписывает связи

plt.show()