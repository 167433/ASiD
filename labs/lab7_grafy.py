import math
from enum import Enum
from typing import Any
from typing import Optional
from typing import Dict, List
from graphviz import Digraph as Groph

class EdgeType(Enum):
    directed = 1
    undirected = 2

class Vertex:
    data: Any
    index: int

    def __init__(self,data):
        self.data = data

class Edge:
    source: Vertex
    destination: Vertex
    weight: Optional[float]

    def __init__(self,source:Vertex, destitantion:Vertex, weight:Optional):
        self.source = source
        self.destination = destitantion
        self.weight = weight

class Queue:

    def __init__(self):
        self.__queue = []

    def put(self,value:Any):
        self.__queue.append(value)

    def get(self):
        return self.__queue.pop(0)

    def empty(self):
        if len(self.__queue) == 0:
            return True
        else:
            return False

class Graph:
    adjacencies: Dict[Vertex, List[Edge]]

    def __init__(self):
        self.adjacencies = {}

    def create_vertex(self, data: Any):
        vertex = Vertex(data)
        self.adjacencies[vertex] = []
        return vertex

    def add_directed_edge(self, source:Vertex, destination:Vertex, weight:Optional[float] = None):
        edge = Edge(source,destination,weight)
        self.adjacencies[source].append(edge)

    def add_undirected_edge(self, source: Vertex, destination: Vertex, weight: Optional[float] = None):
        edge = Edge(source,destination,weight)
        self.adjacencies[source].append(edge)

        edge = Edge(destination,source,weight)
        self.adjacencies[destination].append(edge)

    def add(self, edge: EdgeType, source: Vertex, destination: Vertex, weight: Optional[float] = None) -> None:
        if edge == EdgeType.directed:
            self.add_directed_edge(source, destination, weight)
        else:
            self.add_undirected_edge(source, destination, weight)


    def traverse_breadth_first(self,visit):
        if len(self.adjacencies.keys())>0:

            q = Queue()
            visited = []
            q.put(list(self.adjacencies.keys())[0])
            visited.append(list(self.adjacencies.keys())[0])

            while not q.empty():
                one_el = q.get()
                visit(one_el.data)
                for egde in self.adjacencies[one_el]:
                    if egde.destination not in visited:
                        visited.append(egde.destination)
                        q.put(egde.destination)
        else:
            return None

    def deepth_first_travel(self,visit):
        vertexs = [x for x in self.adjacencies.keys()]
        visited = []
        visited.append(vertexs[0])
        visit(vertexs[0].data)

        for i in range(len(vertexs)):
            self._dfs(vertexs[i],visited, visit)

    def _dfs(self,v:Vertex,visited:List[Vertex], visit: Any):
        for egde in self.adjacencies[v]:
            if egde.destination not in visited:
                visit(egde.destination.data)
                visited.append(egde.destination)
                self._dfs(egde.destination,visited,visit)

    def show(self):
        for ver, edge in self.adjacencies.items():
            edge_str = ""
            for ed in edge:
                edge_str += str(ed.destination.data) + " "
            print(f'{ver.data,edge_str}')

class GraphPath:

    graph: 'Graph'

    def __init__(self,graph: Graph):
        self.graph = graph

    def dijkstra(self,start,goal):

        shorest_distance = {}
        parent = {}
        unseenNodes = self.graph.adjacencies
        path = []

        for node in unseenNodes.keys():
            shorest_distance[node] = math.inf
        shorest_distance[start] = 0

        while unseenNodes:
            minNode = None
            for node in unseenNodes:
                if minNode is None:
                    minNode = node
                elif shorest_distance[node] < shorest_distance[minNode]:
                    minNode = node

            for edge in self.graph.adjacencies[minNode]:
                if edge.weight + shorest_distance[minNode] < shorest_distance[edge.destination]:
                    shorest_distance[edge.destination] = edge.weight + shorest_distance[minNode]
                    parent[edge.destination] = minNode

            unseenNodes.pop(minNode)

        currentNode = goal
        while currentNode != start:
            try:
                path.insert(0,currentNode)
                currentNode = parent[currentNode]

            except KeyError:
                print("Path not reachable")
                break

        path.insert(0,start)

        if shorest_distance[goal] != math.inf:
            print(f'shortast distance is {shorest_distance[goal]}')
            arr_path = []
            for el in path:
                arr_path.append(el.data)
            print(f'Path is {arr_path}')

    def wszerz(self,start,goal):
        q = Queue()
        path = []
        path.append(start)
        q.put(path)
        visited = []
        visited.append(start)

        while not q.empty():
            current_path = q.get()
            current_vertex = current_path[-1]
            new_path = []

            if goal in current_path:
                for ver in current_path:
                    print(f'{ver.data} new path')
                return current_path

            for neighobr in self.graph.adjacencies[current_vertex]:

                if neighobr.destination not in visited:
                    if neighobr.destination != None:
                        new_path = new_path+current_path
                        new_path.append((neighobr.destination))
                        visited.append(neighobr.destination)
                        q.put(new_path)

                    if goal not in new_path:
                        new_path = []



graph = Graph()
vertex_1 = graph.create_vertex(1)
vertex_2 = graph.create_vertex(2)
vertex_3 = graph.create_vertex(3)
vertex_4 = graph.create_vertex(4)
vertex_5 = graph.create_vertex(5)
# vertex_6 = graph.create_vertex(6)

# first_value = list(graph.adjacencies.keys())[0]
# print(first_value.data)

directed = EdgeType.directed
undirected = EdgeType.undirected

graph.add(directed,vertex_1,vertex_2,1)
graph.add(directed,vertex_1,vertex_3,5)
graph.add(directed,vertex_1,vertex_4,3)
graph.add(directed,vertex_3,vertex_4,3)
graph.add(directed,vertex_3,vertex_5,3)


# graph.deepth_first_travel(print)
# print(graph.adjacencies)
#graph.show()

g_path = GraphPath(graph)
print(g_path.wszerz(vertex_1,vertex_3))