#include <cstdio>
#include <cmath>

int fungsi(int &a, int &b, int &x, int &k) {
    if (k == 1) {
        return abs(a * x + b);
    } else {
        int temp = abs(a * x + b);
        k--;
        return fungsi(a, b, temp, k);
    }
}

int main() {
    int a, b, k, x;
    scanf("%d %d %d %d", &a, &b, &k, &x);

    x = fungsi(a, b, x, k);
    printf("%d\n", x);

    return 0;
}