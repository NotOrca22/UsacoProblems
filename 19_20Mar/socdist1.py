import math

with open("socdist1.in", "r") as f1:
    x = int(f1.readline().strip())
    s = list(str(f1.readline()).strip())
    # print(s)
    gapSizes = []
    currentGap = 0
    for i in range(x):
        if s[i] == "0":
            currentGap += 1
        else:
            if currentGap != 0:
                gapSizes.append(currentGap)
            currentGap = 0
    if s[-1] == "0":
        gapSizes.append(currentGap)
    print(gapSizes)
    possibleNewStalls = []
    minGaps = []
    i = gapSizes.index(max(gapSizes))
    midCowGaps = gapSizes[:i]
    midCowGaps.append(math.floor((gapSizes[i]-1)/2))
    midCowGaps.append(math.ceil((gapSizes[i]-1)/2))
    midCowGaps += gapSizes[i+1:]
    print(midCowGaps)
    j = midCowGaps.index(max(midCowGaps))
    midCowGaps1 = midCowGaps[:j] + [int(math.floor(midCowGaps[j]-1/2)), int(math.ceil(midCowGaps[j]-1)/2)] + midCowGaps[j+1:]
    print(midCowGaps1)
    minGaps.append(max(midCowGaps1))
    if s.count("1") >= 2:
        if s[0] == "0":
            midCowGaps2 = [s.index("1")] + midCowGaps
            minGaps.append(max(midCowGaps2))
        if s[-1] == "0":
            midCowGaps2 = midCowGaps + [len(midCowGaps) - list(reversed(s)).index("1") - 1]
            print(midCowGaps2)
            minGaps.append(max(midCowGaps2))
        if s[0] == "0":
            leftCowGaps = [s.index("1")] + gapSizes
            leftCowGaps1 = leftCowGaps[:j] + [int(math.floor(leftCowGaps[j] - 1 / 2)),
                                            int(math.ceil(leftCowGaps[j] - 1) / 2)] + leftCowGaps[j + 1:]
            print(leftCowGaps1)
            minGaps.append(max(leftCowGaps1))
            if s[-1] == "0":
                leftCowGaps2 = leftCowGaps + [len(leftCowGaps) - list(reversed(s)).index("1") - 1]
                print(leftCowGaps2)
                minGaps.append(max(leftCowGaps2))
        if s[-1] == "0":
            rightCowGaps = [s.index("1")-1] + [len(gapSizes) - list(reversed(s)).index("1") - 1]
            rightCowGaps1 = rightCowGaps[:j] + [int(math.floor(rightCowGaps[j] - 1 / 2)),
                                            int(math.ceil(rightCowGaps[j] - 1) / 2)] + rightCowGaps[j + 1:]
            print(rightCowGaps1)
            minGaps.append(max(rightCowGaps1))
            if s[0] == "0":
                rightCowGaps2 = [s.index("1")-1] + rightCowGaps
                print(rightCowGaps2)
                minGaps.append(max(rightCowGaps2))
        with open("socdist1.out", "w") as f2:
            f2.write(str(min(minGaps)))
    elif s.count("1") == 0:
        with open("socdist1.out", "w") as f2:
            f2.write(str(x-1))
