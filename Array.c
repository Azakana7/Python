#include <stdio.h>
#include <vector>

using namespace std;

void cetaklarik(int ukuran, vector<int> larik) {
    int i;
    for (i = 0; i < ukuran; i++) {
        printf("%d\n", larik[i]);
    }
}

int main() {
    vector<int> bilangan;
    int i;

    for (i = 0; i < 10; i++) {
        bilangan.push_back(i);
    }

    cetaklarik(10, bilangan);

    return 0;
}
