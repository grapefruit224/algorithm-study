import sys
from collections import deque
input = sys.stdin.readline

dxy = [[1, 0], [-1, 0], [0, 1], [0, -1]]

m, n = map(int, input().split())
tomatos = []
now_tomatos = []
q = deque()
for i in range(n):
    a = list(map(int, input().split()))
    for j in range(m):
        if a[j] == 1:
            q.append([i, j])
    tomatos.append(a)


def bfs():

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dxy[i][0]
            ny = y + dxy[i][1]
            if not(0<=nx<n and 0<=ny<m):
                continue
            if tomatos[nx][ny] == 0:
                tomatos[nx][ny] = tomatos[x][y] + 1
                q.append([nx, ny])


bfs()

for row in tomatos:
    if 0 in row:
        print(-1)
        exit()

print(max(map(max, tomatos)) - 1)
