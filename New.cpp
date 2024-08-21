#include <iostream>
using namespace std;

int main() {
    int i;
    float suhu[5]; // Array dengan 5 elemen bertipe float

    // Membaca dari keyboard dan meletakkan ke array
    cout << "Masukkan 5 buah data suhu" << endl;
    for (i = 0; i < 5; i++) {
        cout << i + 1 << ". ";
        cin >> suhu[i];
    }

    // Menampilkan isi array ke layar
    cout << "Data suhu yang Anda masukkan :" << endl;
    for (i = 0; i < 5; i++) {
        cout << suhu[i] << endl;
    }

    return 0;
}
