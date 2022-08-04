import sys
from collections import Counter as c
input = sys.stdin.readline

numbers = []
for _ in range(10):
    numbers.append(int(input()))

print(sum(numbers)//len(numbers), c(numbers).most_common(1)[0][0])