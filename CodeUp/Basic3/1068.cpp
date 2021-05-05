#include <stdio.h>

int main()
{
    int a;
    scanf("%d", &a);
    
    if (90 <= a && a <= 100) { printf("A\n"); }
    else if (70 <= a && a <= 89) { printf("B\n"); }
    else if (40 <= a && a <= 69) { printf("C\n"); }
    else if (0 <= a && a <= 39) { printf("D\n"); }

    return 0;
}