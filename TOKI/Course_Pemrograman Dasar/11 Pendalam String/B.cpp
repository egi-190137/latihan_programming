#include <cstdio>
#include <string>
#include <iostream>

using namespace std;

int main() {
    string s, t;
    cin >> s >> t;
    int idx = 0;
    while (s.find(t) >= 0 && s.find(t) < s.length()) {
        s = s.substr(0, s.find(t)) + s.substr(s.find(t)+t.length(), s.length());
    }
    cout << s << endl;
    return 0;
}