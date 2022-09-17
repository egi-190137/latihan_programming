#include <cstdio>

int main() {
    int angka;
    scanf("%d", &angka);
    for (int i = 1; i <= angka; i++) {
        if (i%10 == 0) {
            continue;
        } else if (i == 42) {
            printf("ERROR\n");
            break;
        } else {
            printf("%d\n", i);
        }
    }
    
    return 0;
}