# 2022.03.27
# 제한 시간 30분 / 풀이 시간 32분 06초
# 채점 결과: 정답 및 시간초과
# 시간복잡도: O(N^2)
# 문제 링크: 

def dfs(x: int, y: int):
    ice_board[x][y] = 1
    if 0 <= (x - 1) < n and 0 <= y < m:
        if ice_board[x - 1][y] == 0:
            dfs(x - 1, y)
    if 0 <= x < n and 0 <= (y + 1) < m:
        if ice_board[x][y + 1] == 0:
            dfs(x, y + 1)
    if 0 <= (x + 1) < n and 0 <= y < m:
        if ice_board[x + 1][y] == 0:
            dfs(x + 1, y)
    if 0 <= x < n and 0 <= (y - 1) < m:
        if ice_board[x][y - 1] == 0:
            dfs(x, y - 1)

n, m = map(int, input().split())
ice_board = []
for _ in range(n):
    row = input()
    row_to_int = [ int(i) for i in row ]
    ice_board.append(row_to_int)

result = 0
for i in range(n):
    for j in range(m):
        if ice_board[i][j] == 0:
            dfs(i, j)
            result += 1

print(result)

# input 1
'''
4 5
00110
00011
11111
00000
'''
# output 1
'''
3
'''

# input 2
'''
15 14
00000111100000
11111101111110
11011101101110
11011101100000
11011111111111
11011111111100
11000000011111
01111111111111
00000000011111
01111111111000
00011111111000
00000001111000
11111111110011
11100011111111
11100011111111
'''
# output 2
'''
8
'''