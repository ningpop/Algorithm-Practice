# 2022.02.15
# 제한 시간 30분 / 풀이 시간 06분 22초
# 채점 결과: 정답
# 시간복잡도: O(N)

n = int(input())
array = list(map(int, input().split()))

m = int(input())
request = list(map(int, input().split()))

array.sort()

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

for i in request:
    result = binary_search(array, i, 0, len(array) - 1)
    if result == None:
        print("no", end=' ')
    else:
        print("yes", end=' ')