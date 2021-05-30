# 2021.05.30
# 풀이시간 분 / 제한시간 20분
# 제한시간 초과 및 미해결
# https://www.acmicpc.net/problem/10825

n = int(input())

student = {}
for _ in range(n):
    name, kor, eng, math = input().split()
    student[name] = [int(kor), int(eng), int(math)]

student = sorted(student.items(), key=lambda x: (-x[1][0], x[1][1], -x[1][2], x[0]))
for value in student:
    print(value[0])