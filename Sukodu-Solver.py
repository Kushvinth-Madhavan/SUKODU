import sys

graph = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]
blank = [(i, j) for i in range(9) for j in range(9) if graph[i][j] == 0]

def isValid(x, y, num):
    if num in graph[x]:  # Check row
        return False
    if num in [graph[i][y] for i in range(9)]:  # Check column
        return False
    nx, ny = x // 3 * 3, y // 3 * 3
    if num in [graph[i][j] for i in range(nx, nx+3) for j in range(ny, ny+3)]:  # Check 3x3 box
        return False
    return True

def dfs(idx):
    if idx == len(blank):
        for row in graph:
            print(*row)
        exit(0)

    x, y = blank[idx]
    for num in range(1, 10):
        if isValid(x, y, num):
            graph[x][y] = num
            dfs(idx + 1)
            graph[x][y] = 0

dfs(0)
