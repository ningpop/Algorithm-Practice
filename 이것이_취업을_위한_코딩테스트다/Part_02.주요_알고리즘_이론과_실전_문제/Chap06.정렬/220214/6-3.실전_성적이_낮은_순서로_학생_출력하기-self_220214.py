# 2022.02.14
# 제한 시간 20분 / 풀이 시간 04분 32초
# 채점 결과: 정답
# 시간복잡도: O(N)

n = int(input())

array = []
for i in range(n):
    name, score = input().split()
    array.append((name, int(score)))

def setting(data):
    return data[1]

array.sort(key=setting)

for i in array:
    print(i[0], end=' ')