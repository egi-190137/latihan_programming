#include <iostream>

using namespace std;

int * findDivisibleSubSequence(int *arr, int n) {
    int sum[n], seenInIndex[n], a, len;

    for (int i = 0; i < n; i++) {
        if (i == 0) {
            sum[i] = arr[i];
        } else {
            sum[i] = sum[i-1] + arr[i];
        }
    }

    // fill array seenIndex = -1
    for (int i = 0; i < n; i++) {
        seenInIndex[i] = -1;
    }

    for (int i = 0; i < n; i++) {
        if (seenInIndex[sum[i] % n] == -1) {
            seenInIndex[sum[i] % n] = i;
        } else {
            a = seenInIndex[sum[i] % n];
            len = i - a;
            int result[len];
            for (int j = 0; j < len; j++) {
                if (j == 0) {
                    result[j] = a + 1;
                } else {
                    result[j] = result[j-1];
                }
            }
            return result;
        }
    }
}

int main() {
    int n;
    cin >> n;

    int arr[n];
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    int result[] = findDivisibleSubSequence(arr, n);

}