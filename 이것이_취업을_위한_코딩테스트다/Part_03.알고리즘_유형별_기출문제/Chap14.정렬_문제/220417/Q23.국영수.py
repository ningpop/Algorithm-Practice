# 2022.04.17
# 제한 시간 20분 / 풀이 시간 13분 52초
# 채점 결과: 정답
# 시간복잡도: O(NlogN)
# 문제 링크: https://www.acmicpc.net/problem/10825

n = int(input())

students = []
for _ in range(n):
    name, kor, eng, math = input().split()
    students.append((name, int(kor), int(eng), int(math)))

for i in sorted(students, key=lambda x : (-x[1], x[2], -x[3], x[0])):
    print(i[0])