from collections import deque

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
for _ in range(int(input())):
    N, M, K = map(int, input().split())

    field = [[0 for _ in range(M)] for _ in range(N)]
    for _ in range(K):
        x, y = map(int, input().split())
        field[x][y] = 1
    queue = deque()
    count = 0

    for i in range(N):
        for j in range(M):
            if field[i][j] != 0:
                queue.append((i, j))

                while queue:
                    x, y = queue.popleft()
                    for n in range(4):
                        nx = x + dx[n]
                        ny = y + dy[n]

                        if 0 <= nx < N and 0 <= ny < M and field[nx][ny] != 0:
                            field[nx][ny] = 0
                            queue.append((nx, ny))
                count += 1

    print(count)
