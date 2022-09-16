#include <cstdio>

int main() {
    int angka;
    scanf("%d", &angka);
    if (angka < 10) {
        printf("satuan\n");
    } else if (angka < 100) {
        printf("puluhan\n");
    } else if (angka < 1000) {
        printf("ratusan\n");
    } else if (angka < 10000) {
        printf("ribuan\n");
    } else if (angka < 100000) {
        printf("puluhribuan\n");
    }
    return 0;
}