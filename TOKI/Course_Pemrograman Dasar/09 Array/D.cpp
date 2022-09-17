#include <cstdio>

int main() {
    int baris, kolom;
    scanf("%d %d", &baris, &kolom);
    
    int ar[baris][kolom];
    for (int i = 0; i < baris; i++) {
        for (int j = 0; j < kolom; j++) {
            scanf("%d", &ar[i][j]);
        }
    }

    int tmp = baris;
    baris = kolom;
    kolom = tmp;

    int result[baris][kolom];
    for (int i = 0; i < baris; i++) {
        for (int j = 0; j < kolom; j++) {
            result[i][j] = ar[kolom-j-1][i];
        }
    }
    for (int i = 0; i < baris; i++) {
        for (int j = 0; j < kolom; j++) {
            printf("%d", result[i][j]);
            if (j < kolom-1) {
                printf(" ");
            }
        }
        printf("\n");
    }

}