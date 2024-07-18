from collections import deque

M, N = map(int, input().split())

tomatoes = [list(map(int, input().split())) for _ in range(N)]
matured = deque()
for i in range(N):
    for j in range(M):
        if tomatoes[i][j] == 1:
            matured.append((i, j))

if not any(0 in tomato for tomato in tomatoes):
    print(0)
elif not matured:
    print(-1)
else:
    days = 0
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

    while matured:
        x, y = matured.popleft()

        for n in range(4):
            nx, ny = x + dx[n], y + dy[n]
            if 0 <= nx < N and 0 <= ny < M and tomatoes[nx][ny] == 0:
                matured.append((nx, ny))
                tomatoes[nx][ny] = tomatoes[x][y] + 1

    for tomato in tomatoes:
        if 0 in tomato:
            print(-1)
            exit(0)
        else:
            days = max(days, max(tomato))
    print(days - 1)
