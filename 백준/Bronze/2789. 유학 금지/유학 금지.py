word = input()
ban = 'CAMBRIDGE'

answer = word
for i in word:
    if i in ban:
        answer = answer.replace(i, '')
print(answer)