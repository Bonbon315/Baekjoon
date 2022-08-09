import sys
input = sys.stdin.readline

n = int(input())
result = [0, 0, 0, 0, 0]
for _ in range(n):
    x, y = map(int, input().split())
    if x == 0 or y == 0:
        result[0] += 1
    elif x > 0 and y > 0:
        result[1] += 1
    elif x < 0 and y > 0:
        result[2] += 1
    elif x < 0 and y < 0:
        result[3] += 1
    else:
        result[4] += 1

print(f'Q1: {result[1]}')
print(f'Q2: {result[2]}')
print(f'Q3: {result[3]}')
print(f'Q4: {result[4]}')
print(f'AXIS: {result[0]}')