#include <bits/stdc++.h>
using namespace std;
int dx[4] = {1, 0, -1, 0};
int dy[4] = {0, 1, 0, -1};
int n;
string board[26];
bool vis[26][26];
int main() {
    ios::sync_with_stdio(0); cin.tie(0);
    cin >> n;
    for (int i = 0; i < n; i++) cin >> board[i];
    int count = 0;
    vector<int> ans;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (board[i][j] == '0' || vis[i][j] == 1) continue;
            queue<pair<int, int>> q;
            count++;
            vis[i][j] = 1;
            q.push({i, j});
            int tmp = 1;
            while (!q.empty()) {
                auto cur = q.front(); q.pop();
                for (int dir = 0; dir < 4; dir++) {
                    int nx = cur.first + dx[dir];
                    int ny = cur.second + dy[dir];
                    if (nx < 0 || nx >= n || ny < 0 || ny >= n) continue;
                    if (board[nx][ny] == '0' || vis[nx][ny] == 1) continue;
                    vis[nx][ny] = 1;
                    q.push({nx, ny});
                    tmp++;
                }
            }
            ans.push_back(tmp);
        }
    }
    cout << count << "\n";
    sort(ans.begin(), ans.end());
    for (int i : ans) cout << i << "\n";
}