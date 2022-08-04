import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())

for i in range(N):
    word = list(input().split()) #입력받은 문자열, 문장을 띄어 쓰기 기준으로 잘라 리스트 요소로 반환
    for j in word : #for 반복문을 통해 리스트를 순회하며, -1로 뒤집음. end처리로 띄어쓰기선언해 구분
        print(j[::-1], end=' ')