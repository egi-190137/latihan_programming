#include <cstdio>
#include <cmath>

using namespace std;

int main() {
    int n;
    scanf("%d", &n);
    
    int angka[n];
    for (int i = 0; i < n; i++) {
        scanf("%d", &angka[i]);
    }

    for (int i = 0; i < n; i++) {
        if (angka[i] <= 1) {
            printf("YA\n");
        } else {
            int pembagi = 0;
            for (int j = 2; j <= sqrt(angka[i]); j++) {
                if (angka[i] % j == 0) {
                    if (j == sqrt(angka[i])) {
                        pembagi++;
                    } else {
                        pembagi += 2;
                    }
                }
                if (pembagi > 2) {
                    break;
                }
            }
            if (pembagi > 2) {
                printf("BUKAN\n");
            } else {
                printf("YA\n");
            }
        }
    }
    
    return 0;
}