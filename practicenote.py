import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

omok = [list(map(int, input().split())) for _ in range(19)]

dx = [0, 1, 1, -1]
dy = [1, 0, 1, 1]

for x in range(19):
    for y in range(19):
        if omok[x][y] != 0:

            for i in range(4):
                cnt = 1
                nx = x + dx[i]
                ny = y + dy[i]

                while 0 <= nx < 19 and 0 <= ny < 19 and omok[nx][ny] == omok[x][y]:
                    cnt += 1

                    if cnt == 5:
                        if 0 <= x - dx[i] < 19 and 0 <= y - dy[i] < 19 and omok[x - dx[i]][y - dy[i]] == omok[x][y]:
                            break
                        if 0 <= nx + dx[i] < 19 and 0 <= ny + dy[i] < 19 and omok[nx + dx[i]][ny + dy[i]] == omok[x][y]:
                            break
                        
                        print(omok[x][y])
                        print(x + 1, y + 1)
                        exit()

                    nx += dx[i]
                    ny += dy[i]

print(0)