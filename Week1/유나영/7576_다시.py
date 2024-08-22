from collections import deque

M, N = map(int, input().split())
tomato_box = [list(map(int, input().split())) for _ in range(N)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

# 이미 익어있는 토마토의 위치를 저장할 덱
matured = deque()

# 토마토가 익어있으면 덱이 저장
for col in range(N):
    for row in range(M):
        if tomato_box[col][row] == 1:
            matured.append((col, row))

# 익은 토마토가 있는 동안
while matured:
    col, row = matured.popleft()

    for n in range(4):
        n_row = row + dx[n]
        n_col = col + dy[n]
        if 0 <= n_row < M and 0 <= n_col < N and tomato_box[n_col][n_row] == 0:
            # 익지 않은 토마토를 익음 처리하고,
            matured.append((n_col, n_row))
            # 전날의 일수에 +1을 더하여 날짜 카운트
            tomato_box[n_col][n_row] = tomato_box[col][row] + 1


days = 0
for tomatoes in tomato_box:
    # 토마토 박스에 익지 않은 토마토가 남아있으면 -1 출력
    if 0 in tomatoes:
        print(-1)
        exit(0)
    else:
        # 현재 일수와 남은 일수 중 더 큰 값으로 일수 저장
        days = max(days, max(tomatoes))

print(days - 1)


## 다른 버전
# days = 0
      # 익은 토마토가 있는 동안
#     while matured:
#         while matured:
              # 익은 토마토들을 큐에 저장
#             queue.append(matured.popleft())
#         while queue:
#             col, row = queue.popleft()
#
#             for n in range(4):
#                 n_row = row + dx[n]
#                 n_col = col + dy[n]
#                 if 0 <= n_row < M and 0 <= n_col < N and tomato_box[n_col][n_row] == 0:
                      # 익지 않은 토마토를 익음 처리
#                     matured.append((n_col, n_row))
#                     tomato_box[n_col][n_row] = 1
          # 큐가 비었으면 1일 증가
#         days += 1
#
#     for tomatoes in tomato_box:
#         for tomato in tomatoes:
              # 토마토 상자에 익지 않은 토마토가 남았으면
#             if tomato == 0:
#                 print(-1)
#                 exit(0)
#     print(days - 1)