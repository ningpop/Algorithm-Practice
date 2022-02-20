# 2022.02.16
# 제한 시간 30분 / 풀이 시간 19분 56초
# 채점 결과: 정답
# 시간복잡도: O(N*M)

n, m = map(int, input().split())

array = [100] * 10001

kinds_of_coin = []
for i in range(n):
    coin = (int(input()))
    kinds_of_coin.append(coin)
    array[coin] = 1

for i in range(1, m + 1):
    if array[i] == 100:
        for j in kinds_of_coin:
            if array[i - j] != 100:
                array[i] = min(array[i], array[i - j] + 1)

if array[m] == 100:
    print(-1)
else:
    print(array[m])