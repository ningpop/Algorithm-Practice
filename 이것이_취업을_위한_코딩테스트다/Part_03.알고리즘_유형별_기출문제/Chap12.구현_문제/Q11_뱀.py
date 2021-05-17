N = int(input())

K =  int(input())
apple_place = []
for _ in range(K):
    apple_place.append(map(int, input().split()))

L = int(input())
snake_rotate = []
for _ in range(L):
    X, C = input().split()
    snake_rotate.append((X, C))

board = [ [0] * N for _ in range(N) ] # 빈 맵 만들기
# 맵에 사과 위치 표시
for i, j in apple_place:
    board[i-1][j-1] = 1

