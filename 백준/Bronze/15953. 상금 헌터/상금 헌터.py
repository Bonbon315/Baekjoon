import sys
input = sys.stdin.readline

def prize17(rank):
    if rank == 1:
        return 5000000
    elif 2 <= rank <= 3:
        return 3000000
    elif 4 <= rank <= 6:
        return 2000000
    elif 7 <= rank <= 10:
        return 500000
    elif 11 <= rank <= 15:
        return 300000
    elif 16 <= rank <= 21:
        return 100000
    else:
        return 0

def prize18(rank):
    if rank == 1:
        return 5120000
    elif 2 <= rank <= 3:
        return 2560000
    elif 4 <= rank <= 7:
        return 1280000
    elif 8 <= rank <= 15:
        return 640000
    elif 16 <= rank <= 31:
        return 320000
    else:
        return 0


T = int(input())
for i in range(T):
    a, b = map(int, input().split())
    print(prize17(a) + prize18(b))

