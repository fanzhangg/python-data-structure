"""
Breadth First Search:
- proceeds by exploring edges in the graphs to find all the vertices in G if v has a path to G.
- find all the vertices that are a distance k from s before find the vertice that is a distance k+1.
- build a tree on level at a time
- adds all children before add a grandchild
- color each v as white, grey, or black
    - initially white
    - grey if initially discovered
    - black after BFS has completely explored a vertex
    - -> v is black, no adjacent white u
- uses an extended version of the Vertex
    - distance
    - predecessor
    - color
"""

from queue import Queue

from list_graph import Vertex


def bfs(start: Vertex):
    start.distance = 0
    v_queue = Queue()
    v_queue.put(start)
    while not v_queue.empty():
        curr_v = v_queue.get()
        for nbr in curr_v.get_out_neighbors():
            if not nbr.color:
                nbr.color = 'g'
                nbr.distance = curr_v.distance + 1
                nbr.add_in_neighbor(curr_v)
                v_queue.put(nbr)
        curr_v.color = 'b'
