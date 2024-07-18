N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()
visited = [False] * N
result = []


def dp():
    if len(result) == M:
        print(' '.join(map(str, result)))
        return
    dup = 0
    for i in range(N):
        if not visited[i] and dup != numbers[i]:
            result.append(numbers[i])
            visited[i] = True
            dup = numbers[i]
            dp()
            visited[i] = False
            result.pop()


dp()
