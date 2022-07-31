texts = []
lengths = []

for i in range(5):
    t = input()
    texts.append(t)
    lengths.append(len(t))

for i in range(max(lengths)):
    for k in range(5):
        if i < lengths[k]:
            print(texts[k][i], end='')
