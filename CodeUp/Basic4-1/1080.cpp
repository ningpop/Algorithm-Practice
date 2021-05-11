#include <stdio.h>

int main()
{
    int i, n, sum = 0;
    scanf("%d", &n);
    
    for (i = 0; sum < n; i++) {
        sum += i;
    }
    printf("%d\n", i-1);
    
    return 0;
}