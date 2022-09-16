#include <cstdio>

int main() {
    int N, hasil, Bi;
    scanf("%d", &N);
    hasil = 0;
    for (int i = 0; i < N; i++) {
        scanf("%d", &Bi);
        hasil += Bi;
    }
    printf("%d\n", hasil);

    return 0;
}