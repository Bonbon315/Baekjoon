import sys
input = sys.stdin.readline

triangle = list(int(input()) for _ in range(3))

if sum(triangle) == 180:
    if triangle[0] == triangle[1] == triangle[2]:
        print('Equilateral')
    elif len(set(triangle)) == 2:
        print('Isosceles')
    else:
        print('Scalene')
else:
    print('Error')