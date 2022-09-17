#include <cstdio>
#include <cstring>

char kata[100];

int main() {
    scanf("%s", kata);

    for (int i = 0; i < strlen(kata); i++) {
        int ord = (int) kata[i];
        if (65 <= ord && ord <= 90) {
            ord += 32;
        } else {
            ord -= 32;
        }
        kata[i] = ord;
    }
    printf("%s\n", kata);

}