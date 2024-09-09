import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
rope = []
for _ in range(n):
    weight = int(input())
    rope.append(weight)
rope_duplicate = Counter(rope)
rope_duplicate = sorted(rope_duplicate.items(), key=lambda x : x[0])
answer = rope_duplicate[0][0] * n
left = rope_duplicate[0][1]

for i in range(1, len(rope_duplicate)):
    answer = max(answer, rope_duplicate[i][0]*(n-left))
    left += rope_duplicate[i][1]

print(answer)

# 정렬을 잘 못해서... 헤맸다. 무게를 기준으로 정렬할 것...
# 그리고 해당 무게보다 적은 로프를 제외하고 총 무게를 계산할 것!! -> 그래서 left로 누적해서 계산한다.