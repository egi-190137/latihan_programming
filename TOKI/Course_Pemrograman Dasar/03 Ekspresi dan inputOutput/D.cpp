#include <cstdio>

int main() {
    int a, b, n, m;
    scanf("%d %d", &n, &m);
    a = n /m;
    b = n % m;
    printf("masing-masing %d\n", a);
    printf("bersisa %d\n", b);
    return 0;
}