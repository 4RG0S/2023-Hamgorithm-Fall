#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

int n, m;
int map[101];
bool visited[101];

int bfs() {
    queue<pair<int,int>> q;
    q.push({ 1,0 });

    while (!q.empty()) {
        pair<int, int> cur = q.front(); q.pop();
        if (cur.first == 100)
            return cur.second;
        for (int i = 1; i <= 6; i++) {
            int next = cur.first + i;
            if (map[next] != 0)
                next = map[next];

            if (next > 100)
                continue;
            if (visited[next])
                continue;

            q.push({ next,cur.second + 1 });
            visited[next] = true;
        }
    }
}

int main() {
    ios::sync_with_stdio(false); cin.tie(NULL);

    cin >> n >> m;
    for (int i = 0; i < n; i++) {
        int x, y;
        cin >> x >> y;
        map[x] = y;
    }
    for (int i = 0; i < m; i++) {
        int u, v;
        cin >> u >> v;
        map[u] = v;
    }

    cout << bfs();

    return 0;
}