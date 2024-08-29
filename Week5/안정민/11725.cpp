#include <bits/stdc++.h>
using namespace std;
#define MAX 100001
int n, arr[MAX];
bool vis[MAX];
vector<int> v[MAX];
void dfs(int k) {
    vis[k] = true;
    for (int i = 0; i < v[k].size(); i++) {
        int next = v[k][i];
        if (!vis[next]) {
            arr[next] = k;
            dfs(next);
        }
    }
}
int main() {
    cin >> n;
    for (int i = 1; i < n; i++) {
        int x, y;
        cin >> x >> y;
        v[x].push_back(y);
        v[y].push_back(x);
    }
    dfs(1);
    for (int i = 2; i <= n; i++) cout << arr[i] << "\n";
}