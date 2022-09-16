#include <cstdio>

int main() {
    int a;
    scanf("%d", &a);

    if (a > 0) {
        if (a % 2 == 0) {
            printf("%d\n", a);
        }
    }
    return 0;
}