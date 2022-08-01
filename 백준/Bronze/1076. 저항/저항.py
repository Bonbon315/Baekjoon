resist = {'black': 0, 'brown': 1, 'red': 2, 'orange': 3, 'yellow': 4, \
    'green': 5, 'blue': 6, 'violet': 7, 'grey': 8, 'white': 9}

n1 = resist[input()] * 10
n2 = resist[input()]
n3 = 10 ** resist[input()]

print((n1 + n2) * n3)