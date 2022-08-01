import sys
input = sys.stdin.readline

N = int(input())
cards = dict()
for i in range(N):
    card = int(input())
    if card not in cards:
        cards[card] = 1
    else:
        cards[card] += 1

freq_card = max(cards.values())
max_cards = []
for k, v in cards.items():
    if v == freq_card:
        max_cards.append(k)
max_cards.sort()
print(max_cards[0])