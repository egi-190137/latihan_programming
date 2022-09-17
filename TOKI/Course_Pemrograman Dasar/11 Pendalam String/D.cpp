#include <iostream>
#include <string>

using namespace std;

int main() {
    string s1, s2, s3, s4;

    cin >> s1;
    cin >> s2;
    cin >> s3;
    cin >> s4;

    s1 = s1.substr(0,s1.find(s2)) + s1.substr(s1.find(s2)+s2.length(), s1.length());

    s1 = s1.substr(0, s1.find(s3)+s3.length()) + s4 + s1.substr(s1.find(s3)+s3.length(), s1.length());   

    cout << s1 << endl;

}