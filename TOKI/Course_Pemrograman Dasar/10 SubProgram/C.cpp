#include <cstdio>

int reverse(int &x) {
    int result = 0;
    while (x > 0) {
        result = (result * 10) + x % 10;
        x /= 10;
    }

    return result;
}

int main() {
    int a, b;
    scanf("%d %d", &a, &b);
    
    a = reverse(a);
    b = reverse(b);

    int c = a + b;
    c = reverse(c);
    printf("%d\n", c);

    return 0;
}