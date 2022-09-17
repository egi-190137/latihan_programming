#include <cstdio>

int main() {
    int n, m, p;
    scanf("%d %d %d", &n, &m, &p);
    
    int A[n][m], B[m][p], C[n][p];
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            scanf("%d", &A[i][j]);
        }
    }

    for (int i = 0; i < m; i++) {
        for (int j = 0; j < p; j++) {
            scanf("%d", &B[i][j]);
        }
    }
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < p; j++) {
            C[i][j] = 0;
            for (int k = 0; k < m; k++) {
                C[i][j] += A[i][k] * B[k][j];
            }
            printf("%d", C[i][j]);
            if (j < p-1) {
                printf(" ");
            }
        }
        printf("\n");
    }

    return 0;
}