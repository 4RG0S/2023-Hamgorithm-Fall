// 23.09.12
// BOJ 14502

#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

int n, m;
vector<pair<int, int>> newwall;
vector<pair<int, int>> virus;

int map[8][8];
int setmap[8][8];

int dy[] = { 1,-1,0,0 };
int dx[] = { 0,0,1,-1 };

vector<vector<int>> comb_arr;
vector<int> temp;
vector<int> visited(65);
void combination(int idx, int cnt, int N, int R) {
    if (cnt == R) {
        comb_arr.push_back(temp);
        return;
    }
    for (int i = idx; i <= N; i++) {
        if (visited[i])
            continue;
        visited[i] = true;
        temp.push_back(i);
        combination(i, cnt + 1, N, R);
        temp.pop_back();
        visited[i] = false;
    }
}

void bfs(pair<int,int> v) {
    queue<pair<int, int>> q;
    q.push(v);
    while (!q.empty()) {
        pair<int, int> cur = q.front(); q.pop();
        for (int i = 0; i < 4; i++) {
            int ny = cur.first + dy[i];
            int nx = cur.second + dx[i];

            if (ny < 0 || ny >= n || nx < 0 || nx >= m)
                continue;
            if (setmap[ny][nx] != 0)
                continue;
            
            setmap[ny][nx] = 2;
            q.push({ ny,nx });
        }
    }
}

int main() {
    ios::sync_with_stdio(false); cin.tie(NULL);

    cin >> n >> m;

    for (int y = 0; y < n; y++) {
        for (int x = 0; x < m; x++) {
            cin >> map[y][x];
            if (map[y][x] == 0)
                newwall.push_back({ y,x });
            if (map[y][x] == 2)
                virus.push_back({ y,x });
        }
    }
    combination(0, 0, (int)newwall.size() - 1, 3);

    int maxsize = 0;
    for (int i = 0; i < (int)comb_arr.size(); i++) {
        pair<int, int> setwall[3] = { newwall[comb_arr[i][0]],newwall[comb_arr[i][1]],newwall[comb_arr[i][2]] };

        for (int y = 0; y < n; y++) {
            for (int x = 0; x < m; x++) {
                setmap[y][x] = map[y][x];
            }
        }
        for (int j = 0; j < 3; j++)
            setmap[setwall[j].first][setwall[j].second] = 1;

        for (int j = 0; j < (int)virus.size(); j++)
            bfs(virus[j]);

        int cnt = 0;
        for (int y = 0; y < n; y++) {
            for (int x = 0; x < m; x++) {
                if (setmap[y][x] == 0)
                    cnt++;
            }
        }
        maxsize = max(maxsize, cnt);
    }

    cout << maxsize;

    return 0;
}