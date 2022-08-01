word = input()
ans = ''
for i in word:
    if i.isupper():
        ans += i
print(ans)