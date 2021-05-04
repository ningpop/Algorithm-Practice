#include <stdio.h>

int main()
{
    long long int a, b, c;
    scanf("%d %d %d", &a, &b, &c);
    printf("%d\n%.1f", a+b+c, (a+b+c)/3.0);
    
    return 0;
}