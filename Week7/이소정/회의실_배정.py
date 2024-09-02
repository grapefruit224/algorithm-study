import sys
input = sys.stdin.readline

n = int(input())
meeting = [list(map(int, input().split())) for _ in range(n)]
meeting = sorted(meeting, key=lambda x : (x[1], x[0]))
s, e = meeting[0]
answer = 1
for i in range(1, n):
    ns, ne = meeting[i]
    if not(e <= ns):
        continue
    answer += 1
    s, e = ns, ne
print(answer)