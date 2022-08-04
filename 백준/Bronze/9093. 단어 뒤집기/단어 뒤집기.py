import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    sentence = list(input().split())
    ans = []
    for word in sentence:
        ans.append(word[::-1])
    print(*ans, sep=' ')