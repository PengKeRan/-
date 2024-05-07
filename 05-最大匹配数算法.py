class BipartiteGraph:
    def __init__(self, graph):
        self.graph = graph
        self.left_match = {}
        self.right_match = {}
        self.visited = set()

    def max_matching(self):
        for left_node in self.graph.keys():
            self.visited = set()
            self.find_augmenting_path(left_node)
        return len(self.left_match)

    def find_augmenting_path(self, left_node):
        if left_node in self.visited:
            return False
        self.visited.add(left_node)
        for right_node in self.graph[left_node]:
            if right_node not in self.right_match or self.find_augmenting_path(self.right_match[right_node]):
                self.left_match[left_node] = right_node
                self.right_match[right_node] = left_node
                return True
        return False


# Example usage:

graph = {
    'A': ['X', 'Y', 'Z'],
    'B': ['X', 'Y'],
    'C': ['X', 'Z'],
}

bipartite_graph = BipartiteGraph(graph)
max_matching_size = bipartite_graph.max_matching()
print("最大匹配数:", max_matching_size)
