#include <cstdio>
#include <string>
#include <iostream>

using namespace std;

bool palindrome(string kata) {
    int len = kata.length();
    if (len <= 1) {
        return true;
    } else {
        string substr = kata.substr(1, len-2);
        return (kata[0] == kata[len-1]) && palindrome(substr);
    }
}

int main() {
    string kata;
    getline(cin, kata);

    bool result = palindrome(kata);
    if (result) {
        printf("YA\n");
    } else {
        printf("BUKAN\n");
    }
}