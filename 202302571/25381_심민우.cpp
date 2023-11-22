#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    string s;
    cin >> s;

    int cnt = 0;
    queue<int> A, B, C;
    for (int i = 0; i < s.size(); i++) {
        if (s[i] == 'A')
            A.push(i);
        else if (s[i] == 'B')
            B.push(i);
        else if (s[i] == 'C')
            C.push(i);
    }

    while (!B.empty() && !C.empty()) {
        int b = B.front();
        int c = C.front(); C.pop();

        if (b < c) {
            B.pop();
            cnt++;
        }
    }

    while (!A.empty() && !B.empty()) {
        int a = A.front();
        int b = B.front(); B.pop();

        if (a < b) {
            A.pop();
            cnt++;
        }
    }

    cout << cnt;
    return 0;
}