"""Implementing Graph in adjacent list"""


class Vertex:
    def __init__(self, value):
        self.value = value
        self.color = None
        self.distance = 0

        # variables related to neighbors
        self.out_neighbors = {}
        self.in_neighbors = {}
        self.indegree = len(self.in_neighbors)
        self.outdegree = len(self.out_neighbors)
        self.degree = self.indegree + self.outdegree

    def __str__(self):
        """
        :return: i.e. "1 (color: "white", out-neighbors: [a, b, c], in-neighbors: [d]"
        """
        try:
            out_neighbors_list = str([str(v.value) for v in self.out_neighbors.keys()])
        except AttributeError:
            out_neighbors_list = "[]"

        try:
            in_neighbors_list = str([str(v.value) for v in self.in_neighbors.keys()])
        except AttributeError:
            in_neighbors_list = "[]"

        return "".join((str(self.value), " (",
                        "color:", str(self.color),
                        "\tout:", out_neighbors_list,
                        "\tin:", in_neighbors_list,
                        ")"))

    def add_in_neighbor(self, in_nbr, weight=0):
        """Add a in-neighbor: in_nbr has an edge to current vertex"""
        self.in_neighbors[in_nbr] = weight

    def add_out_neighbor(self, out_nbr, weight=0):
        """Add a out-neighbor: out_nbr with an edge from current vertex"""
        self.out_neighbors[out_nbr] = weight

    def get_out_neighbors(self):
        """Return all connected vertices"""
        return self.out_neighbors.keys()

    def get_weight(self, nbr):
        """Return the weight of the edge from this vertex to the vertex passed as a parameter"""
        return self.out_neighbors[nbr]


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
        from_v.add_out_neighbor(self.vert_list[to_key], weight)

    def add_undirected_edge(self, key1, key2, weight=0):
        if key1 not in self.vert_list:
            self.add_vertex(key1)
        if key2 not in self.vert_list:
            self.add_vertex(key2)
        v1 = self.vert_list[key1]
        v2 = self.vert_list[key2]
        v1.add_out_neighbor(self.vert_list[key2], weight)
        v2.add_out_neighbor(self.vert_list[key1], weight)

    def get_vertices(self):
        return self.vert_list.keys()

    def __iter__(self):
        """Loop over all the vertex objects in a graph"""
        return iter(self.vert_list.values())
