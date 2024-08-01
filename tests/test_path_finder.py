from shortestpath.path_finder import find_paths, bfs


def test_find_paths(dummy_graph):
    """
    Test path_finder.
    """
    actual = find_paths(dummy_graph)
    expected =  [(0, {1}), (1, {2, 4}), (2, {3}), (4, set()), (3, set())]
    assert actual == expected


def test_bfs(dummy_graph):
    """
    Test BFS implementation.
    """
    paths = []
    visited = set()
    nodes = list(dummy_graph.nodes())
    for node in nodes:
        if node not in visited:
            bfs(dummy_graph, node, visited, paths)

    expected =  [(0, {1}), (1, {2, 4}), (2, {3}), (4, set()), (3, set())]
    assert paths == expected

