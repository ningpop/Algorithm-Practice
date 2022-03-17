# 2022.03.17
# 제한 시간 20분 / 풀이 시간 15분 07초
# 채점 결과: 예외 테스트 케이스 만족 X (숫자가 들어있지 않을 때, 숫자를 붙이지 않아야함)
# 시간복잡도: O(N)
# 문제 링크: -

s = input()

new_string = []
result = 0
for i in s:
    if i.isalpha():
        new_string.append(i)
    else:
        result += int(i)

print(str(''.join(sorted(new_string))) + str(result))

# K1KA5CB7 -> ABCKK13
# AJKDLSI412K4JSJ9D -> ADDIJJJKKLSS20