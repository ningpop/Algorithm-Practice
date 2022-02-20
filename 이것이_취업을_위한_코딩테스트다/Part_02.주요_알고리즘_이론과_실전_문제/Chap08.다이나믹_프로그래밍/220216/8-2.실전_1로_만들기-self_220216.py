# 2022.02.16
# 제한 시간 20분 / 풀이 시간 44분 02초
# 채점 결과: 시간 초과 및 정답
# 시간복잡도: O(N^2)

def operate(value: int, way: int):
    if way == 5:
        return value // 5
    elif way == 3:
        return value // 3
    elif way == 2:
        return value // 2
    else:
        return value - 1

x = int(input())

array = [0] * (x + 1)
array[0] = -1
for i in [1, 2, 3, 5]:
    array[i] = 1

for i in range(4, x + 1):
    if array[i] == 0:
        min_op = []
        if i % 5 == 0:
            min_op.append(5)
        if i % 3 == 0:
            min_op.append(3)
        if i % 2 == 0:
            min_op.append(2)
        min_op.append(1)
        
        min_count = 30000
        for j in min_op:
            pre_value = operate(i, j)
            min_count = min(array[pre_value] + 1, min_count)
        array[i] = min_count

print(array[x])