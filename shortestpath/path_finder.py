"""Path Finder

Discovers the shortest path to all nodes within the graph using the Bread-First-Search algorithm,
which search for it by exploring all the connected nodes in a level-by-level manner.
"""

import logging
from typing import Collection, Dict, List, Optional, Set, Tuple, Union
from queue import Queue
import random

__all__ = [
    "find_paths"
]

logger = logging.getLogger(__name__)


def find_paths(graph):
    """Find the shortest paths to all nodes within the graph using the Bread-First-Search algorithm"""
    paths = []
    visited = set()
    nodes = list(graph.nodes())
    for node in nodes:
        if node not in visited:
            bfs(graph, node, visited, paths)
    return paths


def bfs(graph, node, visited, paths):
    """Search for the shortest path to all nodes within the graph by exploring all the connected nodes
    in a level-by-level manner. It starts at a root node and visits all the adjacent nodes. 
    Then for each of those adjacent nodes, it explores their unexplored neighbour nodes and so on."""
    queue = Queue()
    queue.put(node)
    visited.add(node)
    while not queue.empty():
        node = queue.get()
        nbrs = set()
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.put(neighbor)
                visited.add(neighbor)
                nbrs.add(neighbor)
        paths.append((node, nbrs))
        logger.info(f'paths = {paths}')
        