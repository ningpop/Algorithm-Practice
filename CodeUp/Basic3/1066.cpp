#include <stdio.h>

int main()
{
    int a, b, c;
    scanf("%d %d %d", &a, &b, &c);
    
    if(a%2==0) printf("%s", "even\n");
    else printf("%s", "odd\n");

    if(b%2==0) printf("%s", "even\n");
    else printf("%s", "odd\n");

    if(c%2==0) printf("%s", "even\n");
    else printf("%s", "odd\n");

    return 0;
}