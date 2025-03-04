from collections import deque


def wave_algorithm(grid, start, end):
    # Инициализация сетки
    rows, cols = len(grid), len(grid[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    distance = [[float('inf') for _ in range(cols)] for _ in range(rows)]

    # Распространение волны
    queue = deque([start])
    distance[start[0]][start[1]] = 0
    visited[start[0]][start[1]] = True

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Право, лево, вниз, вверх

    while queue:
        x, y = queue.popleft()

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if (0 <= nx < rows) and (0 <= ny < cols) and grid[nx][ny] != -1 and not visited[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = True
                distance[nx][ny] = distance[x][y] + 1

                if (nx, ny) == end:
                    break

    # Восстановление пути
    path = []
    current = end

    if distance[end[0]][end[1]] == float('inf'):
        return None  # Путь не найден

    while current != start:
        path.append(current)

        for dx, dy in directions:
            nx, ny = current[0] + dx, current[1] + dy

            if (0 <= nx < rows) and (0 <= ny < cols) and distance[nx][ny] < distance[current[0]][current[1]]:
                current = (nx, ny)
                break

    path.append(start)
    path.reverse()

    return path


# Пример использования
grid = [
    [0, 0, 0, 0, 0],
    [0, -1, -1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, -1, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

start_point = (0, 0)
end_point = (4, 4)

path = wave_algorithm(grid, start_point, end_point)

if path:
    print("Кратчайший путь:", path)
else:
    print("Путь не найден")
