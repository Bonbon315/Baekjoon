import sys
sys.stdin = open('input.txt', 'r', encoding='utf-8')
input = sys.stdin.readline

books = dict()

n = int(input())
for i in range(n):
    book = input().rstrip()
    if book not in books:
        books[book] = 1
    else:
        books[book] += 1

books = dict(sorted(books.items()))
print(max(books))