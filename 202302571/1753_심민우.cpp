#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

int v, e;
int s;
vector<pair<int, int>> graph[20001];
vector<int> dist;

void dijkstra() {
    priority_queue<pair<int, int>> pq;
    dist[s] = 0;
    pq.push({ 0,s });

    while (!pq.empty()) {
        int curdist = -pq.top().first;
        int curnode = pq.top().second;
        pq.pop();

        if (dist[curnode] < curdist)
            continue;
        for (pair<int, int> next : graph[curnode]) {
            int nextnode = next.first;
            int nextcost = curdist + next.second;
            if (nextcost < dist[nextnode]) {
                dist[nextnode] = nextcost;
                pq.push({ -nextcost,nextnode });
            }
        }
    }
}

int main() {
    ios::sync_with_stdio(false); cin.tie(NULL);

    cin >> v;
    cin >> e;
    cin >> s;
    while (e--) {
        int p, q, r;
        cin >> p >> q >> r;
        graph[p].push_back({ q,r });
    }

    dist.assign(v + 1, 2147483647);
    dijkstra();

    for (int i = 1; i <= v; i++) {
        if (dist[i] == 2147483647)
            cout << "INF";
        else
            cout << dist[i];
        cout << '\n';
    }

    return 0;
}