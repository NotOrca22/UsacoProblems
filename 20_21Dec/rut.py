cows = []
eatenCells = []
for i in range(int(input())):
    x = input().split(" ")
    x[1] = int(x[1])
    x[2] = int(x[2])
    x.append(True)
    x.append(1)
    cows.append(x)
cows2 = cows.copy()
for i in range(100):
    eatenDuringIteration = []
    for cow in cows:
        if cow[3]:
            if cow[0] == "E":
                cow[1] += 1
                if [cow[1],cow[2]] in eatenCells:
                    cow[3] = False

                else:
                    cow[4] += 1
                    eatenDuringIteration.append([cow[1], cow[2]])
                    if cow[1] == 100:
                        cow[3] = False
            else:
                cow[2] += 1
                if [cow[1], cow[2]] in eatenCells:
                    cow[3] = False
                else:
                    cow[4] += 1
                    eatenDuringIteration.append([cow[1], cow[2]])
                    if cow[2] == 100:
                        cow[3] = False
    for cell in eatenDuringIteration:
        eatenCells.append(cell)
# print(cows)
for cow in cows:
    if cow[0] == "E":
        if cow[1] + cow[4] > 99:
            print("Infinity")
        else:
            print(cow[4])
    else:
        if cow[2] + cow[4] > 99:
            print("Infinity")
        else:
            print(cow[4])