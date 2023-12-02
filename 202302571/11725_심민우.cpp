#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

int n;
vector<int> tree[100001];
int parent[100001];

void dfs(int curnode) {
    for (int node : tree[curnode]) {
        if (parent[node] == 0) {
            parent[node] = curnode;
            dfs(node);
        }
    }
}

int main() {
    ios::sync_with_stdio(false); cin.tie(NULL);

    cin >> n;
    for (int i = 0; i < n - 1; i++) {
        int p, q;
        cin >> p >> q;
        tree[p].push_back(q);
        tree[q].push_back(p);
    }

    dfs(1);
    for (int i = 2; i <= n; i++)
        cout << parent[i] << '\n';

    return 0;
}