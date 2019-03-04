import unittest

from list_graph import Graph


class TestListGraph(unittest.TestCase):
    def test_add_vertex(self):
        g = Graph()
        g.add_vertex(1)
        self.assertEqual(g.vert_list[1].id, 1)
        self.assertEqual(g.vert_num, 1)

    def test_get_vertex(self):
        g = Graph()
        g.add_vertex(1)
        self.assertEqual(g.get_vertex(1).id, 1)
        self.assertEqual(g.get_vertex(0), None)

    def test_add_edge(self):
        g = Graph()
        g.add_vertex(1)
        g.add_edge(1, 2, 3)
        to_v = g.get_vertex(1).connect_to
        values, keys = to_v.values(), to_v.keys()
        self.assertEqual(list(keys)[0].id, 2)
        self.assertEqual(list(values)[0], 3)

if __name__ == '__main__':
    unittest.main()
