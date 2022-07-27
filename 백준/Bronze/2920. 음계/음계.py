thing = list(map(int, input().split()))
ascthing = sorted(thing)
desthing = sorted(thing, reverse=True)

if ascthing == thing:
    print('ascending')
elif desthing == thing:
    print('descending')
else:
    print('mixed')