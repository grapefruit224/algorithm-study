#include <bits/stdc++.h>
using namespace std;
int dp[1000001];
int n;
int main() {
    ios::sync_with_stdio(0); cin.tie(0);
    cin >> n;
    // 초기값
    dp[1] = 0;
    for (int i = 2; i <= n; i++) {
        // 1을 뺀다.
        dp[i] = dp[i - 1] + 1;
        // X가 2로 나누어 떨어지면, 2로 나눈다.
        if (i % 2 == 0) dp[i] = min(dp[i], dp[i / 2] + 1);
        // X가 3으로 나누어 떨어지면, 3으로 나눈다.
        if (i % 3 == 0) dp[i] = min(dp[i], dp[i / 3] + 1);
    }
    cout << dp[n];
}