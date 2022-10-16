#include <iostream>

using namespace std;

int euclid(int a, int b) {
    if (b == 0) {
        return a;
    } else {
        return euclid(b, a % b);
    }
}

int main() {
    int a, b;
    cout << "Masukkan nilai a : ";
    cin >> a;

    cout << "Masukkan nilai b : ";
    cin >> b;

    cout << a << " " << b << endl;

    int result = euclid(a, b);
    cout << result << endl;
}