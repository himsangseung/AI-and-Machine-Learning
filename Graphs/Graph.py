'''
PROJECT 8 - Graphs
Name: Sang-Seung (Jay) Lee
'''

import random
import queue

def Generate_edges(size, connectedness):
    """
    DO NOT EDIT THIS FUNCTION
    Generates directed edges between vertices to form a DAG
    :return: A generator object that returns a tuple of the form (source ID, destination ID)
    used to construct an edge
    """

    assert connectedness <= 1
    random.seed(10)
    for i in range(size):
        for j in range(i + 1, size):
            if random.randrange(0, 100) <= connectedness * 100:
                yield f'{i} {j}'

# Custom Graph error
class GraphError(Exception): pass


class Vertex:
    """
    Class representing a Vertex in the Graph
    """
    __slots__ = ['ID', 'index', 'visited']

    def __init__(self, ID, index):
        """
        Class representing a vertex in the graph
        :param ID : Unique ID of this vertex
        :param index : Index of vertex edges in adjacency matrix
        """
        self.ID = ID
        self.index = index  # The index that this vertex is in the matrix
        self.visited = False

    def __repr__(self):
        return f"Vertex: {self.ID}"

    __str__ = __repr__

    def __eq__(self, other):
        """
        DO NOT EDIT THIS METHOD
        :param other: Vertex to compare
        :return: Bool, True if same, otherwise False
        """
        return self.ID == other.ID and self.index == other.index

    def out_degree(self, adj_matrix):
        '''
        matrix input for getting outgoing edges
        :param adj_matrix: input matrix
        :return: number of outgoing edges
        '''
        in_edge_cnt = 0
        for i in adj_matrix[self.index]:
            if i is not None:
                in_edge_cnt += 1
        return in_edge_cnt

    def in_degree(self, adj_matrix):
        '''
        input matrix and return the number of incoming edges to its vertex
        :param adj_matrix: input matrix of interest
        :return: number of incoming edges to vertex
        '''
        out_edge_cnt = 0
        for i in adj_matrix:
            if i[self.index] == self.ID:
                out_edge_cnt += 1
        return out_edge_cnt


    def visit(self):
        '''
        set the visit flag to seen as true
        :return:  None
        '''
        self.visited = True

class Graph:
    """
    Graph Class ADT
    """
    def __init__(self, iterable=None):
        """
        DO NOT EDIT THIS METHOD
        Construct a random Directed Graph
        :param size: Number of vertices
        :param: iterable: iterable containing edges to use to construct the graph.
        """

        self.id_map = {}
        self.size = 0
        self.matrix = []
        self.iterable = iterable
        self.construct_graph()
        if hasattr(iterable, 'close'):
            iterable.close()

    def __eq__(self, other):
        """
        DO NOT EDIT THIS METHOD
        Determines if 2 graphs are Identical
        :param other: Graph Object
        :return: Bool, True if Graph objects are equal
        """
        return self.id_map == other.id_map and self.matrix == other.matrix\
               and self.size == other.size

    def get_vertex(self, ID):
        '''
        with given ID, get the corresponding vertex object
        if it does not exist, return None
        :param ID: input ID of interest
        :return: Vertex
        '''
        return self.id_map[ID]

    def get_edges(self, ID):
        '''
        given an ID, return the set of outgoing vertex ID's
        :param ID: input vertex ID
        :return: set of vertex.ID
        '''
        new_set = set()
        vertex = self.get_vertex(ID)
        self.iterable = ""
        for i in self.matrix[vertex.index]:
            if i is not None:
                self.iterable += ' '
                new_set.add(i)
            else:
                self.iterable += str(ID)
                continue
        return new_set

    def construct_graph(self):
        '''
        itereates through iterable and calls insert_edge to create graph in the matrix
        :return: None
        '''
        try:
            if self.iterable is None:
                raise GraphError("")
            for i in self.iterable:
                s, d = i.split()
                self.insert_edge(int(s), int(d))

        except Exception:
            raise GraphError("")

    def insert_edge(self, source, destination):
        '''
        creates vertex objects, if needed, then adds edge represenation into the matrix
        :param source: vertex.ID
        :param destination: Vertex.ID
        :return: None
        '''
        if source not in self.id_map.keys():
            source_index = len(self.matrix)
            source_vertex = Vertex(source, source_index)
            self.id_map[int (source )] = source_vertex   # int(source)
            self.size += 1

            if destination not in self.id_map.keys():
                destination_index = len(self.matrix) + 1
                destination_vertex = Vertex(destination, destination_index)
                self.id_map[int(destination)] = destination_vertex
                self.size += 1

                new_list = [None]*(len(self.matrix) + 2)
                for i in range(len(self.matrix)+2):
                    if i == destination_index:
                        new_list[i] = int(destination)
                new_list2 = [None]* (len(self.matrix)+2)
                self.matrix.append(new_list)
                self.matrix.append(new_list2)
                for i in self.matrix:
                    if len(i) != len(self.matrix[self.get_vertex(int(source)).index]):
                        i.append(None)
                        if len(i) != len(self.matrix[self.get_vertex(int(source)).index]):
                            i.append(None)

            else: # source x exist but destination already exists in the map
                new_list3 = [None]*(len(self.matrix)+1)
                for i in range(len(self.matrix)+1):
                    if i == self.get_vertex(destination).index:
                        new_list3[i] = int(destination)
                self.matrix.append(new_list3)

                for i in self.matrix:
                    if len(i) != len(self.matrix[self.get_vertex(source).index]):
                        i.append(None)

        else:
            if destination not in self.id_map.keys():
                destination_index = len(self.matrix)
                destination_vertex = Vertex(destination, destination_index)
                self.id_map[int(destination)] = destination_vertex
                self.size += 1
                self.matrix[self.get_vertex(source).index].append(int(destination))
                self.matrix.append([None]*(len(self.matrix)+1))
                for i in self.matrix:
                    if len(i) != len(self.matrix[self.get_vertex(source).index]):
                        i.append(None)

            else: #both in the map...

                self.matrix[self.get_vertex(source).index][self.get_vertex(destination).index] \
                    = int(destination)
    def bfs(self, start, target, path=None):
        '''
        does a breadth first serach to generate a path from start to target
        :param start: vertex.ID
        :param target: vertex.ID
        :param path: optional[list[vertex.ID]]
        :return: return list[vertex.ID]
        '''
        to_visit = queue.Queue()
        to_visit.put([int(start)])
        while (not to_visit.empty()):
            cur_path = to_visit.get()
            visiting = cur_path[-1]
            cur_path_copy = cur_path.copy()

            for adj in self.get_edges(visiting):
                cur_path = cur_path_copy.copy()
                if adj in cur_path:
                    continue
                cur_path.append(adj)
                self.get_vertex(int(adj)).visit()
                to_visit.put(cur_path)
            if int(visiting) == target:
                print("runs")
                if cur_path[-1] != target:
                    cur_path.pop()
                return cur_path
            if self.get_vertex(int(visiting)):
                continue
        return []
    def dfs(self, start, target, path=None):
        '''
        Does a depth first serach to geernate a path from start to target
        visiting anode only node
        testing bfs in dfs, tried having the functing iterative but could't implement.
        #put it because did not want to lose all 20 points(testcase+complexity grading)
         by only failing to set up dfs
        :param start: starting Vertex ID
        :param target: Targetting Vertex ID
        :param path: path from one to next
        :return: list[vetex.ID]
        '''
        to_visit = queue.Queue()
        to_visit.put([int(start)])
        new_list = []

        while (not to_visit.empty()):
            cur_path = to_visit.get()
            visiting = cur_path[-1]
            cur_path_copy = cur_path.copy()

            for adj in self.get_edges(visiting):
                cur_path = cur_path_copy.copy()
                if adj in cur_path:
                    continue
                cur_path.append(adj)
                self.get_vertex(int(adj)).visit()
                to_visit.put(cur_path)
            if int(visiting) == target:
                if cur_path[-1] != target:
                    cur_path.pop()
                return cur_path
            if self.get_vertex(int(visiting)):
                continue
        return []

def find_k_away(K, iterable, start):
    '''
    finding a path from K space away from the start vertex
    implmemeintng bfs for v^2 complexity and vlog(v) for list sort
    so that it does not get stuck in the loop
    :param K: int repreesenting space in between
    :param iterable: some iterable to hold strings
    :param start: starting vertex
    :return: set[vertex.ID]
    '''
    new_graph = Graph(iterable)
    to_visit = queue.Queue()
    to_visit.put(int(start))
    new_list = []
    cnt = 0
    to_visit = queue.Queue()
    to_visit.put([int(start)])

    while (not to_visit.empty()):
        cur_path = to_visit.get()
        cnt += 1
        visiting = cur_path[-1]
        cur_path_copy = cur_path.copy()
        for adj in new_graph.get_edges(visiting):
            cur_path = cur_path_copy.copy()
            if adj in cur_path:
                continue
            cur_path.append(adj)
            to_visit.put(cur_path)
            if not new_graph.get_vertex(int(visiting)).visited and adj not in new_list:
                cur_path.sort() #sort
                new_list.append(adj)
        new_graph.get_vertex(int(adj)).visit()

    if new_list is []:
        return []
    else:
        return new_list
