def go_dawn():
    a, b = -10, -10
    with open('data/map.txt', 'r') as Map:
        inf = Map.readlines()
    n = len(inf)
    x, y = 0, 0
    for j in range(n):
        for i in range(n):
            if inf[j][i] == '@':
                x, y = i, j
                break
    if inf[y + 1][x] == '.':
        n_p = list(inf[y])
        k_p = list(inf[y + 1])
        n_p[x] = '.'
        k_p[x] = '@'
        inf[y] = ''. join(n_p)
        inf[y + 1] = ''.join(k_p)
        with open('data/map.txt', 'w') as Map:
            for elem in inf:
                Map.write(elem)
        return 'do', x, y
    return 'sleep', a, b


def go_up():
    a, b = -10, -10
    with open('data/map.txt', 'r') as Map:
        inf = Map.readlines()
    n = len(inf)
    x, y = 0, 0
    for j in range(n):
        for i in range(n):
            if inf[j][i] == '@':
                x, y = i, j
                break
    if inf[y - 1][x] == '.':
        n_p = list(inf[y])
        k_p = list(inf[y - 1])
        n_p[x] = '.'
        k_p[x] = '@'
        inf[y] = ''. join(n_p)
        inf[y - 1] = ''.join(k_p)
        with open('data/map.txt', 'w') as Map:
            for elem in inf:
                Map.write(elem)
        if y - 1 == 0 and x == 1:
            return 'win', x, y
        return 'do', x, y
    return 'sleep', a, b


def go_left():
    a, b = -10, -10
    with open('data/map.txt', 'r') as Map:
        inf = Map.readlines()
    n = len(inf)
    x, y = 0, 0
    for j in range(n):
        for i in range(n):
            if inf[j][i] == '@':
                x, y = i, j
                break
    if inf[y][x - 1] == '.':
        n_p = list(inf[y])
        n_p[x] = '.'
        n_p[x - 1] = '@'
        inf[y] = ''. join(n_p)
        with open('data/map.txt', 'w') as Map:
            for elem in inf:
                Map.write(elem)
        return 'do', x, y
    return 'sleep', a, b


def go_right():
    a, b = -10, -10
    with open('data/map.txt', 'r') as Map:
        inf = Map.readlines()
    n = len(inf)
    x, y = 0, 0
    for j in range(n):
        for i in range(n):
            if inf[j][i] == '@':
                x, y = i, j
                break
    if inf[y][x + 1] == '.':
        n_p = list(inf[y])
        n_p[x] = '.'
        n_p[x + 1] = '@'
        inf[y] = ''.join(n_p)
        with open('data/map.txt', 'w') as Map:
            for elem in inf:
                Map.write(elem)
        return 'do', x, y
    return 'sleep', a, b