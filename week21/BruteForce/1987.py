import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(input()) for i in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = 0
visited = []


def dfs(x, y, cnt):
    global result
    result = max(result, cnt)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < n) and (0 <= ny < m) and not (board[nx][ny] in visited):
            visited.append(board[nx][ny])
            dfs(nx, ny, cnt+1)
            visited.remove(board[nx][ny])


visited.append(board[0][0])
dfs(0, 0, 1)

print(result)
