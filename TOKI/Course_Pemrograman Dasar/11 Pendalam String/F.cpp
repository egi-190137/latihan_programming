#include <cstdio>
#include <cstring>

char kata[100];
char hasil[1001];
bool underscore = false;

int main() {
    scanf("%s", kata);

    for (int i = 0; i < strlen(kata); i++) {
        int ord = (int) kata[i];
        if (65 <= ord && ord <= 90) {
            // ord += 32;
            hasil[strlen(hasil)] = '_';
            hasil[strlen(hasil)] = (kata[i] + 32);
        } else if (kata[i] == '_') {
            underscore = true;
        } else if (underscore) {
            hasil[strlen(hasil)] = (kata[i] - 32);
            underscore = false;
        } else {
            hasil[strlen(hasil)] = kata[i];
        }
        // kata[i] = ord;
    }
    printf("%s\n", hasil);

}