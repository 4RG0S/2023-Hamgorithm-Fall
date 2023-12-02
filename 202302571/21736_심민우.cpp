#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <cmath>

using namespace std;

int n, m;
char map[601][601];
bool visited[601][601] = { {false,} };
int cnt;

int dy[] = { 1,0,-1,0 };
int dx[] = { 0,1,0,-1 };

void dfs(int y, int x) {
    for (int i = 0; i < 4; i++) {
        int ny = y + dy[i];
        int nx = x + dx[i];

        if (ny < 0 || ny >= n || nx < 0 || nx >= m)
            continue;
        if (visited[ny][nx])
            continue;
        if (map[ny][nx] == 'X')
            continue;
        if (map[ny][nx] == 'P')
            cnt++;

        visited[ny][nx] = true;
        dfs(ny, nx);
    }
}


int main() {
    ios::sync_with_stdio(false); cin.tie(NULL);

    cin >> n >> m;
    for (int y = 0; y < n; y++) {
        for (int x = 0; x < m; x++) {
            cin >> map[y][x];
        }
    }

    for (int y = 0; y < n; y++) {
        for (int x = 0; x < m; x++) {
            if (map[y][x] == 'I') {
                visited[y][x] = true;
                dfs(y, x);
            }
        }
    }

    if (cnt == 0)
        cout << "TT";
    else
        cout << cnt;

    return 0;
}