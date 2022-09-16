#include <cstdio>
#include <cmath>

int main() {
    float angka;
    scanf("%f", &angka);
    int floor_angka = floor(angka);
    int ceil_angka = ceil(angka);
    printf("%d %d\n", floor_angka, ceil_angka);
    
    return 0;
}