#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

int n, k;

bool visited[100001] = { {false,} };

int cnt = 0;
int method = 9999999;

bool isinside(int x) {
    return (x >= -1) && (x <= 100001);
}

void bfs() {
    queue<pair<int, int>> q;
    q.push({ n,0 });

    while (!q.empty()) {
        pair<int, int> cur = q.front(); q.pop();
        visited[cur.first] = true;

        if (cur.first == k) {
            if (method == 9999999)
                method = cur.second;
            if (cur.second == method)
                cnt++;
        }
        if (cur.second > method)
            continue;

        if (isinside(cur.first - 1) && !visited[cur.first - 1]) {
            q.push({ cur.first - 1, cur.second + 1 });
        }
        if (isinside(cur.first + 1) && !visited[cur.first + 1]) {
            q.push({ cur.first + 1, cur.second + 1 });
        }
        if (isinside(cur.first * 2) && !visited[cur.first * 2]) {
            q.push({ cur.first * 2, cur.second + 1 });
        }
    }
}


int main() {
    ios::sync_with_stdio(false); cin.tie(NULL);

    cin >> n >> k;

    bfs();
    cout << method << '\n' << cnt;

    return 0;
}