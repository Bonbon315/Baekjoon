import sys
import heapq
input = sys.stdin.readline

N = int(input())
numbers = []
for i in range(N):
    number = int(input())
    if number != 0:
        heapq.heappush(numbers, number)
    else:
        if len(numbers) == 0:
            print(0)
        else:
            print(heapq.heappop(numbers))

