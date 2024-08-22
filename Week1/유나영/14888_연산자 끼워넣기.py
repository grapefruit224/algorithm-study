# 2024.08.17
def dfs(n, value):
    global min_val, max_val
    if n == N-1:
        min_val = min(min_val, value)
        max_val = max(max_val, value)
        return

    if operators[0] > 0:
        operators[0] -= 1
        dfs(n + 1, value + numbers[n + 1])
        operators[0] += 1

    if operators[1] > 0:
        operators[1] -= 1
        dfs(n + 1, value - numbers[n + 1])
        operators[1] += 1

    if operators[2] > 0:
        operators[2] -= 1
        dfs(n + 1, value * numbers[n + 1])
        operators[2] += 1

    if operators[3] > 0:
        operators[3] -= 1
        dfs(n + 1, int(value / numbers[n + 1]))
        operators[3] += 1


N = int(input())
numbers = list(map(int, input().split()))
operators = list(map(int, input().split()))
min_val, max_val = 1e9, -1e9
dfs(0, numbers[0])
print(max_val)
print(min_val)