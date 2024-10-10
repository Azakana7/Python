#include <iostream>

using namespace std;

int main() {

    char a1;
    char a2 ('A');
    char a3 (65);
    char a4 = a3 + 6;

    cout << "Input nilai a1 = ";
    cin >> a1;

    cout << endl << endl;

    cout << "Data variabel char" << endl;
    cout << "a1 = " << a1 << endl;
    cout << "a2 = " << a2 << endl;
    cout << "a3 = " << a3 << endl;
    cout << "a4 = " << a4 << endl;

    return 0;
}

