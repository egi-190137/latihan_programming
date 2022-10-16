#include <iostream>
#include <vector>

using namespace std;

vector<int> SieveOfEratosthenes(int n) {
    vector<int> result;
    bool eliminated[n+1];

    for (int i = 0; i < n+1; i++) {
        eliminated[i] = false;
    }
    

    for (int i = 2; i <= n; i++) {
        if (!eliminated[i]) {
            result.push_back(i);

            int j = i * i;
            while (j <= n) {
                eliminated[j] = true;
                j += i;
            }
        }
    }
    return result;
}

int main() {
    int n;
    cin >> n;

    vector<int> result = SieveOfEratosthenes(n);

    for (auto i = result.begin(); i != result.end(); ++i) {
        cout << *i << " ";
    }

    cout << endl;
}