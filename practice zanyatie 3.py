from collections import deque


def bfs_levels(adjacency_matrix, start):
    # Количество вершин
    n = len(adjacency_matrix)

    # Список уровней (по умолчанию None, что значит не пройдено)
    levels = [None] * n

    # Начальный уровень для стартовой вершины
    levels[start] = 0

    # Очередь для BFS
    queue = deque([start])

    while queue:
        current = queue.popleft()

        # Проходим по всем соседям текущей вершины
        for neighbor in range(n):
            if adjacency_matrix[current][neighbor] == 1 and levels[neighbor] is None:
                # Если существует ребро и вершина еще не пройдена
                levels[neighbor] = levels[current] + 1
                queue.append(neighbor)

    return levels


# Пример матрицы смежности для графа
# 0 - нет ребра, 1 - есть ребро между вершинами
adjacency_matrix = [
    [0, 1, 1, 0, 0],
    [1, 0, 1, 1, 0],
    [1, 1, 0, 1, 0],
    [0, 1, 1, 0, 1],
    [0, 0, 0, 1, 0]
]

# Выбираем начальную вершину (например, 0)
start_vertex = 0

# Получаем уровни вершин
levels = bfs_levels(adjacency_matrix, start_vertex)

# Выводим уровни для каждой вершины
print("Уровни вершин от начальной вершины:", levels)