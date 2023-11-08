#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

int n, m;

int dis[102][102] = { {0,} };

vector<pair<int, int>> house;
vector<pair<int, int>> chickenhouse;

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

int main(void) {
    ios::sync_with_stdio(false); cin.tie(NULL);
    cin >> n >> m;

    for (int y = 1; y <= n; y++) {
        for (int x = 1; x <= n; x++) {
            int p;
            cin >> p;
            if (p == 1)
                house.push_back({ y,x });
            else if (p == 2)
                chickenhouse.push_back({ y,x });
        }
    }

    for (int i = 0; i < house.size(); i++) {
        for (int j = 0; j < chickenhouse.size(); j++) {
            dis[i][j] = abs(house[i].first - chickenhouse[j].first) + abs(house[i].second - chickenhouse[j].second);
        }
    }

    combination(0, 0, (int)chickenhouse.size()-1, m);
    int minchicken = 1000000000;
    for (int i = 0; i < comb_arr.size(); i++) {
        int sum = 0;
        for (int j = 0; j < house.size(); j++) {
            int mindis = 1000000000;
            for (int k = 0; k < m; k++) {
                mindis = min(mindis, dis[j][comb_arr[i][k]]);
            }
            sum += mindis;
        }
        minchicken = min(sum, minchicken);
    }

    cout << minchicken;

    return 0;
}