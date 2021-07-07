# 2021.07.07
# 풀이시간 37분 / 제한시간 20분
# 정답 및 풀이시간 초과

def fixed_pointing(array: list, start: int, end: int):
    mid = (start + end) // 2

    value = array[mid]
    idx = array.index(value)

    if idx == value:
        return value
    elif start == mid or mid == end:
        return -1
    elif idx < value:
        return fixed_pointing(array, start, mid)
    elif idx > value:
        return fixed_pointing(array, mid, end)
    else:
        return -1


n = int(input())
array = list(map(int, input().split()))

start = 0
end = len(array) - 1
print(fixed_pointing(array, start, end))