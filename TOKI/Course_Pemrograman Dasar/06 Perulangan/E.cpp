#include <cstdio>

int main() {
    int angka;
    scanf("%d", &angka);
    while (angka % 2 == 0) {
        angka /= 2;
    }
    if (angka == 1) {
        printf("ya\n");
    } else {
        printf("bukan\n");
    }
    return 0;
}