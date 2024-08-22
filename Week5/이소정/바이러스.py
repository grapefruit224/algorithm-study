import sys
from collections import defaultdict
input = sys.stdin.readline

computer = int(input())
pairs = int(input())
trees = defaultdict(list)
for _ in range(pairs):
    u, v = map(int, input().split())
    trees[u].append(v)
    trees[v].append(u)
visited = [0]*(computer+1)
answer = 0
def dfs(start):
    global answer
    if visited[start] == 1:
        return
    visited[start] = 1
    answer += 1
    for go in trees[start]:
        dfs(go)
dfs(1)

print(answer-1)