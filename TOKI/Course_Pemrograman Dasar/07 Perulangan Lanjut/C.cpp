#include <cstdio>

int main() {
    int n;
    int angka = 0;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < i+1; j++) {
            printf("%d", angka);
            if (angka == 9) {
                angka = 0;
            } else {
                angka++;
            }
        }
        // for (int j = 0; j < n-i-1; j++) {
        //     printf(" ");
        // }
        printf("\n");
    }
    return 0;
}