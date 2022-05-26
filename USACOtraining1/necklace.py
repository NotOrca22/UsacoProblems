"""
ID: orcawha1
LANG: PYTHON3
TASK: beads
"""
with open("beads.in", "r") as f1:
    necklaceLength = int(f1.readline().strip())
    necklace = f1.readline().strip()
    doubleNecklace = list(necklace * 2)
    maxBeads = 0
    for i in range(necklaceLength):
        subNecklaceLength = 1
        startingColor = doubleNecklace[i]
        subIndex = i+1
        if startingColor == "r":
            while True:
                if doubleNecklace[subIndex] == "b":
                    startingColor = "b"
                    while True:
                        if doubleNecklace[subIndex] == "r":
                            if subNecklaceLength > maxBeads:
                                maxBeads = subNecklaceLength
                                print(i)
                            break
                        elif subNecklaceLength > necklaceLength:
                            if subNecklaceLength > maxBeads:
                                maxBeads = subNecklaceLength
                                print(i)
                            break
                        subIndex += 1
                        subNecklaceLength += 1

                elif subNecklaceLength > necklaceLength:
                    if subNecklaceLength > maxBeads:
                        maxBeads = subNecklaceLength
                    break
                subIndex += 1
                subNecklaceLength += 1
        elif startingColor == "b":
            while True:
                if doubleNecklace[subIndex] == "r":
                    while True:
                        if doubleNecklace[subIndex] == "b":
                            if subNecklaceLength > maxBeads:
                                maxBeads = subNecklaceLength
                                print(i)
                            break
                        elif subNecklaceLength > necklaceLength:
                            if subNecklaceLength > maxBeads:
                                maxBeads = subNecklaceLength
                                print(i)
                            break
                        subIndex += 1
                        subNecklaceLength += 1
                        if subNecklaceLength > maxBeads:
                            maxBeads = subNecklaceLength
                            print(i)
                    break
                elif subNecklaceLength >= necklaceLength:
                    if subNecklaceLength > maxBeads:
                        maxBeads = subNecklaceLength
                    break
                subIndex += 1
                subNecklaceLength += 1
        else:
            subIndex += 1
            subNecklaceLength += 1
            startingColor = doubleNecklace[i+1]
            while True:
                if doubleNecklace[subIndex] != startingColor:
                    while True:
                        if doubleNecklace[subIndex] == startingColor:
                            if subNecklaceLength > maxBeads:
                                maxBeads = subNecklaceLength
                                print(i)
                            break
                        elif subNecklaceLength > necklaceLength:
                            if subNecklaceLength > maxBeads:
                                maxBeads = subNecklaceLength
                                print(i)
                            break
                        subIndex += 1
                        subNecklaceLength += 1
                    if subNecklaceLength > maxBeads:
                        maxBeads = subNecklaceLength
                    break
                elif subNecklaceLength > necklaceLength:
                    if subNecklaceLength > maxBeads:
                        maxBeads = subNecklaceLength
                    break
                subIndex += 1
                subNecklaceLength += 1

    with open("beads.out", "w") as f2:
        f2.write(str(maxBeads) + "\n")


