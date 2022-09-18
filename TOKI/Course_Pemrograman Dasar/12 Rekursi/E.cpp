#include <string>
#include <iostream>

using namespace std;

string dec2bin(int &angka) {
    if (angka == 1) {
        return "1";
    } else {
        int temp = angka/2;
        return dec2bin(temp) + to_string(angka%2);
    }

}

int main() {
    int angka;
    cin >> angka;
    cout << dec2bin(angka) << endl;
}