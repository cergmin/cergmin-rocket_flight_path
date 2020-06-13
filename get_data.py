with open('data.csv', 'r') as f:
    for s in f.read().splitlines():
        if s[0] == '#':
            continue
        print(s.split(',')[0], end=', ')
input()
