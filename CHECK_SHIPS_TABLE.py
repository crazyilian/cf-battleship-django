from collections import deque


def checkTable(s, H, W, goodSizeShip):
    if s.count('.') + s.count('#') + s.count('\n') != len(s):
        return "Таблица состоит не только из . и #"
    table = s.split('\n')
    w, h = len(table[0]), len(table)

    for i in table:
        if w == len(i):
            continue
        return "Таблица не прямоугольная"

    if h != H or w != W:
        return f"Таблица размера ({h}, {w})"

    cnt = {}

    used = [[False] * w for i in range(h)]

    steps = [
        [1, 0],
        [0, 1],
        [-1, 0],
        [0, -1]
    ]

    for i in range(h - 1):
        for j in range(w):
            if j + 1 < w and table[i][j] == '#' and table[i + 1][j + 1] == '#':
                return "Найдены две клетки корабля по диагонали"
            if j - 1 >= 0 and table[i][j] == '#' and table[i + 1][j - 1] == '#':
                return "Найдены две клетки корабля по диагонали"

    for i in range(h):
        for j in range(w):
            if not used[i][j] and table[i][j] == '#':
                q = deque()
                q.append((i, j))
                used[i][j] = True
                tmp = 0
                while len(q) > 0:
                    x, y = q.popleft()

                    if table[i][j] == '#':
                        tmp += 1

                    for dx, dy in steps:
                        xNew = x + dx
                        yNew = y + dy

                        if (xNew >= 0 and yNew >= 0 and xNew < h and yNew < w
                                and table[xNew][yNew] == '#' and not used[xNew][yNew]):
                            q.append((xNew, yNew))
                            used[xNew][yNew] = True
                cnt[tmp] = cnt.get(tmp, 0) + 1
    tmp = []
    for k, v in cnt.items():
        tmp.append([k, v])

    tmp = sorted(tmp)

    if tmp != goodSizeShip:
        print(tmp)
        print(goodSizeShip)
        return "Размеры кораблей или их количество не соответствуют правилам"

    return True


with open('sample-table.txt') as f:
    s = f.read().strip()

res = checkTable(s, 8, 10, [  # [размер, количество],
    [1, 2],
    [2, 2],
    [3, 2],
    [4, 1]
])

if res != True:
    print('Ошибка!\n')
    print(res)
else:
    print('Корректно')
