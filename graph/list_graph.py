"""Implementing Graph in adjacent list"""


class Vertex:
    def __init__(self, key):
        self.id = key
        self.connect_to = {}

    def __str__(self):
        return "".join((str(self.id), ":", str([i for i in self.connect_to])))

    def add_neighbor(self, nbr, weight=0):
        """Add a connection from this vertex to another"""
        self.connect_to[nbr] = weight

    def get_connections(self):
        """Return all vertices in the adjacency list"""
        return self.connect_to.keys()

    def get_weight(self, nbr):
        """Return the weight of the edge from this vertex to the vertex passed as a parameter"""
        return self.connect_to[nbr]

    def get_id(self):
        return self.id


class Graph:
    """Holds the master list of vertices
    Maps vertex names to vertex object"""

    def __init__(self):
        self.vert_list = {}
        self.vert_num = 0

    def add_vertex(self, key):
        self.vert_num += 1
        new_vertex = Vertex(key)
        self.vert_list[key] = new_vertex
        return new_vertex

    def get_vertex(self, key):
        if key in self.vert_list:
            return self.vert_list[key]
        else:
            return None

    def __contains__(self, key):
        return key in self.vert_list

    def add_edge(self, from_key, to_key, weight=0):
        if from_key not in self.vert_list:
            self.add_vertex(from_key)
        if to_key not in self.vert_list:
            self.add_vertex(to_key)
        from_v = self.vert_list[from_key]
        from_v.add_neighbor(self.vert_list[to_key], weight)

    def get_vertices(self):
        return self.vert_list.keys()

    def __iter__(self):
        """Loop over all the vertex objects in a graph"""
        return iter(self.vert_list.values())
