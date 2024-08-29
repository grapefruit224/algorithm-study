N = int(input())
stones = list(map(int, input().split()))
dp = [1e9 for _ in range(N)]
dp[0] = 0

for i in range(1, N):
    for j in range(i):
        # j번째 돌에서 i번째 돌까지 뛰는 데 드는 힘
        K = (i - j) * (1 + abs(stones[j] - stones[i]))
        print(f"K: {K}, i: {i}, j: {j}, dp: {dp[j-1]}")
        print(dp)

        # K와 dp[j](j번째 돌까지 뛰는 데 든 힘) 중 더 큰 값(현재 경로의 최대 값)을 골라서
        # 지금까지 저장된 i번째 돌까지 뛰는 데 드는 힘보다 작은 값을 저장
        dp[i] = min(dp[i], max(dp[j], K))


print(dp[N - 1])
