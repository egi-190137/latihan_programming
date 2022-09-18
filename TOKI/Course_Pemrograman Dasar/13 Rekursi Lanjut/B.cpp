#include <iostream>
#include <string>

using namespace std;

string pegunungan(int &tinggi) {
    if (tinggi == 1) {
        return "*\n";
    } else {
        string temp = "";
        for (int i = 0; i < tinggi; i++) {
            temp += "*";
        }
        int arg = tinggi-1;
        return pegunungan(arg) + temp + "\n" + pegunungan(arg);
    }

}
int main() {
    int tinggi;
    cin >> tinggi;
    cout << pegunungan(tinggi) << endl;

}