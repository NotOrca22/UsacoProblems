if __name__ == "__main__":
    cowList = []
    buckets = []
    timesToCheck = []
    with open("blist.in", "r") as f1:
        numOfCows = f1.readline()
        numOfCows = int(numOfCows.strip())
        for i in range(numOfCows):
            cowData = f1.readline()
            cowData = cowData.strip().split(" ")
            cowData = [int(value) for value in cowData]
            cowList.append(cowData)
            timesToCheck.append(cowData[0])
            timesToCheck.append(cowData[1])
    print(timesToCheck)
    for i in timesToCheck:
        bucketsNeeded = 0
        for cow in cowList:
            if cow[0] <= i <= cow[1]:
                bucketsNeeded += cow[2]
        buckets.append(bucketsNeeded)
    with open("blist.out", "w") as f2:
        f2.write(str(max(buckets)) + "\n")
