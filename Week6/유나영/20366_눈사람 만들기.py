from collections import defaultdict
from itertools import combinations

N = int(input())
snowballs = list(map(int, input().split()))
snowballs.sort()
sub = []
snowman = list(combinations(snowballs, 2))
for i in range(len(snowman)):
    snowman[i] += snowman[i][0] + tuple(snowman[i][1])
snowmen = list(combinations(snowman, 2))
print(snowman)
#print(snowmen)
length = len(snowmen)
height = []
min_value = 1e9
snowmen.sort()

for i in range(length - 1):
    dic = defaultdict(int)
    head, body = snowmen[i][0], snowmen[i][1]
    #print(f"head: {head}, body: {body}")
    if body[0] not in head and body[1] not in head:
        a, b = head[0], head[1]
        x, y = body[0], body[1]
        #print(f"a: {a}, b: {b}, x: {x}, y: {y}")
        if min_value > abs((x + y) - (a + b)):
            min_value = abs((x + y) - (a + b))
    # dic[a], dic[b] = 1, 1
    # if dic[x] != 1 and dic[y] != 1:
    #     height.append(abs((a + b) - (x + y)))


print(min_value)

for i in range(601):
    print(i, end=" ")