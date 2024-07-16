from collections import deque
dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]

N = int(input())
apartment = [list(input()) for _ in range(N)]
num_house = []
count = 0
queue = deque()
for i in range(N):
    for j in range(N):
        if apartment[i][j] != '0':
            queue.append((i, j))
            is_single = True
            while queue:
                x, y = queue.popleft()

                for n in range(4):
                    next_x = x + dx[n]
                    next_y = y + dy[n]

                    if 0 <= next_x < N and 0 <= next_y < N and apartment[next_x][next_y] != '0':
                        apartment[next_x][next_y] = '0'
                        queue.append((next_x, next_y))
                        is_single = False
                        count += 1
            if is_single:
                num_house.append(1)
            if count != 0:
                num_house.append(count)
                count = 0

print(len(num_house))
print('\n'.join(map(str, sorted(num_house))))