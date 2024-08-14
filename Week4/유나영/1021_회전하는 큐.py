from collections import deque

N, M = map(int, input().split())
numbers = list(map(int, input().split()))

queue = deque()
# 덱에 1부터 N까지의 수 추가
for i in range(1, N + 1):
    queue.append(i)
# 횟수를 셀 변수
count = 0

# numbers 리스트를 순회하면서
for i in range(M):
    # 뽑아야 할 수와 덱의 맨 첫번째 수가 같지 않은 동안
    while numbers[i] != queue[0]:

        # 뽑아야 할 수의 인덱스가 중간보다 앞쪽이면 앞에서 뒤로 보냄
        if queue.index(numbers[i]) <= len(queue) // 2:
            queue.append(queue.popleft())
            count += 1
        else:

            # 뽑아야 할 수의 인덱스가 중간보다 뒤쪽이면 뒤에서 앞으로 보냄
            queue.appendleft(queue.pop())
            count += 1
    # 뽑아야 할 수가 덱의 맨 앞으로 왔으면
    if numbers[i] == queue[0]:
        queue.popleft()
        continue

print(count)
