#include <cstdio>
#include <cstdlib>

struct titik {
    int x, y;
};

int main() {
    titik titik1;
    titik titik2;
    scanf("%d %d", &titik1.x, &titik1.y);
    scanf("%d %d", &titik2.x, &titik2.y);

    int jarak = abs(titik1.x-titik2.x) + abs(titik1.y-titik2.y);
    printf("%d\n", jarak);

    return 0;
}