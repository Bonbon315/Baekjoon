import sys
input = sys.stdin.readline

n = int(input())
persons = {}

for i in range(n):
    person, here = input().split()

    if here == 'enter':
        persons[person] = 1
    elif here == 'leave':
        persons[person] -= 1

persons2 = dict(sorted(persons.items(), reverse=True))

for k, v in persons2.items():
    if v > 0:
        print(k)