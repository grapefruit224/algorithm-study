n, w, L = map(int, input().split())
trucks = list(map(int, input().split()))

count, i = 1, 1
# 다리에 올라가 있는 트럭의 무게 합
total_weight = trucks[0]
# 다리에 올라가 있는 트럭들의 정보
bridge = [[trucks[0], w - 1]]

# 다리에 트럭이 존재하는 동안
while bridge:
    # 맨 앞 트럭이 끝에 도달했으면 다리에서 제거
    if bridge[0][1] == 0:
        total_weight -= bridge[0][0]
        bridge.pop(0)
    # 각 트럭들을 한 칸씩 전진
    for j in range(len(bridge)):
        bridge[j][1] -= 1
    # 남은 트럭이 존재하고, 다음 트럭을 다리에 올릴 수 있으면
    if n != 1 and i < n and total_weight + trucks[i] <= L:
        bridge.append([trucks[i], w - 1])
        total_weight += trucks[i]
        i += 1
    count += 1

print(count)