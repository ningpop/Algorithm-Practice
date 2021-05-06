#include <stdio.h>

int main()
{
    char a, i;
    scanf("%c", &a);
    i = 'a';
    while(true)
    {
        printf("%c ", i);
        if (i == a)
            break;
        i++;
    }

    return 0;
}