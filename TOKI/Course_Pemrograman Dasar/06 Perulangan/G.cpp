// #include <cstdio>

// int main() {
//     int N;
//     scanf("%d", &N);
//     int angka[N];
//     for (int i = 0; i < N; i++) {
//         scanf("%d", &angka[i]);
//     }

//     int terbesar = angka[0];
//     int terkecil = angka[0];
//     for (int i = 1; i < N; i++) {
//         if (terbesar < angka[i]) {
//             terbesar = angka[i];
//         }
//         if (terkecil > angka[i]) {
//             terkecil = angka[i];
//         }
//     }
//     printf("%d %d\n", terbesar, terkecil);
      
//     return 0;
// }

#include <cstdio>

int main() {
    int N;
    scanf("%d", &N);
    int temp, terbesar, terkecil;
    
    for (int i = 0; i < N; i++) {
        scanf("%d", &temp);
        if (i == 0) {
            terbesar = temp;
            terkecil = temp;
        } else {
            if (terbesar < temp) {
                terbesar = temp;
            }
            if (terkecil > temp) {
                terkecil = temp;
            }
        }
    }
    printf("%d %d\n", terbesar, terkecil);
      
    return 0;
}