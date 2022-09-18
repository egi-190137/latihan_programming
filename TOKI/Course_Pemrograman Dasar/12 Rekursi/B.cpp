#include <cstdio>

int faktorial(int &n) {
    if (n == 1) {
        return 1;
    } else if (n%2 == 0) {
        int temp = n-1;
        return n/2 * faktorial(temp);
    } else {
        int temp = n-1;
        return n * faktorial(temp);
    }
}

int main() {
    int n; 
    scanf("%d", &n);
    int hasil = faktorial(n);
    printf("%d\n", hasil);
}