#include <stdio.h>

int main()
{
    int n;
    while(true)
    {
        scanf("%d", &n);
        if (n == 0)
            break;
        printf("%d\n", n);
    }

    return 0;
}