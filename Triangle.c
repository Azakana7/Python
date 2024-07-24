#include <stdio.h>

int main()

{

int a, b, c;

scanf("%d %d %d", &a, &b, &c);

if ( (a >= b + c) || (b >= a + c) 1(c >= a + b) ) printf("Bukan Segitiga");

else

if (( a ==b) && ( b ==c)) printf("Segitiga Sama Sisi");

else if (( a ==b) || ( b ==c) || ( a ==c)) printf("Segitiga Sama Kaki");

else printf("Segitiga Sembarang");

return 0;
