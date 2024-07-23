N = int(input())
numbers = list(map(int, input().split()))
add, minus, mul, div = map(int, input().split())

min_num = 1e9
max_num = -1e9


def dfs(depth, n, add, minus, mul, div):
    global min_num, max_num
    print(n)
    if depth == N:
        min_num = min(min_num, n)
        max_num = max(max_num, n)
        return
    if add > 0:
        dfs(depth + 1, n + numbers[depth], add - 1, minus, mul, div)
    elif minus > 0:
        dfs(depth + 1, n - numbers[depth], add, minus - 1, mul, div)
    elif mul > 0:
        dfs(depth + 1, n * numbers[depth], add, minus, mul - 1, div)
    elif div > 0:
        dfs(depth + 1, n // numbers[depth], add, minus, mul, div - 1)


dfs(1, numbers[0], add, minus, mul, div)
print(int(min_num), int(max_num))
