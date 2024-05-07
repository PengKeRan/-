def is_safe(graph, v, c, color):
    """
    判断给定的颜色c是否可以分配给顶点v
    """
    for i in range(len(graph)):
        if graph[v][i] == 1 and color[i] == c:
            return False
    return True


def graph_coloring_util(graph, m, v, color):
    """
    递归实现图的着色
    """
    if v == len(graph):
        return True

    for c in range(1, m + 1):
        if is_safe(graph, v, c, color):
            color[v] = c
            if graph_coloring_util(graph, m, v + 1, color):
                return True
            color[v] = 0

    return False


def graph_coloring(graph, m):
    """
    给定一个图和颜色数量m，尝试对图进行着色
    """
    color = [0] * len(graph)
    if not graph_coloring_util(graph, m, 0, color):
        print("无法找到合适的着色方案。")
        return False

    print("图的着色方案为：", color)
    return True


# 测试
graph = [
    [0, 1, 1, 1],
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [1, 0, 1, 0]
]
colors = 3  # 着色数
graph_coloring(graph, colors)
