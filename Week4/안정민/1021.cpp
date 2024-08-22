#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(0); cin.tie(0);
    int n, m;
    cin >> n >> m;
    deque<int> dq;
    for (int i = 1; i <= n; i++) dq.push_back(i);
    int res = 0;
    while (m--) {
        int t;
        cin >> t;
        int idx = find(dq.begin(), dq.end(), t) - dq.begin();
        while (dq.front() != t) {
            if (idx < (int)dq.size() - idx) {
                dq.push_back(dq.front());
                dq.pop_front();
            }
            else {
                dq.push_front(dq.back());
                dq.pop_back();
            }
            res++;
        }
        dq.pop_front();
    }
    cout << res;
}