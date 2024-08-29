from collections import deque
dishes, tot_sushi, con_dish, extra = map(int, input().split())
belt = [int(input()) for _ in range(dishes)]

sushi = deque([])
ate_dishes = [0 for _ in range(tot_sushi+1)]
result, count = 0, 0
for i in range(con_dish):
    sushi.append(belt[i])
    if ate_dishes[belt[i]] == 0:
        count += 1
    ate_dishes[belt[i]] += 1
result = count

for i in range(dishes):
    print(sushi)
    print(ate_dishes)
    ate = sushi.popleft()
    ate_dishes[ate] -= 1
    if ate_dishes[ate] == 0:
        count -= 1

    index = (i + con_dish) % dishes
    sushi.append(belt[index])
    if ate_dishes[belt[index]] == 0:
        count += 1
    ate_dishes[belt[index]] += 1

    print("after:", sushi)
    if ate_dishes[extra] == 0:
        result = max(result, count + 1)
    else:
        result = max(result, count)

print(result)

n,d,k,c = map(int,input().split())
count = 1
s = [0] * (d+1)
s[c] = 1
data = []
for i in range(n):
    data.append(int(input()))

for i in range(k):
    s[data[i]] += 1
    if s[data[i]] == 1:
        count += 1

answer = count

for i in range(n-1):
    s[data[i]] -= 1
    if s[data[i]] == 0:
        count -= 1
    s[data[(i+k) % n]] += 1
    if s[data[(i+k) % n]] == 1:
        count += 1
    answer = max(answer, count)

print(answer)