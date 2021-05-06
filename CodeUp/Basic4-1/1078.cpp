#include <stdio.h>

int main()
{
    int a, result = 0;
    scanf("%d", &a);
    for (int i = 0; i <= a; i+=2) {
        result += i;
    }
    printf("%d", result);

    return 0;
}