with open("revegetate.in", "r") as f1:
    info = f1.readline().strip().split(" ")
    info = [int(x) for x in info]
    connections = {}
    grassNumbers = {}
    for i in range(0, info[0]+1):
        connections[i] = []
        grassNumbers[i] = 0
    for j in range(info[1]):
        data = f1.readline().strip().split(" ")
        data = [int(y) for y in data]
        connections[data[0]].append(data[1])
        connections[data[1]].append(data[0])
    for i in range(1,info[0]+1):
        minGrassNum = 0
        for j in range(i):
            if i in connections[j]:
                if grassNumbers[j] > minGrassNum:
                    minGrassNum = grassNumbers[j]
        grassNumbers[i] = minGrassNum + 1
    print(grassNumbers)
    with open("revegetate.out", "w") as f2:
        l = list(grassNumbers.values())
        l = [str(z) for z in l]
        f2.write("".join(l[1:]) + "\n")