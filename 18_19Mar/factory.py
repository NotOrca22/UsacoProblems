with open("factory.in", "r") as f1:
    lines = []
    ct = int(f1.readline().strip())
    connections = {}
    while True:
        try:
            x, y = f1.readline().strip().split(" ")
            x, y = int(x), int(y)
            lines.append((x,y))
        except:
            break
    for i in range(1, ct+1):
        connections[i] = []
    for line in lines:
        print(line)
        connections[line[0]].append(line[1])
    print(lines)
    print(connections)
    done = False
    valids = []
    for i in range(1, ct+1):
        if connections[i] == []:
            with open("factory.out", "w") as f2:
                valids.append(i)
                # done = True
                # break
    # if not done:
    if len(valids) == 1:
        with open("factory.out", "w") as f2:
            f2.write(str(valids[0]) + "\n")
    else:
        with open("factory.out", "w") as f2:
            f2.write("-1\n")