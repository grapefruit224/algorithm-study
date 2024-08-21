from collections import deque
N = int(input())
tree = [[] for _ in range(N + 1)]

# 트리를 입력받음
for _ in range(N-1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

# 부모 노드를 저장할 리스트
result = [0 for _ in range(N + 1)]

# parent 정보와 노드 정보를 같이 저장함
queue = deque([[1, tree[1]]])
while queue:
    parent, nodes = queue.popleft()
    for i in range(len(nodes)):
        # 루트 노드이거나 이미 방문한 노드이면 continue
        if nodes[i] == 1 or result[nodes[i]] != 0:
            continue
        # 부모 노드를 설정해주고, 해당 노드에 연결된 자식 노드를 queue에 추가
        result[nodes[i]] = parent
        queue.append([nodes[i], tree[nodes[i]]])

for i in range(2, N + 1):
    print(result[i])