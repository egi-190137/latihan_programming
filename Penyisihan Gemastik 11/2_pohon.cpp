#include <iostream>
#include <math.h>
#include <array>
#include <algorithm>
#include <iterator>

using namespace std;

struct titik {
    int x, y;
};

struct line {
    float gradient;
    bool position; // 0 dikiri / dibawah pak  blangkon // 1 dikanan / diatas pak  blangkon 
};

int main() {
    int n, xb, yb;
    titik arr[n];
    line lines[n];

    int test[] = {1, 2,3 4, 5};
    cin >> n;
    cin >> xb;
    cin >> yb;

    cout << n << " " << xb << " " << yb << endl;
    for (int i = 0; i < n; i++) {
        cin >> arr[i].x;
        cin >> arr[i].y;
    }
    bool idx = find(begin(test), end(test), 1) != end(test);

    for (int i = 0; i < n; i++) {
        float gradient = (arr[i].y-yb) / (arr[i].x-xb);
        bool position;

        if (isinf(gradient)) {
            position = (arr[i].y > yb);
        } else {
            position = (arr[i].x > xb);
        }

        line temp;
        temp.gradient = gradient;
        temp.position = position; 

        // Cek apakah ada di array lines
        // bool idx = find(begin(lines), end(lines), temp) != end(lines);
        
        // if (idx != end(lines)) {
        //     cerr << "Found at position " << distance(lines, idx) << endl;
        // } else {
        //     cerr << "Not found" << endl;
        // }

    }



    // cout << sizeof(arr)/sizeof(arr[0]) << endl;

    // for (int i = 0; i < sizeof(arr)/sizeof(arr[0]); i++) {
    //     cout << arr[i] << endl;
    // }
}