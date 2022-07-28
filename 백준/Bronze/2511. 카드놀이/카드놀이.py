A = list(map(int, input().split()))
B = list(map(int, input().split()))
Ascore = 0
Bscore = 0
score = []
for i in range(len(A)):
    if A[i] > B[i]:
        Ascore += 3
        score.append('A')
    elif B[i] > A[i]:
        Bscore += 3
        score.append('B')
    else:
        Ascore += 1
        Bscore += 1
        score.append('D')

print(Ascore, Bscore)
if Ascore > Bscore:
    print('A')
if Bscore > Ascore:
    print('B')
if Ascore == Bscore:
    for i in range(9, -1, -1):
        if score[i] != 'D':
            print(score[i])
            break
        if i == 0:
            print('D')
