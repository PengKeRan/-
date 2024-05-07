# 迪杰斯特拉最短路径算法
import heapq


def dijkstra(graph, start, target):
    # 记录起点到每个节点的最短路径长度
    distances = {node: float('inf') for node in graph}
    # 记录前驱节点
    previous_nodes = {node: None for node in graph}
    # 确保起点到自身的路径长度为0
    distances[start] = 0

    # 使用堆优化来快速找到最短路径
    unvisited_nodes = [(distance, node) for node, distance in distances.items()]
    heapq.heapify(unvisited_nodes)

    while len(unvisited_nodes) > 0:
        # 获取距离最短的节点
        current_distance, current_node = heapq.heappop(unvisited_nodes)

        # 如果已经找到了目标节点的路径，就提前结束循环
        if current_node == target:
            break

        # 遍历所有相邻节点
        for adjacent_node, weight in graph[current_node].items():
            # 检查是否通过当前节点可以缩短到达相邻节点的距离
            new_distance = current_distance + weight
            if new_distance < distances[adjacent_node]:
                distances[adjacent_node] = new_distance
                previous_nodes[adjacent_node] = current_node
                heapq.heappush(unvisited_nodes, (new_distance, adjacent_node))

    # 构建最短路径
    path = []
    current = target
    while previous_nodes[current] is not None:
        path.append(current)
        current = previous_nodes[current]
    path.append(start)
    path.reverse()

    return distances[target], path


# 示例图
graph = {
    'A': {'B': 10, 'C': 20},
    'B': {'D': 15, 'E': 10},
    'C': {'D': 20, 'E': 25},
    'D': {'F': 10},
    'E': {'F': 20},
    'F': {}
}

# 使用Dijkstra算法找到起点'A'到终点'F'的最短路径
distance, path = dijkstra(graph, 'A', 'F')
print(f"最短路径长度: {distance}")
print(f"最短路径: {' -> '.join(path)}")