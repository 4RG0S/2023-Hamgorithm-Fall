#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <cmath>
#include <sstream>

using namespace std;

int n, m;
int arr[9];
bool visited[9];

void dfs(int num, int cnt) {
    if (cnt == m) {
        for (int i = 0; i < m; i++)
            cout << arr[i] << ' ';
        cout << '\n';
        return;
    }
    for (int i = num; i <= n; i++) {
        visited[i] = true;
        arr[cnt] = i;
        dfs(i, cnt + 1);
        visited[i] = false;
    }
}


int main() {
    ios::sync_with_stdio(false); cin.tie(NULL);

    cin >> n >> m;
    dfs(1, 0);

    return 0;
}