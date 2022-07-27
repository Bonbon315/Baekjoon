taebo = input()

leftcnt = 0
for i in taebo:
    if i == '@':
        leftcnt += 1
    if i == '(':
        break
rightcnt = taebo.count('@') - leftcnt

print(leftcnt, rightcnt)