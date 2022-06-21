with open("traffic.in", "r") as f1:
    numOfMiles = int(f1.readline().strip())
    low = -9999999
    high = 9999999
    infoList = []
    for i in range(numOfMiles-1, -1, -1):
        info = f1.readline().strip().split(" ")
        infoList.append([info[0]] + [int(x) for x in info[1:]])


    for info in reversed(infoList):
        if info[0] == "on":
            low -= info[2]
            high -= info[1]
        elif info[0] == "off":
            low += info[1]
            high += info[2]
        else:
            low = max(low, info[1], 0)
            high = min(high, info[2])
        low = max(0, low)
        high = max(0, high)
        if low > high:
            temp1 = low
            low = high
            high = temp1
    low1 = low
    high1 = high
    for info in infoList:
        if info[0] == "on":
            low += info[1]
            high += info[2]
        elif info[0] == "off":
            low -= info[2]
            high -= info[1]
        else:
            low = max(low, info[1])
            high = min(high, info[2])
        low = max(0, low)
        # if low > high:
        #     print(low, high)
        #     temp1 = low
        #     low = high
        #     high = temp1
    print(low, high)

    # print(low, high)
    with open("traffic.out", "w") as f2:
        f2.write(str(low1) + " " + str(high1) + "\n" + str(low) + " " + str(high))