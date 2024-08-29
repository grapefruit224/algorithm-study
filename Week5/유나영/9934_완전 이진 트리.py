K = int(input())
paper = list(map(int, input().split()))
result = [[] for _ in range(K + 1)]
trees = [[] for _ in range(K)]

def div_conquer(buildings, depth):
    length = len(buildings)
    result[depth - 1].append(buildings[length//2])
    if depth == K:
        result[depth].append(buildings)
        return
    div_conquer(buildings[:length//2], depth + 1)
    div_conquer(buildings[length//2 + 1:], depth + 1)


div_conquer(paper, 1)
for i in range(K):
    print(*result[i])
def div_conquer(buildings, depth):
    mid = len(buildings) // 2
    result[depth].append(buildings[mid])
    if len(buildings) == 1:
        return
    div_conquer(buildings[:mid], depth + 1)
    div_conquer(buildings[mid + 1:], depth + 1)


div_conquer(paper, 0)
for i in range(K):
    print(*result[i])