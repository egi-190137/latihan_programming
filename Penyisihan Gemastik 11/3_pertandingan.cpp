#include <iostream>

using namespace std;

int main() {
    int n, m, temp;
    cin >> n >> m;


    int A[n], B[n];
    for (int i = 0; i < n; i++) {
        cin >> A[i];
    }

    for (int i = 0; i < n; i++) {
        cin >> B[i];
    }

    for (int i = 0; i < n; i++) {
        int idxTerkecil = i;
        for (int j = i+1; j < n; j++) {
            if (A[idxTerkecil] > A[j]) {
                idxTerkecil = j;
            }
        }

        // Tukar index A dan B
        temp = A[idxTerkecil];
        A[idxTerkecil] = A[i];
        A[i] = temp;

        temp = B[idxTerkecil];
        B[idxTerkecil] = B[i];
        B[i] = temp;

        if (A[i] > m) {
            break;
        } else {
            m += B[i];
        }
    }

    cout << m << endl;

}