#include <iostream>
#include <math.h>
#include <array>
#include <algorithm>
#include <iterator>
#include <vector>

using namespace std;

struct titik {
    int x, y;
};

// bool cekGradien(vector<line> &lines, line gradient) {
//     for (const line& line : lines) {
//         if (line == gradient) {
//             return true;
//         }
//     }
//     return false;
// }

struct line {
    float gradient;
    bool position; // 0 dikiri / dibawah pak  blangkon // 1 dikanan / diatas pak  blangkon 
};

int main() {
    int n, xb, yb, delta_x;
    // vector<line> lines;

    // int test[] = {1, 2,3, 4, 5};
    cin >> n;
    cin >> xb;
    cin >> yb;

    titik arr[n];
    line lines[n];

    // cout << n << " " << xb << " " << yb << endl;
    for (int i = 0; i < n; i++) {
        cin >> arr[i].x >> arr[i].y;
    }

    // for (int i = 0; i < n; i++) {
    //     cout << arr[i].x << " " << arr[i].y << endl;
    // }


    // bool idx = find(begin(test), end(test), 1) != end(test);

    for (int i = 0; i < n; i++) {
        float gradient;
        bool position;

        delta_x = arr[i].x-xb;
        if (delta_x == 0) {
            gradient = INFINITY;
        } else {
            gradient = (arr[i].y-yb) / delta_x;
        }

        if (isinf(gradient)) {
            position = (arr[i].y > yb);
        } else {
            position = (arr[i].x > xb);
        }

        // line temp;
        lines[i].gradient = gradient;
        lines[i].position = position;

        // lines[i] = temp;

        
        // // Cek apakah ada di array lines
        // bool idx = find(begin(lines), end(lines), temp) != end(lines);
        
        // if (idx != end(lines)) {
        //     cerr << "Found at position " << distance(lines, idx) << endl;
        // } else {
        //     cerr << "Not found" << endl;
        // }
    }

    int count = 0;
    for (int i = 0; i < n; i++) {
        bool unique = true;
        for (int j = i+1; j < n; j++) {
            if ((lines[i].gradient == lines[j].gradient) && (lines[i].position == lines[j].position)) {
                unique = false;
                break;
            }
        }
        if (unique) {
            count++;
        }

    }

    cout << count << endl;



    // cout << sizeof(arr)/sizeof(arr[0]) << endl;

    // for (int i = 0; i < sizeof(arr)/sizeof(arr[0]); i++) {
    //     cout << arr[i] << endl;
    // }
}