# 2022.03.23
# 제한 시간: 40분 / 풀이 시간 68분 19초
# 채점 결과: 오답 및 제한시간 내 미해결
# 시간복잡도: O(N^2)
# 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/60061

def check_pillar(wall: list, x: int, y: int) -> bool:
    if y == 0 or wall[x - 1][y] == 1 or wall[x][y] == 1 or wall[x][y - 1] == 0:
        return True
    return False

def check_barrage(wall: list, x: int, y: int) -> bool:
    if (wall[x][y - 1] == 0) or (wall[x + 1][y - 1] == 0) or (wall[x - 1][y] == 1 and wall[x + 1][y] == 1):
        return True
    return False

def solution(n: int, build_frame: list) -> list:
    wall = [ [-1] * (n + 1) for _ in range(n + 1) ]
    answer = []
    for x, y, a, b in build_frame:
        if b == 0: # 삭제
            wall[x][y] = -1
            answer.remove([x, y, a])
            for nx, ny, t in answer:
                if t == 0: # 기둥
                    if not check_pillar(wall, nx, ny):
                        wall[x][y] = a
                        answer.append([x, y, a])
                        break
                else: # 보
                    if not check_barrage(wall, nx, ny):
                        wall[x][y] = a
                        answer.append([x, y, a])
                        break
        else: # 설치
            if a == 0: # 기둥
                if check_pillar(wall, x, y):
                    wall[x][y] = 0
                    answer.append([x, y, a])
            else: # 보
                if check_barrage(wall, x, y):
                    wall[x][y] = 1
                    answer.append([x, y, a])

    return sorted(answer)

print(solution(5, [
    [1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], 
    [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]
    ]))
print(solution(5, [
    [0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], 
    [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1], [2, 0, 0, 0], 
    [1, 1, 1, 0], [2, 2, 0, 1]
    ]))