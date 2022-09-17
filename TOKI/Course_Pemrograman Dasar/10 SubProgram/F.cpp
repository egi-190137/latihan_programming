#include <cstdio>
#include <cmath>

int main() {
    int n, d;
    scanf("%d %d", &n, &d);

    int x[n], y[n];
    for (int i = 0; i < n; i++) {
        scanf("%d %d", &x[i], &y[i]);
    }
    
    int jarak, terdekat, terjauh;
    for (int i = 0; i < n-1; i++) {
        for (int j = i+1; j < n; j++) {
            jarak = (int) (pow(abs(x[i]-x[j]), d)) + pow(abs(y[i]-y[j]), d);

            if (i == 0 && j == 1) {
                terdekat = jarak;
                terjauh = jarak;
            }

            if (jarak > terjauh) {
                terjauh = jarak;
            } else if (jarak < terdekat) {
                terdekat = jarak;
            }
        }
    }

    printf("%d %d\n", terdekat, terjauh);
}