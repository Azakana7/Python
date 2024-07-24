#include <stdio.h>

int main() {
    int a, b, c;

    // Read the values of a, b, and c from the user
    scanf("%d %d %d", &a, &b, &c);

    // Check if it is not a triangle
    if ((a >= b + c) || (b >= a + c) || (c >= a + b)) {
        printf("Bukan Segitiga\n");
    } else {
        // Check if it is an equilateral triangle
        if ((a == b) && (b == c)) {
            printf("Segitiga Sama Sisi\n");
        }
        // Check if it is an isosceles triangle
        else if ((a == b) || (b == c) || (a == c)) {
            printf("Segitiga Sama Kaki\n");
        }
        // Otherwise, it is a scalene triangle
        else {
            printf("Segitiga Sembarang\n");
        }
    }

    return 0;
}

