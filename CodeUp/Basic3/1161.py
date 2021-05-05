def even_or_odd(num: int) -> str:
    if num%2 == 0:
        return "짝수"
    return "홀수"

a, b = map(int, input().split())
print(even_or_odd(a) + '+' + even_or_odd(b) + '=' + even_or_odd(a+b))