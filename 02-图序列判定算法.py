def is_non_increasing(seq):
    """
    判断给定的序列是否是非递增的
    """
    return all(seq[i] >= seq[i + 1] for i in range(len(seq) - 1))


def is_graphical(seq):
    """
    判断给定的非负整数组成的序列是否可图化
    """
    seq.sort(reverse=True)  # 将序列按非增序排列
    if seq[-1] < 0:
        return False  # 序列中存在负数，不可图化

    while seq[0] > 0:
        k = seq[0]  # 取出最大的度数
        if len(seq) <= k:
            return False  # 序列长度不足以支持最大度数的节点
        for i in range(1, k + 1):
            seq[i] -= 1  # 将k个最大度数的节点的度数减1
        seq = seq[1:]  # 去除度数为0的节点
        seq.sort(reverse=True)  # 重新按非增序排列
    return True


def generate_graph(seq):
    """
    生成满足条件的无向图
    """
    if not is_non_increasing(seq):
        print("给定的序列不是非递增的，无法生成图。")
        return None
    if not is_graphical(seq):
        print("给定的序列不可图化。")
        return None

    graph = {}
    seq.sort(reverse=True)
    while seq:
        k = seq[0]
        neighbors = seq[1:k + 1]
        graph[k] = neighbors
        seq = seq[k + 1:]
    return graph


# 测试
sequence = [5, 4, 3, 3, 2, 2, 1, 1]
print("给定序列是否可图化：", is_graphical(sequence))