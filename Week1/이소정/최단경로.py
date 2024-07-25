import sys, heapq
from collections import defaultdict
from math import inf
input = sys.stdin.readline

V, E = map(int, input().split())
k = int(input())
graph = defaultdict(list)
dp = [inf]*(V+1)
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append([v, w])

def dfs():
    pq = []
    heapq.heappush(pq, (0, k))
    dp[k] = 0

    while pq:
        weight, departure = heapq.heappop(pq)

        if dp[departure] < weight:
            continue
        for v, w in graph[departure]:

            if dp[v] > weight+w:
                dp[v] = weight+w
                heapq.heappush(pq, (dp[v], v))

dfs()

for i in range(1, V+1):
    if dp[i] == inf:
        print("INF")
        continue
    print(dp[i])