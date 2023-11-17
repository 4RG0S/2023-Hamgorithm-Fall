#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m;
    cin >> n;

    vector<int> crain(n);
    for (int i = 0; i < n; i++) {
        cin >> crain[i];
    }
    sort(crain.begin(), crain.end(), greater<int>());

    cin >> m;
    vector<int> box(m);
    for (int i = 0; i < m; i++) {
        cin >> box[i];
    }
    sort(box.begin(), box.end(), greater<int>());

    if (crain[0] < box[0]) {
        cout << "-1";
        return 0;
    }
    int cnt = 0;
    while (!box.empty()) {
        cnt++;
        for (int i = 0; i < crain.size(); i++) {
            for (int j = 0; j < box.size(); j++) {
                if (crain[i] >= box[j]) {
                    box.erase(box.begin() + j);
                    break;
                }
            }
        }
    }

    cout << cnt;

    return 0;
}