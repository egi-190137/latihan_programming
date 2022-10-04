#include <cstdio>
#include <iostream>

using namespace std;

int catat[9];

void tulis(int &kedalaman, int &n, int&k) {
    if (kedalaman >= k) {
        for (int i = 0; i < k; i++) {
            cout << catat[i];
            if (i < k-1) {
                cout << " ";
            } 
        }
        cout << endl; 
    } else {
        int awal;
        if (kedalaman == 0) {
            awal = 1;
        } else {
            awal = catat[kedalaman-1] + 1;
        }

        // int akhir;
        // if (kedalaman == k) {
        //     akhir = n;
        // } else {
        //     akhir = n - (2-kedalaman-1);
        // }
        for (int i = awal; i <= n; i++) {
            catat[kedalaman] = i;
            int temp = kedalaman+1;
            tulis(temp, n, k);
        }
    }
}

int main() {
    int n, k;
    cin >> n >> k;

    int temp = 0;
    tulis(temp, n, k);
}