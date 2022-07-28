from collections import Counter

N = int(input())
cards = list(map(int, input().split()))
M = int(input())
numbers = map(int, input().split())

cnt = Counter(cards)
for i in numbers:
    if i in cnt:
        print(cnt[i], end=' ')
    else:
        print('0', end=' ')