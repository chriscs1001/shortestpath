## shortestpath

## Visualization of Shortest Path Visiting All Nodes in a Graph

For a given graph, the shortest path visiting all nodes in it is discovered and visualized with an animation.
The Breadth-First-Search (BFS) algorithm is used to find the shortest path to all nodes in an unweighted undirected graph.

A new graph will be randomly created for each animation so that users can observe how the shortest path to all nodes can be identified in various graphs.

At the beginning of each animation, all the nodes and the edges of the graph are displayed in blue and black colors, respectively. BFS starts at a source node and visits all the adjacent nodes. Then for each of those adjacent nodes, it explores their unexplored neighbor nodes and so on, until all the nodes in the graph are explored. The randomly generated graph sometimes might have multiple components. All of them will be explored if there are.

The time complexity of BFS is O(n + m), where n is the number of nodes and m is the number of edges in the graph. BFS visits each node and traverses each edge once, ensuring a comprehensive graph exploration. This makes its performance linear to the graph's size, providing a predictable upper time limit.

For the purpose of visualization, the node's color will be changed as DFS makes progress in searching the shortest path to all nodes in the graph.

Here is the list of the color codes for visualization:

- Node's initial color: Blue
- Edge's initial color: Black
- Current node's marker: Green
- Discovered neighbor node's color: Orange
- Shortest path color: Red

This animation may help users understand how BFS finds the shortest path to all nodes in an unweighted undirected graph.
Please feel to use it and enjoy it! Any contribution will be welcome. Please check out the contributing guidelines if you wish to make.

## Installation

```bash
$ pip install shortestpath
```

## Usage

```bash
$ path_visualizer
```

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`shortestpath` was created by Chris Chang Seong. It is licensed under the terms of the MIT license.
