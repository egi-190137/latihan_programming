#include <cstdio>
#include <cmath>

int fungsi(int &a, int &b, int &x) {
    return abs(a * x + b);
}

int main() {
    int a, b, k, x;
    scanf("%d %d %d %d", &a, &b, &k, &x);
    for (int i = 0; i < k; i++) {
        x = fungsi(a, b, x);
    }
    printf("%d\n", x);

    return 0;
}