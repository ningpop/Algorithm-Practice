# https://programmers.co.kr/learn/courses/30/lessons/60059
# 2021.05.15
# 제한시간 40분
# 시간초과 및 미해결

def rotate_key(key: list) -> list:
    pass

def check_lock(key: list, field: list) -> bool:
    for i in range(len(field)-len(key)+1):
        for j in range(len(field)-len(key)+1):
            for k in range(len(key)):
                for l in range(len(key)):
                    field[i+k][j+l] += key[k][l]
            for k in range(field//3, len(field)):
                for l in range(field//3, len(field)):
                    if field[k][l] != 1:
                        return False



def solution(key: list, lock: list) -> bool:
    field = []
    for i in range(len(lock)*3):
        field.append([0 for z in range(len(lock)*3)])

    for i in range(len(lock)):
        for j in range(len(lock)):
            field[len(lock)+i][len(lock)+j] = lock[i][j]
    
    



print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))

