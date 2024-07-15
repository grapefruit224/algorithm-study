import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().strip())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]
answer = []

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(sx, sy):
    global house_count
    if visited[sx][sy] == 1:
        return
    visited[sx][sy] = 1
    for i in range(4):
        nx = sx + dx[i]
        ny = sy + dy[i]
        if not (0<=nx<n and 0<=ny<n):
            continue
        if graph[nx][ny] == 1 and visited[nx][ny] == 0:
            house_count += 1
            dfs(nx, ny)

group_count = 0
house_count = 0
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and not visited[i][j]:
            group_count += 1
            house_count = 1
            dfs(i, j)
            answer.append(house_count)
        house_count = 0
print(group_count)
for a in sorted(answer):
    print(a)