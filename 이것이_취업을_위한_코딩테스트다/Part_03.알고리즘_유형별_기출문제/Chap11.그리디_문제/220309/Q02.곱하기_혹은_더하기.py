# 2022.03.11
# 제한 시간 30분 / 풀이 시간 10분 43초
# 채점 결과: 정답
# 시간복잡도: O(N)

s = input()

number_list = []
for i in s:
    number_list.append(int(i))

result = 0
for i in range(len(number_list)):
    if number_list[i] == 0 or number_list[i] == 1:
        result += number_list[i]
    else:
        if result == 0:
            result += number_list[i]
        else:
            result *= number_list[i]

print(result)