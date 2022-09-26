#include <iostream>
#include <cmath>

using namespace std;

int main() {
    bool menang = true;
    int n, temp, m;
    cin >> n;

    int p[n];
    for (int i = 0; i < n; i++) {
        cin >> p[i];
    }

    for (int i = 0; i < n; i++) {
        cout << p[i] << " ";
    }

    cout << endl;

    m = p[0];

    for (int i = 1; i < n; i++) {
        int idxTerkecil = i;
        for (int j = i+1; j < n; j++) {
            if (p[idxTerkecil] > p[j]) {
                idxTerkecil = j;
            }
        }
        // if (i != idxTerkecil) {
            // Tukar index
        temp = p[idxTerkecil];
        p[idxTerkecil] = p[i];
        p[i] = temp;

        // cout << "m : " << m << " Ai :" << A[i] << " Bi : " << B[i] << endl;
        if (p[i] > m) {
            menang = false;
            break;
        } else {
            m -= p[i];
        }
    }

    if (menang) {
        cout << "menang" << endl;

        for (int i = 0; i < n; i++) {
            cout << p[i];
            if (i == n-1) {
                cout << endl;
            } else {
                cout << " ";
            }
        }
    } else {
        cout << "kalah" << endl;
    }

}