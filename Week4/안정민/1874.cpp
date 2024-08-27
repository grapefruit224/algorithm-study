#include <bits/stdc++.h>
using namespace std;
int n;
stack<int> s;
vector<char> v;
int main() {
    ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);
    int i = 1;
    cin >> n;
    while (n--) {
        int x; cin >> x;
        if (i <= x) {
            while (i <= x) {
                s.push(i++);
                v.push_back('+');
            }
        }
        if (s.top() == x) {
            s.pop();
            v.push_back('-');
        }
        else {
            cout << "NO";
            return 0;
        }
    }
    for (char c : v) cout << c << '\n';
}