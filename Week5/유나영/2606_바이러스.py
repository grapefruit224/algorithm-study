from collections import deque

N = int(input())
pairs = int(input())
computers = [[] for _ in range(N + 1)]
for i in range(pairs):
    x, y = map(int, input().split())
    computers[x].append(y)
    computers[y].append(x)
print(computers)
visited = [False for _ in range(N + 1)]
#visited[1] = True
count = 0
queue = deque(computers[1])
while queue:
    print("queue: ", queue)
    index = queue.popleft()
    print("index: ", index)
    print("visited:", visited)
    print("computer: ", computers[index])
    for com in computers[index]:
        if not visited[com] and com != 1:
            print("append: ", com)
            queue.append(com)
            visited[com] = True
            count += 1
    visited[index] = True
print(visited.count(True))
