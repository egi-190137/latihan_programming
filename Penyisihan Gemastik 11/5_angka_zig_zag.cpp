#include <iostream>

using namespace std;

int solve(int (&arr)[], int &size) {
    int count = 0;

    for (int i = 0; i < size-2; i++ ) {
        for (int j = i+1; j < size-1; j++) {
            for (int k = j+1; k < size; k++) {
                if ((arr[i] < arr[j] && arr[j] > arr[k])
                    || (arr[i] > arr[j] && arr[j] < arr[k])) {
                    cout << arr[i] << " " << arr[j] << " " << arr[k] << endl;
                    count++;
                }
            }
        }
    }
    cout << endl;
    return count;
}

int main() {
    int t;
    cin >> t;

    int result[t];
    for (int i = 0; i < t; i++) {
        int n;
        cin >> n;
        int arr[n];
        for (int j = 0; j < n; j++) {
            cin >> arr[j];
        }
        result[i] = solve(arr,n);
    }

    for (int i = 0; i < t; i++) {
        cout << result[i] << endl;
    }


    return 0;
}