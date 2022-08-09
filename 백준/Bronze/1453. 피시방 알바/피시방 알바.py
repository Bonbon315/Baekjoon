import sys
input = sys.stdin.readline

N = int(input())
guests = list(map(int, input().split()))
guests_here = set(guests)

print(len(guests) - len(guests_here))