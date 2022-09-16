#include <cstdio>

int main() {
    int a;
    scanf("%d", &a);

    if (a > 0) {
        printf("positif\n");
    } else if (a < 0) {
        printf("negatif\n");
    } else {
        printf("nol\n");
    }
    return 0;
}