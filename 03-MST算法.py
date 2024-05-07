import heapq


def prim(graph):
    """
    使用Prim算法生成最小生成树

    参数：
    graph：邻接字典，表示无向图，格式为 {节点1: {邻居节点1: 权重1, 邻居节点2: 权重2, ...}, ...}

    返回值：
    min_span_tree：最小生成树的边列表，每个边由两个节点和权重组成，格式为 [(节点1, 节点2, 权重), ...]
    """
    min_span_tree = []
    visited = set()  # 已访问的节点集合
    start_node = list(graph.keys())[0]  # 随机选择一个节点作为起始节点
    visited.add(start_node)
    candidate_edges = [(cost, start_node, neighbor) for neighbor, cost in graph[start_node].items()]
    heapq.heapify(candidate_edges)  # 将候选边按权重堆排序

    while candidate_edges:
        cost, node1, node2 = heapq.heappop(candidate_edges)
        if node2 not in visited:
            visited.add(node2)
            min_span_tree.append((node1, node2, cost))
            for neighbor, cost in graph[node2].items():
                if neighbor not in visited:
                    heapq.heappush(candidate_edges, (cost, node2, neighbor))

    return min_span_tree


# 示例测试
graph = {
    'A': {'B': 2, 'D': 3},
    'B': {'A': 2, 'C': 1, 'D': 4},
    'C': {'B': 1, 'D': 2},
    'D': {'A': 3, 'B': 4, 'C': 2}
}

print("Prim算法生成的最小生成树：", prim(graph))