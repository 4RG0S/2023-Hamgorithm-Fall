#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

int n, m;
int arr[10];
bool visited[10];
int ans[10];

void dfs(int index) {
    if (index == m) {
        for (int i = 0; i < m; i++) {
            cout << ans[i] << " ";
        }
        cout << '\n';
        return;
    }

    for (int i = 0; i < n; i++) {
        if (visited[i])
            continue;

        visited[i] = true;
        ans[index] = arr[i];
        dfs(index + 1);
        visited[i] = false;
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> n >> m;
    for (int i = 0; i < n; i++)
        cin >> arr[i];

    sort(arr, arr + n);
    dfs(0);


    return 0;
}