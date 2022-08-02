import sys
input = sys.stdin.readline

while True:
    sentence = input().rstrip()
    if sentence == '.':
        break

    stack = []
    ans = 'yes'
    for s in sentence:
        if s == '(' or s == '[':
            stack.append(s)
        elif s == ')':
            if len(stack) == 0 or stack[-1] == '[':
                ans = 'no'
                break
            elif stack[-1] == '(':
                stack.pop()
        elif s == ']':
            if len(stack) == 0 or stack[-1] == '(':
                ans = 'no'
                break
            elif stack[-1] == '[':
                stack.pop()
    if len(stack) != 0:
        ans = 'no'
    print(ans)