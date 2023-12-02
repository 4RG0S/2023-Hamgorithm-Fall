// 23.09.11
// BOJ 16953
// 그래프 이론

#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

int bfs(long long a, long long b) {
    queue<pair<long long, long long>> q;
    q.push({ a,1 });
    while (!q.empty()) {
        pair<long long, long long> cur = q.front(); q.pop();

        if (cur.first == b)
            return cur.second;
        
        if (cur.first * 2 <= b)
            q.push({ cur.first * 2, cur.second + 1 });
        if(cur.first * 10 + 1 <= b)
            q.push({ cur.first * 10 + 1, cur.second + 1 });
    }
    return -1;
}

int main() {
    ios::sync_with_stdio(false); cin.tie(NULL);

    long long a, b;
    cin >> a >> b;
    cout << bfs(a, b);

    return 0;
}