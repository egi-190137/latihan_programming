#include <iostream>

using namespace std;

int m[128][128];

void makeSquareOne(int &r, int&c, int &k) {
    for (int i = r; i < r+k; i++) {
        for (int j = c; j < c+k; j++) {
            m[i][j] = 1;
        }
    }
}

void printSquare(int r, int c) {
    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
            cout << m[i][j];
            if (j < c-1) {
                cout << " ";
            }
        }
        cout << endl;
    }    
}

void quadtree(int &r, int &c, int &k, int &kedalaman, string &s) {
    if (kedalaman >= s.size()) {
        makeSquareOne(r, c, k);
    } else {
        int arg_r, arg_c, arg_k, arg_kedalaman;
        arg_kedalaman = kedalaman+1;
        if (s[kedalaman] == '0') {
            arg_r = r;
            arg_c = c;
            arg_k = k/2;
        } else if (s[kedalaman] == '1') {
            arg_r = r;
            arg_c = c+(k/2);
            arg_k = k/2;
        } else if (s[kedalaman] == '2') {
            arg_r = r+(k/2);
            arg_c = c;
            arg_k = k/2;
        } else if (s[kedalaman] == '3') {
            arg_r = r+(k/2);
            arg_c = c+(k/2);
            arg_k = k/2;
        }
        quadtree(arg_r, arg_c, arg_k, arg_kedalaman, s);
    }
}

int main() {
    for (int i = 0; i < 128; i++) {
        for (int j = 0; j < 128; j++) {
            m[i][j] = 0;
        }
    }

    int nJawaban, r, c;
    cin >> nJawaban;

    string jawaban[nJawaban];
    for (int i = 0; i < nJawaban; i++) {
        cin >> jawaban[i];
    }

    cin >> r >> c;
    
    int max_rc = max(r, c);
    int pow1 = 1;
    while (pow1 < max_rc) {
        pow1 *= 2;
    }

    int arg_r = 0;
    int arg_c = 0;
    int arg_kedalaman = 1;
    
    for (int i = 0; i < nJawaban; i++) {
        quadtree(arg_r, arg_c, pow1, arg_kedalaman, jawaban[i]);
    } 

    printSquare(r, c);
}