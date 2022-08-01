import sys
input = sys.stdin.readline

books = dict()

n = int(input())
for i in range(n):
    book = input().rstrip()
    if book not in books:
        books[book] = 1
    else:
        books[book] += 1

maxsold = max(books.values())
bestseller = []
for k, v in books.items():
    if v == maxsold:
        bestseller.append(k)
bestseller.sort()
print(bestseller[0])