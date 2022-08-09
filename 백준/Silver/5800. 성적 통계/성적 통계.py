import sys
input = sys.stdin.readline

K = int(input())

for cls in range(1, K+1):
    grade = list(map(int, input().split()))
    num = grade.pop(0)
    grade.sort()
    dif = []
    for i in range(1, num):
        dif.append(grade[i] - grade[i-1])
    print(f'Class {cls}')
    print(f'Max {max(grade)}, Min {min(grade)}, Largest gap {max(dif)}')