#include <stdio.h>

int main()
{
    int a, d, n;
    scanf("%d %d %d", &a, &d, &n);
    
    int result = a;
    for (int i = 2; i <= n; i++) {
        result += d;
    }
    printf("%d", result);
    
    
    return 0;
}