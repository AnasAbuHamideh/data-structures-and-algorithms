class Node:

    def __init__(self,value):
        self.value = value

class Edge:

  def __init__(self, vertex, weight):
    self.vertex = vertex
    self.weight = weight

class Graph:

    def __init__(self):
         self.__adjacency_list = {}

    def add_node(self, value):
        v = Node(value)
        self.__adjacency_list[v] = []
        return v

    def add_edge(self, start_vertex, end_vertex, weight=0):
        if start_vertex not in self.__adjacency_list:
            raise KeyError("Start Vertex not found in graph")
      
        if end_vertex not in self.__adjacency_list:
            raise KeyError("End Vertex not found in graph")

        edge = Edge(end_vertex, weight)
        self.__adjacency_list[start_vertex].append(edge)


    def get_nodes(self):
        return self.__adjacency_list.keys()
    
    def get_neighbors(self, vertex):
        return self.__adjacency_list.get(vertex, [])

    def size(self):
        return len(self.__adjacency_list)

