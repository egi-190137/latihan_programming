#include <iostream>

using namespace std;

int catat[9];
int pernah[9];

void tulis(int &kedalaman, int &n) {
    if (kedalaman >= n) {
        bool zigzag = true;
        for (int i = 1; i < n-1; i++) {
            bool cond1 = catat[i-1] < catat[i] && catat[i] > catat[i+1];
            bool cond2 = catat[i-1] > catat[i] && catat[i] < catat[i+1];
            if ( !(cond1 || cond2) ) {
                zigzag = false;
            }
        }
        if (zigzag) {
            for (int i = 0; i < n; i++) {
                cout << catat[i];
            }
            cout << endl;
        }

    } else {
        for (int i = 1; i <= n; i++) {
            if (!pernah[i-1]) {
                pernah[i-1] = true;
                catat[kedalaman] = i;

                int temp = kedalaman+1;
                tulis(temp, n);
                pernah[i-1] = false;
            }
        }
    }
}

int main() {
    int n;
    cin >> n;
    int arg = 0;
    tulis(arg, n);
}