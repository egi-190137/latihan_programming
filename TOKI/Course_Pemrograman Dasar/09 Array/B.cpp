#include <cstdio>
#include <iostream>

using namespace std;

int N, arr[105];

int main() {
    while (scanf("%d", &arr[N]) != EOF) {
        N++;
    }

    N--;
    cout << "\n";
    while (N >= 0) {
        cout << arr[N] << "\n";
        N--;
    }
    // cout << arr[N-1;
    
}