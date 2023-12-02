#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <cmath>

using namespace std;

int r, c;
char map[21][21];

int dy[] = { 0,1,0,-1 };
int dx[] = { 1,0,-1,0 };

bool visited[27] = { false, };

int maxmove = 0;

void dfs(int y, int x, int cnt) {
    maxmove = max(cnt, maxmove);
    for (int i = 0; i < 4; i++) {
        int ny = y + dy[i];
        int nx = x + dx[i];

        if (ny < 0 || ny >= r || nx < 0 || nx >= c)
            continue;

        if (!visited[map[ny][nx] - 'A']) {
            visited[map[ny][nx] - 'A'] = true;
            dfs(ny, nx, cnt + 1);
            visited[map[ny][nx] - 'A'] = false;
        }
        
    }
}

int main() {
    ios::sync_with_stdio(false); cin.tie(NULL);

    cin >> r >> c;
    for (int y = 0; y < r; y++) {
        for (int x = 0; x < c; x++) {
            cin >> map[y][x];
        }
    }   
    visited[map[0][0] - 'A'] = true;
    dfs(0, 0, 1);
    cout << maxmove;


    return 0;
}