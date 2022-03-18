# 2022.03.19
# 제한 시간: 40분 / 풀이 시간 40분 00초
# 채점 결과: 오답 및 제한시간 내 미해결
# 시간복잡도: O(N^3)...?
# 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/60059

def rotate_key(key: list) -> list:
    key_size = len(key)
    rotated_key = [ 0 * key_size for _ in range(key_size) ]
    for i in range(key_size):
        for j in range(key_size):
            rotated_key[i][j] = key[key_size - j - 1][i]
    return rotated_key

def is_unlock(lock: list, rock_row: int) -> bool:
    large_lock_row = len(lock)
    for i in range(large_lock_row):
        for j in range(large_lock_row):
            pass
    return True

def solution(key: list, lock: list) -> bool:
    key_row_and_col = len(key)
    lock_row_and_col = len(lock)

    large_lock_row_and_col = (key_row_and_col - 1) * 2 + lock_row_and_col
    large_lock = [ [0] * large_lock_row_and_col for i in range(large_lock_row_and_col) ]
    
    for i in range(large_lock_row_and_col):
        for j in range(large_lock_row_and_col):
            if (key_row_and_col - 1) <= i < (2 * key_row_and_col - 1) and (key_row_and_col - 1) <= j < (2 * key_row_and_col - 1):
                large_lock[i][j] = lock[i - (key_row_and_col - 1)][j - (key_row_and_col - 1)]
    print(large_lock)
    for i in range(key_row_and_col + lock_row_and_col - 1):
        for j in range(key_row_and_col + lock_row_and_col - 1):
            for k in range(4):
                rotated_key = rotate_key(key)



    return True

print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]])) # true