with open("socdist2.in", "r") as f1:
    x = int(f1.readline().strip())
    cowList = []

    for _ in range(x):
        a, b = f1.readline().strip().split(" ")
        cowList.append([int(a), int(b)])
    cowList = (sorted(cowList, key=lambda x:x[0]))
    infectedCowList = []
    for cow in cowList:
        if cow[1] == 1:
            infectedCowList.append(cow[0])
    print(cowList)
    print(infectedCowList)
    maxR = 9999999
    for i in range(x-1):
        for j in range(i+1, x):
            cow1 = cowList[i]
            cow2 = cowList[j]
            if cow1[1] != cow2[1]:
                maxR = min(maxR, abs(cow2[0] - cow1[0])-1)
    print(maxR)
    blocks = []
    currentBlock = []
    for cow in infectedCowList:
        if len(currentBlock) == 0:
            currentBlock.append(cow)
        else:
            if currentBlock[-1] + maxR >= cow:
                currentBlock.append(cow)
            else:
                blocks.append(currentBlock)
                currentBlock = [cow]
    if len(currentBlock) > 0:
        blocks.append(currentBlock)
    with open("socdist2.out", 'w') as f2:
        f2.write(str(len(blocks)))