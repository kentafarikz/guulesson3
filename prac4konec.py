from collections import deque


def count_vertices(edges):
    """Подсчет количества вершин в графе."""
    vertices = set()
    for edge in edges:
        vertices.add(edge[0])
        vertices.add(edge[1])
    return len(vertices)


def get_vertices(edges):
    """Получение списка вершин из списка ребер."""
    vertices = set()
    for edge in edges:
        vertices.add(edge[0])
        vertices.add(edge[1])
    return list(vertices)


def build_adjacency_list(edges):
    """Создание списка смежности для быстрого доступа к соседним вершинам."""
    adjacency_list = {}
    for edge in edges:
        if edge[0] not in adjacency_list:
            adjacency_list[edge[0]] = []
        if edge[1] not in adjacency_list:
            adjacency_list[edge[1]] = []
        adjacency_list[edge[0]].append(edge[1])
        adjacency_list[edge[1]].append(edge[0])
    return adjacency_list


def wave_algorithm(edges, start, end):
    """Реализация волнового алгоритма с использованием очереди."""
    vertices = get_vertices(edges)
    num_vertices = count_vertices(edges)

    # Создание списка смежности
    adjacency_list = build_adjacency_list(edges)

    # Инициализация массива пройденных вершин
    visited = {v: 0 for v in vertices}
    visited[start] = 1

    # Инициализация массива предков для восстановления пути
    parent = {v: None for v in vertices}

    # Флаг для проверки, найдена ли конечная вершина
    found = False

    # Использование очереди для обхода графа
    queue = deque([start])

    while queue:
        current_vertex = queue.popleft()

        # Если конечная вершина найдена, выходим из цикла
        if current_vertex == end:
            found = True
            break

        # Проходим по всем соседним вершинам
        for neighbor in adjacency_list.get(current_vertex, []):
            if visited[neighbor] == 0:
                visited[neighbor] = visited[current_vertex] + 1
                parent[neighbor] = current_vertex
                queue.append(neighbor)

    # Восстановление пути
    if found:
        path = []
        current = end
        while current is not None:
            path.append(current)
            current = parent[current]
        path.reverse()
        return path, visited
    else:
        return None, visited


# Пример использования
edges = [(1, 2), (2, 3), (2, 4), (4, 5), (1, 6), (6, 7), (4, 5)]
start = 1
end = 5
path, visited = wave_algorithm(edges, start, end)
if path:
    print(f"Кратчайший путь от {start} до {end}: {path}")
else:
    print(f"Путь от {start} до {end} не найден")
print("Шаги посещения вершин:", visited)
