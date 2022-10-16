#include <iostream>
#include <math.h>

using namespace std;

int main() {
    int a = 5;
    int b = 0;

    float c;
    if (b == 0) {
        c = INFINITY;
    } else {
        c = a / b;
    }

    cout << c << endl;
}