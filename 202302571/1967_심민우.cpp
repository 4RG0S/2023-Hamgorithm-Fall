#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <memory.h>

using namespace std;

int n;
vector<pair<int,int>> tree[10001];
bool visited[10001] = { {false,} };

int maxlen = -1, maxnode;

void dfs(int curnode, int len) {
    visited[curnode] = true;
    if (maxlen < len) {
        maxlen = len;
        maxnode = curnode;
    }
    for (auto& node : tree[curnode]) {
        if (visited[node.first])
            continue;
        dfs(node.first, node.second + len);
    }
}

int main() {
    ios::sync_with_stdio(false); cin.tie(NULL);

    cin >> n;
    for (int i = 0; i < n - 1; i++) {
        int p, q, w;
        cin >> p >> q >> w;
        tree[p].push_back({ q,w });
        tree[q].push_back({ p,w });
    }

    dfs(1, 0);
    maxlen = -1;
    memset(visited, false, sizeof(visited));
    dfs(maxnode, 0);
    cout << maxlen;

    return 0;
}