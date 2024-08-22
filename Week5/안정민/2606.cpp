#include <bits/stdc++.h>
using namespace std;
bool visited[101];
vector<int> v[101];
int a, b, cnt;
void dfs(int x){
    cnt++;
    visited[x]=true;
    for(int i : v[x]){
        if(!visited[i]){
            dfs(i);
        }
    }
}
int main(){
    ios::sync_with_stdio(0); cin.tie(0);
    cin >> a >> b;
    for(int i = 0; i < b;i++){
        int c,d;
        cin >> c >> d;
        v[c].push_back(d);
        v[d].push_back(c);
    }
    dfs(1);
    cout << cnt-1;
}