def dfs(row, col, matrix, visited):
    if (row < 0 or row >= len(matrix)
            or col < 0 or col >= len(matrix[0])
            or matrix[row][col] != "."
            or visited[row][col]):
        return 0

    visited[row][col] = True
    connections = 1

    for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        connections += dfs(row + dr, col + dc, matrix, visited)

    return connections


def find_max_connections(matrix):
    max_connections = 0
    rows, cols = len(matrix), len(matrix[0])
    visited = [[False] * cols for _ in range(rows)]

    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] == "." and not visited[row][col]:
                max_connections = max(max_connections, dfs(row, col, matrix, visited))

    return max_connections


board = [input().split() for _ in range(int(input()))]

print(find_max_connections(board))
