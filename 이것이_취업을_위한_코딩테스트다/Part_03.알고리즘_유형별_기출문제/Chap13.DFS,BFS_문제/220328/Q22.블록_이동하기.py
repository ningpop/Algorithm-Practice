# 2022.04.06
# 제한 시간 50분 / 풀이 시간 50분 00초
# 채점 결과: 오답 및 제한시간 내 미해결
# 시간복잡도: 
# 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/60063

def check_move(board: list, state: str, x1: int, y1: int, x2: int, y2: int, direction: str) -> bool:
    if state == 'v':
        if direction == 'r':
            if board[x1][y1 + 1] != 1 and board[x2][y2 + 1] != 1:
                return True
            return False
        elif direction == 'd':
            if board[x2 + 1][y2] != 1:
                return True
            return False
        elif direction == 'l':
            if board[x1][y1 - 1] != 1 and board[x2][y2 - 1] != 1:
                return True
            return False
        elif direction == 'u':
            if board[x1 - 1][y1] != 1:
                return True
            return False
    elif state == 'h':
        if direction == 'r':
            if board[x2][y2 + 1] != 1:
                return True
            return False
        elif direction == 'd':
            if board[x1 + 1][y1] != 1 and board[x2 + 1][y2] != 1:
                return True
            return False
        elif direction == 'l':
            if board[x1][y1 - 1] != 1:
                return True
            return False
        elif direction == 'u':
            if board[x1 - 1][y1] != 1 and board[x2 - 1][y2] != 1:
                return True
            return False
    return False

def check_turn(board: list, state: int, x1: int, y1: int, x2: int, y2: int, direction: int) -> bool:
    if state == 0: # 로봇이 가로 상태
        if direction == 0: # 시계 방향으로 회전
            if board[x1 - 1][y1] != 1 and board[x2 - 1][y2] != 1:
                return True
            return False
        else: # 반시계 방향으로 회전
            if board[x1 - 1][y1] != 1 and board[x2 - 1][y2] != 1:
                return True
            return False
    else: # 로봇이 세로 상태
        if direction == 0: # 시계 방향으로 회전
            pass
        else: # 반시계 방향으로 회전
            pass

def solution(board: list) -> int:
    answer = 0
    return answer

print(solution([
    [0, 0, 0, 1, 1],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 1, 1],
    [1, 1, 0, 0, 1],
    [0, 0, 0, 0, 0]
    ])) # 7