from random import choice


def generation_map():
    map = open('data/map.txt', mode='w')
    list_map = ['#'] * 13
    print(list_map)
    for i in range(13):
        for j in range(13):
            list_map[i] += choice(['#', '.'])
        list_map[i] += '#'
        list_map[i] = ''.join(list_map[i])
    list_map.insert(0, '#@#############')
    list_map.insert(14, '###############')
    for elem in list_map:
        map.write(f'{str(elem)}\n')
    map.close()
