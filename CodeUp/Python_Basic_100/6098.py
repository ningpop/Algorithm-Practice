miro = [[0] * 10 for _ in range(10) ]
for i in range(10):
    mi = input().split()
    for j in range(10):
        miro[i][j] = int(mi[j])

# 개미 현재 위치 초기화
ant_x = 1
ant_y = 1

while True:
    if miro[ant_x][ant_y] == 0:
        miro[ant_x][ant_y] = 9 # 방문처리
    elif miro[ant_x][ant_y] == 2:
        miro[ant_x][ant_y] = 9 # 방문처리하고 break
        break

    if (miro[ant_x][ant_y + 1] == 1 and miro[ant_x + 1][ant_y] == 1) or (ant_x == 9 and ant_y == 9):
        break

    if miro[ant_x][ant_y + 1] != 1: # 우측이 벽이 아니면
        miro[ant_x][ant_y] = 9 # 방문처리
        ant_y += 1 # 우측으로 이동

    elif miro[ant_x + 1][ant_y] != 1: # 하단이 벽이 아니면
        miro[ant_x][ant_y] = 9 # 방문처리
        ant_x += 1 # 하단으로 이동

for i in miro:
    for j in i:
        print(j, end=' ')
    print()