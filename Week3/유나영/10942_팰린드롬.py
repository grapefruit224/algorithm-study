N = int(input())
numbers = list(map(int, input().split()))
# 인덱스랑 순서 맞추기
numbers.insert(0, 0)

dp = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

# 대각선 방향(자기 자신)을 팰린드롬으로 설정
for i in range(1, N+1):
    dp[i][i] = 1

# 연속된 글자 ex) "aa", "bb" 와 같은 문자열을 팰린드롬으로 설정
for i in range(1, N):
    if numbers[i] == numbers[i+1]:
        dp[i][i+1] = 1

# 시작 문자열(numbers[i])와 끝 문자열(numbers[j])가 같고
# 그 사이 문자열(dp[i+1][j-1])이 팰린드롬이면 팰린드롬으로 설정
for k in range(2, N):
    for i in range(N+1):
        j = i + k
        if j <= N:
            if numbers[i] == numbers[j] and dp[i+1][j-1] == 1:
                dp[i][j] = 1

for _ in range(int(input())):
    S, E = map(int, input().split())
    print(dp[S][E])
