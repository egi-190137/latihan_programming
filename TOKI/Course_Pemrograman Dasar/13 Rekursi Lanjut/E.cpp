#include <iostream>

using namespace std;

int m[128][128];
int nJawaban = 0;
string jawaban[128*128];

bool homogen(int &r, int &c, int &k) {
    int val = m[r][c];
    for (int i = r; i < r+k; i++) {
        for (int j = c; j < c+k; j++) {
            if (m[i][j] != val) {
                return false;
            }
        }
    }
    return true;
}

void quadtree(int &r, int &c, int &k, string &s) {
    if (homogen(r, c, k)) {
        if (m[r][c] == 1) {
            jawaban[nJawaban] = "1" + s;
            nJawaban++;
        }
    } else {
        int temp_r = r;
        int temp_c = c;
        int temp_k = k/2;
        string temp_s = s+"0";
        quadtree(temp_r, temp_c, temp_k, temp_s);

        temp_r = r;
        temp_c = c + (k/2);
        temp_k = k/2;
        temp_s = s+"1";
        quadtree(temp_r, temp_c, temp_k, temp_s);

        temp_r = r + (k/2);
        temp_c = c;
        temp_k = k/2;
        temp_s = s+"2";
        quadtree(temp_r, temp_c, temp_k, temp_s);

        temp_r = r + (k/2);
        temp_c = c + (k/2);
        temp_k = k/2;
        temp_s = s+"3";
        quadtree(temp_r, temp_c, temp_k, temp_s);
    }
}

int main() {
    int r, c;
    cin >> r >> c;

    int maxRc = max(r, c);
    int pow1 = 1;
    while (pow1 < maxRc) {
        pow1 *= 2;
    }

    for (int i = 0; i < pow1; i++) {
        for (int j = 0; j < pow1; j++) {
            m[i][j] = 0;
        }
    }

    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
            cin >> m[i][j];
        }
    }

    int arg_rc = 0;
    string arg_s = "";
    
    quadtree(arg_rc, arg_rc, pow1, arg_s);
    cout << nJawaban << endl;
    for (int i = 0; i < nJawaban; i++) {
        cout << jawaban[i] << endl;
    }

}

