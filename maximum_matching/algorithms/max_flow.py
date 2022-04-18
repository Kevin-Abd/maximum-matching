from typing import List, Tuple, Union
from maximum_matching.algorithms.algorithm_base import AlgorithmBase
from maximum_matching.graphs.graph_base import BipartiteSet, GraphBase

class MaxFlow(AlgorithmBase):
    """
    Edmonds Karp algorithm implementation of the Maximum Flow problem
    """

    INF = 1000000009

    vec = [] # graph on which the max flow will run
    visited = []
    capacity = [] # 2D array for capacity

    bfs_path = []


    def BFS(self, start: int, endd: int, n: int) -> bool:
        self.bfs_path = [-1] * n
        que = []
        que.append(start)
        self.visited[start] = True

        found = False
        while (len(que) > 0 and found == False):
            u = que[0]

            if found == False and self.vec[u] is not None:
                for v in self.vec[u]:
                    if self.visited[v] == False and self.capacity[u][v] > 0:
                        que.append(v)
                        self.visited[v] = True
                        self.bfs_path[v] = u

                        if v == endd:
                            found = True

                    if found == True:
                        break

            que.pop(0)

        return found


    def run_max_flow(self, src: int, sink: int, n: int) -> int:
        max_flow = 0
        min_capacity = self.INF
        self.visited = [False] * n

        trends.append([len(visited_nodes_for_trends), max_flow])

        while self.BFS(src, sink, n) is True:

            x = sink
            while x != src:
                min_capacity = min(min_capacity, self.capacity[self.bfs_path[x]][x])
                x = self.bfs_path[x]

            x = sink
            while x != src and min_capacity != self.INF:
                self.capacity[self.bfs_path[x]][x] -= min_capacity
                self.capacity[x][self.bfs_path[x]] += min_capacity
                x = self.bfs_path[x]

            max_flow += min_capacity
            min_capacity = self.INF

            self.visited = [False] * n

        return max_flow


    def make_edge(self, u: int, v: int, cap: int):
        self.capacity[u][v] = cap

        if self.vec[u] is None:
            self.vec[u] = []
        
        self.vec[u].append(v)


    def prepare_graph(self, graph: GraphBase, sourceSinkCap: int = 1) -> List:

        left_side = graph.get_independent_set(BipartiteSet.left)
        right_side = graph.get_independent_set(BipartiteSet.right)

        total_nodes = graph.size + 1
        source_node = total_nodes
        total_nodes += 1
        sink_node = total_nodes
        total_nodes += 1

        # print("Tests: ", right_side[0])

        trends = []
        visited_nodes = graph.size_left

        trends.append([visited_nodes, 0])
        max_matches = 0

        for right_idx in range(graph.size_right):
            self.vec = [None] * total_nodes
            self.capacity = [ [0]*total_nodes for i in range(total_nodes)] 

            # connecting source_node with left side
            for x in left_side:
                u = source_node
                v = x
                self.make_edge(u, v, sourceSinkCap)

            # connecting right_side with sink_node
            for x in right_side:
                u = x
                v = sink_node
                self.make_edge(u, v, sourceSinkCap)

            for i in range(right_idx + 1):
                v = right_side[i]
                neighbours = graph.list(v)
                for u in neighbours:
                    self.make_edge(u, v, 1)

            count_matches = self.run_max_flow(source_node, sink_node, total_nodes)

            visited_nodes += 1

            max_matches = max(max_matches, count_matches)

            trends.append([visited_nodes, count_matches])

        # return (source_node, sink_node, total_nodes)
        return max_matches, trends


    def run(self, graph: GraphBase) -> Tuple[int, Union[List, None]]:
        
        # src, sink, n = self.prepare_graph(graph)

        # count_matches, trends = self.run_max_flow(src, sink, n)

        max_matches, trends = self.prepare_graph(graph)

        # print(trends)

        return (max_matches, trends)