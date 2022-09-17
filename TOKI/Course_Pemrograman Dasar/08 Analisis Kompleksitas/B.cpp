#include <cstdio>
#include <cmath>

using std::sqrt;

int main() {
    int n;
    scanf("%d", &n);
    
    int angka[n];
    for (int i = 0; i < n; i++) {
        scanf("%d", &angka[i]);
    }
    

    for (int i = 0; i < n; i++) {
        if (angka[i] <= 1) {
            printf("BUKAN\n");
        } else {
            bool prima = true;
            for (int j = 2; j <= std::sqrt(angka[i]); j++) {
                if (angka[i] % j == 0) {
                    prima = false;
                    break;
                }
            }
            if (prima) {
                printf("YA\n");
            } else {
                printf("BUKAN\n");
            }
        }
    }
     
    return 0;
}