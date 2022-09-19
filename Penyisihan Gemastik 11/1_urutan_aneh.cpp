#include <iostream>

using namespace std;

int main() {
    int n, temp;
    cin >> n;

    int arr[n];
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }

    for (int i = 0; i < n-1; i++) {
        for (int j = n-1; j > 0; j--) {
            if ( (arr[j-1]%10 == arr[j]%10 && arr[j-1] > arr[j]) || arr[j-1]%10 > arr[j]%10) {
                temp = arr[j-1];
                arr[j-1] = arr[j];
                arr[j] = temp;
            }
        }
    }

    for (int i = 0; i < n; i++) {
        cout << arr[i] << endl;
    }
}