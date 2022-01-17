from random import choice


def generation_map():
    list_map = [[['#'], ['.'], ['#'], ['#'], ['#'], ['#'], ['#'], ['#'], ['#'], ['#'], ['#'], ['#'],
                ['#'], ['#'], ['#']]]
    for i in range(7):
        list_map.append([['#'], ['*'], ['#'], ['*'], ['#'], ['*'], ['#'], ['*'], ['#'], ['*'], ['#'],
                         ['*'], ['#'], ['*'], ['#']])
        list_map.append([['#'], ['#'], ['#'], ['#'], ['#'], ['#'], ['#'], ['#'], ['#'], ['#'], ['#'], ['#'],
                         ['#'], ['#'], ['#']])
    list_map[1][1] = ['.']
    list_map[13][13] = ['@']
    list_map[13][12] = ['.']
    list_map[12][13] = ['.']
    x = 1
    y = 1
    running = True
    list_coords = [(y, x)]
    while running:
        list_point = []
        if 0 < x - 2 < 14 and 0 < y < 14:
            if list_map[y][x - 2] == ['*']:
                list_point.append((y, x - 2))
        if 0 < x + 2 < 14 and 0 < y < 14:
            if list_map[y][x + 2] == ['*']:
                list_point.append((y, x + 2))
        if 0 < x < 14 and 0 < y - 2 < 14:
            if list_map[y - 2][x] == ['*']:
                list_point.append((y - 2, x))
        if 0 < x < 14 and 0 < y + 2 < 14:
            if list_map[y + 2][x] == ['*']:
                list_point.append((y + 2, x))
        if list_point == []:
            c = 0
            for elem in list_coords:
                c += 1
                if 0 < elem[1] - 2 < 14 and 0 < elem[0] < 14:
                    if list_map[elem[0]][elem[1] - 2] == ['*']:
                        list_point.append((elem[0], elem[1] - 2))
                if 0 < elem[1] + 2 < 14 and 0 < elem[0] < 14:
                    if list_map[elem[0]][elem[1] + 2] == ['*']:
                        list_point.append((elem[0], elem[1] + 2))
                if 0 < elem[1] < 14 and 0 < elem[0] - 2 < 14:
                    if list_map[elem[0] - 2][elem[1]] == ['*']:
                        list_point.append((elem[0] - 2, elem[1]))
                if 0 < elem[1] < 14 and 0 < elem[0] + 2 < 14:
                    if list_map[elem[0] + 2][elem[1]] == ['*']:
                        list_point.append((elem[0] + 2, elem[1]))
                if list_point != []:
                    x = elem[1]
                    y = elem[0]
                    break
            if c == len(list_coords):
                running = False
        else:
            point = choice(list_point)
            list_map[point[0]][point[1]] = ['.']
            a = (point[0] - y) // 2
            b = (point[1] - x) // 2
            list_map[a + y][b + x] = ['.']
            x, y = point[1], point[0]
            list_coords.append((y, x))
    for i in range(15):
        for j in range(15):
            list_map[i][j] = ''.join(list_map[i][j])
        list_map[i] = ''.join(list_map[i])
    map = open('data/map.txt', mode='w')
    for elem in list_map:
        map.write(f'{str(elem)}\n')
    map.close()
