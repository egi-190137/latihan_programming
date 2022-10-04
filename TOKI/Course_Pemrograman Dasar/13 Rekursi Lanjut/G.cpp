#include <iostream>

using namespace std;

int m, n;
int matrix[25][25];
bool visited[25][25];

int count = 0;

void f(int &x, int &y, int &c) {
    if (0 <= x && x < m && 0 <= y && y < n) {
        if (!visited[x][y]) {
            if (matrix[x][y] == c) {
                count++;

                visited[x][y] = true; 

                int temp_x, temp_y;
                
                temp_x = x - 1;
                f(temp_x, y, c);

                temp_x = x + 1;
                f(temp_x, y, c);
                
                temp_y = y - 1;
                f(x, temp_y, c);

                temp_y = y + 1;
                f(x, temp_y, c);
            }
        }
    }
}

int main() {
    for (int i = 0; i < 25; i++) {
        for(int j = 0; j < 25; j++) {
            visited[i][j] = false;
        }
    }

    cin >> m >> n;
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            cin >> matrix[i][j];
        }
    }

    int x, y, c;

    cin >> x >> y;
    c = matrix[x][y];

    f(x, y, c);

    count *= (count - 1);
    cout << count << endl;


}