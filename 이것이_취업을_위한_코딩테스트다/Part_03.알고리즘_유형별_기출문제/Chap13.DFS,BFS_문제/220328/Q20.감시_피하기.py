# 2022.04.03
# 제한 시간 60분 / 풀이 시간 60분 60초
# 채점 결과: 오답, 제한시간 내 미해결
# 시간복잡도: 
# 문제 링크: https://www.acmicpc.net/problem/18428

from itertools import combinations

def dfs(school: list, tx: int, ty: int, d: int) -> bool:
    if tx <= 0 or tx > n or ty <= 0 or ty > n:
        return True

    if school[tx][ty] == 'O':
        return True
    elif school[tx][ty] == 'S':
        return False
    
    if d == 0:
        return dfs(school, tx, ty + 1, 0)
    elif d == 1:
        return dfs(school, tx + 1, ty, 1)
    elif d == 2:
        return dfs(school, tx, ty - 1, 2)
    elif d == 3:
        return dfs(school, tx - 1, ty, 3)

n = int(input())
school = [ ['-'] * (n + 1) ]
area_list = []
teacher_list = []
for i in range(n):
    row = ['-'] + list(input().split())
    for j in range(len(row)):
        if row[j] == 'X':
            area_list.append((i + 1, j))
        elif row[j] == 'T':
            teacher_list.append((i + 1, j))
    school.append(row)

area_cases = list(combinations(area_list, 3))
is_answer = False
for case in area_cases:
    for x, y in case:
        school[x][y] = 'O'
    
    for tx, ty in teacher_list:
        is_answer = dfs(school, tx, ty, 0) or dfs(school, tx, ty, 1) or dfs(school, tx, ty, 2) or dfs(school, tx, ty, 3) or is_answer
        
    if is_answer:
        break
    
    for x, y in case:
        school[x][y] = 'X'

if is_answer:
    print("YES")
else:
    print("NO")