import sys
input = sys.stdin.readline

T = int(input())
for i in range(T):
    N = int(input())
    numbers1 = set(map(int, input().split()))
    M = int(input())
    numbers2 = list(map(int, input().split()))

    for n in numbers2:
        if n in numbers1:
            print(1)
        else:
            print(0)