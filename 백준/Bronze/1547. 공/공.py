import sys
input = sys.stdin.readline

ball = ['O', '.', '.']
M = int(input())
for _ in range(M):
    x, y = map(int, input().split())
    x , y = x-1, y-1
    temp = ball[x]
    ball[x] = ball[y]
    ball[y] = temp
print(ball.index('O')+1)