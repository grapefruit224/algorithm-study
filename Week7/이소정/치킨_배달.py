import sys
input = sys.stdin.readline

n, m = map(int, input().split())
city = []
house, chicken = [], []
picked_chicken = []
answer = 1e8

for i in range(n):
    row = list(map(int, input().split()))
    for j in range(n):
        if row[j] == 1:
            house.append([i, j])
        if row[j] == 2:
            chicken.append([i, j])

def calculate(x1, y1, x2, y2):
    return abs(x1-x2) + abs(y1-y2)

# 폐업안시킬 경우의 수 구해서 하는 방법 => itertools 사용
# 아님 백트래킹!
def backtracking(a, alive_cnt):
    global answer
    if a > len(chicken):
        return
    if alive_cnt == m:
        all_distance = 0
        for r, c in house:
            distance = 1e8
            for i in picked_chicken:
                cr, cc = chicken[i]
                distance = min(distance, calculate(r, c, cr, cc))
            all_distance += distance
        answer = min(answer, all_distance)
    picked_chicken.append(a)
    backtracking(a+1, alive_cnt+1) # 치킨집 선택했을 때
    picked_chicken.pop()
    backtracking(a+1, alive_cnt) # 치킨집 선택안했을 때


backtracking(0, 0)
print(answer)