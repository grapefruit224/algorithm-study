#include <bits/stdc++.h>
using namespace std;
int t, m, n, k;
int dx[4] = {1, 0, -1, 0};
int dy[4] = {0, 1, 0, -1};
int vis[52][52];
bool board[52][52];

int main() {
    ios::sync_with_stdio(0); cin.tie(0);
    cin >> t;
    while (t--) {
        cin >> m >> n >> k;
        while (k--) {
            int x, y;
            cin >> x >> y;
            board[y][x] = true;
        }
        int cnt = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (vis[i][j] || !board[i][j]) continue;
                queue<pair<int, int>> q;
                q.push({i, j});
                vis[i][j] = 1;
                while (!q.empty()) {
                    auto cur = q.front(); q.pop();
                    for (int dir = 0; dir < 4; dir++) {
                        int nx = cur.first + dx[dir];
                        int ny = cur.second + dy[dir];
                        if (nx < 0 || nx >= n || ny < 0 || ny >= m) continue;
                        if (vis[nx][ny] || !board[nx][ny]) continue;
                        vis[nx][ny] = 1;
                        q.push({nx, ny});
                    }
                }
                cnt++;
            }
        }
        cout << cnt << "\n";
        for (int i = 0; i < n; i++) {
            fill(board[i], board[i] + m, 0);
            fill (vis[i], vis[i] + m, false);
        }
    }
}