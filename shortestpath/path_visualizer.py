"""Visualization of Shortest Path Visiting All Nodes in a Graph

For a given graph, the shortest path visiting all nodes in it is discovered and visualized with an animation. 
The Breadth-First-Search (BFS) algorithm is used to find the shortest path to all nodes in an unweighted undirected graph. 

A new graph will be randomly created for each animation so that users can observe how the shortest path to all nodes 
can be identified in various graphs. 

At the beginning of each animation, all the nodes and the edges of the graph are displayed in blue and black colors, respectively. 
BFS starts at a source node and visits all the adjacent nodes. Then for each of those adjacent nodes, it explores their unexplored neighbor nodes 
and so on, until all the nodes in the graph are explored. The randomly generated graph sometimes might have multiple components. 
All of them will be explored if there are.

The time complexity of BFS is O(n + m), where n is the number of nodes and m is the number of edges in the graph. 
BFS visits each node and traverses each edge once, ensuring a comprehensive graph exploration. 
This makes its performance linear to the graph's size, providing a predictable upper time limit.

For the purpose of visualization, the node's color will be changed as DFS makes progress in searching the shortest path to all nodes in the graph.
Here is the list of the color codes for visualization:
    * Node's initial color: Blue
    * Edge's initial color: Black
    * Current node's marker: Green
    * Discovered neighbor node's color: Orange
    * Shortest path color: Red

This animation may help users understand how BFS finds the shortest path to all nodes in an unweighted undirected graph.
Please feel to use it and enjoy it! Any contribution will be welcome. Please check out the contributing guidelines if you wish to make.

"""

import logging
from typing import Collection, Dict, List, Optional, Set, Tuple, Union

import random
import string
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from shortestpath.path_finder import find_paths

logger = logging.getLogger(__name__)

logging.basicConfig(filename='shortestpath.log', level=logging.ERROR)

GRAPH_COLOR_NODE_INIT = 'blue'
GRAPH_COLOR_EDGE_INIT = 'black'
GRAPH_COLOR_NEIGHBOR = '#FFA500'  # Orange
GRAPH_COLOR_CURRUNT_NODE = 'green'
GRAPH_COLOR_PATH = 'red'
GRAPH_NODE_SIZE = 500
GRAPH_EDGE_WIDTH = 5
GRAPH_LABEL_FONT_SIZE = 14
GRAPH_TIME_INTERVAL = 1500


def generate_random_graph(n=None, p=None):
    """Randomly create an undirected unweighted graph."""
    if n is None:
        n = random.randint(9, 15)
    if p is None:
        p = random.random()/4 + 0.1
    graph = nx.Graph()
    nodes = string.ascii_uppercase[:n]
    graph.add_nodes_from(nodes)
    for i in range(n):
        for j in range(i+1, n):
            if random.random() < p:
                graph.add_edge(nodes[i], nodes[j])
    return graph


def init():
    """Draw the graph in its initial state before the shortest path finder is launched."""
    nx.draw_networkx_nodes(graph, pos, node_color=GRAPH_COLOR_NODE_INIT, node_size=GRAPH_NODE_SIZE)
    nx.draw_networkx_edges(graph, pos, edge_color=GRAPH_COLOR_EDGE_INIT)
    nx.draw_networkx_labels(graph, pos, font_size=GRAPH_LABEL_FONT_SIZE)
    return


def update(frame):
    """Keep updating the graph as the shortest path to all nodes within it is discovered."""
    global pos, graph, paths, current_node
    if frame >= len(paths):
        return
    node, neighbors = paths[frame]
    current_node.center = [pos[node][0], pos[node][1]+0.05]
    graph.nodes[node]['visited'] = True
    nx.draw_networkx_nodes(graph, pos, nodelist=[node], node_color=GRAPH_COLOR_PATH, node_size=GRAPH_NODE_SIZE)
    nx.draw_networkx_edges(graph, pos, edgelist=[(node, neighbor) for neighbor in neighbors], edge_color=GRAPH_COLOR_PATH, width=GRAPH_EDGE_WIDTH)
    nx.draw_networkx_nodes(graph, pos, nodelist=neighbors, node_color=GRAPH_COLOR_NEIGHBOR, node_size=GRAPH_NODE_SIZE)


if __name__ == '__main__':
    logger.info('Started')
    graph = generate_random_graph()
    pos = nx.spring_layout(graph)
    paths = find_paths(graph)
    current_node = plt.Circle(pos[paths[0][0]], 0.02, color=GRAPH_COLOR_CURRUNT_NODE, zorder=float('inf'))
    fig, ax = plt.subplots()
    ax.set_aspect("equal")
    ax.add_artist(current_node)
    try:
        fig_manager = plt.get_current_fig_manager()
        fig_manager.window.showMaximized()
    except:
        pass
    ani = animation.FuncAnimation(fig, update, interval=GRAPH_TIME_INTERVAL, init_func=init, blit=False)
    plt.show()
    logger.info('Ended')