#include <stdio.h>

int main()
{
    int n, result = 0;
    scanf("%d", &n);
    
    int i = 1;
    while (true) {
        if (result >= n)
            break;
        result += i;
        i++;
    }
    printf("%d", result);
    
    return 0;
}