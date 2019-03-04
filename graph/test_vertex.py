import unittest

import list_graph


class MyTestCase(unittest.TestCase):
    def test_add_neighbor(self):
        v = list_graph.Vertex(1)
        v.add_neighbor(2, 5)
        v.add_neighbor(3, 3)
        self.assertEqual(v.connect_to, {2: 5, 3: 3})

    def test_get_connections(self):
        v = list_graph.Vertex(1)
        v.add_neighbor(2, 5)
        v.add_neighbor(3, 3)
        self.assertEqual([i for i in v.get_connections()], [2, 3])

    def test_get_id(self):
        v = list_graph.Vertex(1)
        self.assertEqual(v.get_id(), 1)

    def test_get_weight(self):
        v = list_graph.Vertex(1)
        v.add_neighbor(2, 5)
        v.add_neighbor(3, 3)
        self.assertEqual(v.get_weight(2), 5)


if __name__ == '__main__':
    unittest.main()
