#include <iostream>

using namespace std;

bool cekBilangan(int &angka) {
    return (angka >= 0 && angka <= 100);
}

int * urutanAneh(int (&arr)[], int &size) {
    int temp;
    for (int i = 0; i < size-1; i++) {
        for (int j = size-1; j > i; j--) {
            if ( (arr[j-1]%10 == arr[j]%10 && arr[j-1] > arr[j]) || arr[j-1]%10 > arr[j]%10) {
                temp = arr[j-1];
                arr[j-1] = arr[j];
                arr[j] = temp;
            }
        }
    }
    return arr;
}

int main() {
    int n, temp;
    cin >> n;

    int arr[n];
    for (int i = 0; i < n; i++) {
        do
        {
            cin >> temp;
        } while (!cekBilangan(temp));
        
        arr[i] = temp;       
    }
    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }

    cout << endl;

    int *result;
    result = urutanAneh(arr, n);  

    for (int i = 0; i < n; i++) {
        cout << result[i] << endl;
    }
}