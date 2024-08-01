import networkx as nx
import pytest

@pytest.fixture(scope="session")
def dummy_graph():
    # Create an adjacency dict for the graph shown below.
    #
    #    2 ---- 1 ---- 0
    #    |  \   |
    #    |   \  |
    #    3      4
    #
    adjacency_dict = {0: (1,), 1: (0,2,4), 2: (1,3,4), 3: (2,), 4: (1,2)}
    graph = nx.Graph(adjacency_dict)
    return graph