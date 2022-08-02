import sys
sys.stdin = open('input.txt', 'r', encoding='utf-8')
input = sys.stdin.readline

N = int(input())
cnt = 0
persons = set()
for i in range(N):
    s = input().rstrip()
    if s == 'ENTER':
        cnt += len(persons)
        persons = set()
    else:
        persons.add(s)
cnt += len(persons)
print(cnt)