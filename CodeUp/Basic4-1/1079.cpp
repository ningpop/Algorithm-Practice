#include <stdio.h>

int main()
{
    char a;
    while (true)
    {
        scanf("%c ", &a);
        printf("%c\n", a);
        if (a == 'q')
            break;
    }

    return 0;
}