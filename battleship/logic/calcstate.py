from collections import deque


def calc_state(tableShots, tableShips):
    w, h = len(tableShips[0]), len(tableShips)
    showTable = [[0] * w for i in range(h)]

    shots = 0
    injury = 0
    for i in range(len(tableShots)):
        for j in range(len(tableShots[i])):
            if tableShots[i][j]:
                if tableShips[i][j] == '.':
                    shots += 1
                    showTable[i][j] = 1
                else:
                    injury += 1
                    showTable[i][j] = 2

    kills = 0
    used = [[False] * w for i in range(h)]

    steps = [
        [1, 0],
        [0, 1],
        [-1, 0],
        [0, -1]
    ]

    for i in range(h):
        for j in range(w):
            if not used[i][j] and tableShips[i][j] == '#':
                q = deque()
                q.append((i, j))
                used[i][j] = True

                path = []

                sizeShip = 0
                shotShip = 0
                while len(q) > 0:
                    x, y = q.popleft()
                    path.append((x, y))

                    if tableShips[x][y] == '#':
                        sizeShip += 1

                    if tableShips[x][y] == '#' and tableShots[x][y]:
                        shotShip += 1

                    for dx, dy in steps:
                        xNew = x + dx
                        yNew = y + dy

                        if (xNew >= 0 and yNew >= 0 and xNew < h and yNew < w
                                and tableShips[xNew][yNew] == '#' and not used[xNew][yNew]):
                            q.append((xNew, yNew))
                            used[xNew][yNew] = True

                # print(sizeShip, shotShip)
                if sizeShip == shotShip:
                    kills += 1
                    for x, y in path:
                        showTable[x][y] = 3

    return shots, injury, kills, showTable

