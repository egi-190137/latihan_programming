#include <cstdio>

int main() {
    int n, pembagi, count;
    scanf("%d", &n);

    pembagi = 2; 
    while (n > 1) {
        count = 0;
        while (n % pembagi == 0) {
            n /= pembagi;
            count++;
        }
        if (count > 0) {
            printf("%d", pembagi);
            if (count > 1) {
                printf("^%d", count);
            }
            if (n > 1) {
                printf(" x ");
            }
        }
        pembagi++;
    }
    printf("\n");

    return 0;
}