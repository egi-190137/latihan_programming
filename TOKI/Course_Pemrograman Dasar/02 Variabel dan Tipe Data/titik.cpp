#include <cstdio>

struct titik {
    int x, y;
};

titik a, b;

int main() {
    a.x = 1;
    a.y = 2;
    
    b.x = 3;
    b.y = 4;
    printf("a.x = %d\t a.y = %d\n", a.x, a.y);
    printf("b.x = %d\t b.y = %d\n", b.x, b.y);
    return 0;
}

