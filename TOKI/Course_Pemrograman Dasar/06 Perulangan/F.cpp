#include <cstdio>

int main() {
    int angka;
    scanf("%d", &angka);
    int faktor = angka;
    while (faktor >= 1) {
        if (angka % faktor == 0) {
            printf("%d\n", faktor);
        }
        faktor--;
    }
    return 0;
}