#include <cstdio>

int matrix[3][3];

int main() {
    for (short i = 0; i < 3; i++) {
        scanf("%d %d %d", &matrix[i][0], &matrix[i][1], &matrix[i][2]);
    }

    for (short i = 0; i < 3; i++) {
        printf("%d %d %d\n", matrix[0][i], matrix[1][i], matrix[2][i]);
    }
    return 0;
    
}