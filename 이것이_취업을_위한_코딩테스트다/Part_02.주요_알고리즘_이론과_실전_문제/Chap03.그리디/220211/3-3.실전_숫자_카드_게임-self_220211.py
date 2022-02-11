# 2022.02.11
# 제한 시간 30분 / 풀이 시간 12분 26초
# 채점 결과: 정답
# 시간복잡도: N^2 + N = O(N^2)

N, M = map(int, input().split())

card_board = []
for i in range(N):
    num_of_row = list(map(int, input().split()))
    card_board.append(num_of_row)

max_num = 0
for i in range(N):
    min_num_of_row = card_board[i][0]
    for j in range(M):
        min_num_of_row = min(min_num_of_row, card_board[i][j])
    max_num = min_num_of_row

print(max_num)