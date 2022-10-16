#include <iostream>

using namespace std;

int walkTober(int **arr, int m, int n, int p) {
    int amount = 0;
    int terbesar;
    for (int i = 0; i < n; i++) {
        terbesar = arr[0][i];
        for (int j = 1; j < m; j++) {
            if (terbesar < arr[j][i]) {
                terbesar = arr[j][i];
            }
        }
        amount += (terbesar - arr[p-1][i]);
    }
    return amount;
}

int main() {
    int t;
    cin >> t;

    int result[t];

    for (int i = 0; i < t; i++) {
        int m, n, p;
        cin >> m >> n >> p;
        int **arr;
        arr = new int *[m];
        for (int j = 0; j < m; j++) {
            arr[j] = new int[n];
            for (int k = 0; k < n; k++) {
                cin >> arr[j][k];
            }
        }
        result[i] = walkTober(arr, m, n, p);
    }

    for (int i = 0; i < t; i++) {
        cout << "Case #" << (i+1) << ": " << result[i] << endl;
    }
}