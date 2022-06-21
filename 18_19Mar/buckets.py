with open("buckets.in", "r") as f1:
    # print(True and False and True)
    print(True or False and True)
    map = []
    for i in range(10):
        map.append(list(f1.readline().strip()))
    print(map)
    barnIndex = None
    lakeIndex = None
    rockIndex = None
    for row in range(10):
        for column in range(10):
            if map[row][column] == "B":
                barnIndex = (row, column)
            if map[row][column] == "R":
                rockIndex = (row, column)
            if map[row][column] == "L":
                lakeIndex = (row, column)
    print(barnIndex, lakeIndex, rockIndex)
    with open("buckets.out", "w") as f2:
        if ((lakeIndex[0] == rockIndex[0] == barnIndex[0])
                and (barnIndex[0] < rockIndex[0] < lakeIndex[0] or barnIndex[1] > rockIndex[1] > lakeIndex[1])
                or (lakeIndex[1] == barnIndex[1] == rockIndex[1])
                and (barnIndex[1] < rockIndex[1] < lakeIndex[1] or (barnIndex[0] > rockIndex[0] > lakeIndex[0]))):
            f2.write(str(abs(lakeIndex[0] - barnIndex[0]) + abs(lakeIndex[1] - barnIndex[1]) + 1))
        else:
            f2.write(str(abs(lakeIndex[0]-barnIndex[0]) + abs(lakeIndex[1]-barnIndex[1]) - 1))