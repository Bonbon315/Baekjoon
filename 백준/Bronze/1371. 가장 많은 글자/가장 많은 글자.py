import sys
input = sys.stdin.read

sent = input().replace('\n', '').replace(' ', '')
a = [0] * 26

for i in sent:
    a[ord(i)-97] += 1

for j in range(26):
    if a[j] == max(a):
        print(chr(j+97), end='')