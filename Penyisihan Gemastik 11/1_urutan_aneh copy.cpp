#include <iostream>

using namespace std;

// int * urutanAneh(int *arr) {
    // int temp;
    // for (int i = 0; i < (sizeof(arr)/sizeof(arr[0])) - 1; i++) {
    //     for (int j = (sizeof(arr)/sizeof(arr[0])) - 1; j > i; j--) {
    //         if ( (arr[j-1]%10 == arr[j]%10 && arr[j-1] > arr[j]) || arr[j-1]%10 > arr[j]%10) {
    //             temp = arr[j-1];
    //             arr[j-1] = arr[j];
    //             arr[j] = temp;
    //         }
    //     }
    // }
    // return arr;
// }

int main() {
    int n, temp;
    cin >> n;

    int arr[n];
    for (int i = 0; i < n; i++) {
        
        do {
            cin >> temp;
        } while (100 >= temp && temp >= 0 );

        arr[i] = temp;
    }

    for (int i = 0; i < n-1; i++) {
        for (int j = n-1; j > i; j--) {
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