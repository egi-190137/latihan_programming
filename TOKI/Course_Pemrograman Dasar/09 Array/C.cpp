#include <cstdio>
#include <map>
#include <iterator>

using namespace std;

int main() {
    int n;
    scanf("%d", &n);
    
    int temp;
    map<int, int> map_angka;
    for (int i = 0; i < n; i++) {
        // scanf("%d", &angka[i]);
        scanf("%d", &temp);
        if (map_angka.find(temp) == map_angka.end()) {
            map_angka[temp] = 1;
        } else {
            map_angka[temp]++;
        }
    }

    int key_terbesar = map_angka.begin()->first;
    map<int, int>::iterator itr;

    for (itr = map_angka.begin(); itr != map_angka.end(); ++itr) {
        if (map_angka[key_terbesar] == itr->second && key_terbesar < itr->first) {
            key_terbesar = itr->first;
        } else if (map_angka[key_terbesar] < itr->second) {
            key_terbesar = itr->first;            
        }
    }
    printf("%d\n", key_terbesar);
    return 0;
}