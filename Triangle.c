#include <stdio.h>

int main() {
    int a, b, c;

    
    scanf("%d %d %d", &a, &b, &c);

    
    if ((a >= b + c) || (b >= a + c) || (c >= a + b)) {
        printf("Bukan Segitiga\n");
    } else {
        
        if ((a == b) && (b == c)) {
            printf("Segitiga Sama Sisi\n");
        }
        
        else if ((a == b) || (b == c) || (a == c)) {
            printf("Segitiga Sama Kaki\n");
        }
        
        else {
            printf("Segitiga Sembarang\n");
        }
    }

    return 0;
}

