import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

T = int(input())
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y):
    if visited[x][y] == 1:
        return
    visited[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if not(0<=nx<m and 0<=ny<n):
            continue
        if graph[nx][ny] == 1 and visited[nx][ny] == 0:
            dfs(nx, ny)
    
for _ in range(T):
    answer = 0
    m, n, k = map(int, input().split())
    ca = []
    graph = [[0]*n for _ in range(m)]
    for _ in range(k):
        x, y = map(int, input().split())
        ca.append([x, y])
        graph[x][y] = 1
    visited = [[0]*n for _ in range(m)]
    for x, y in ca:
        
        if visited[x][y] == 0:
            dfs(x, y)
            answer += 1
    print(answer)
