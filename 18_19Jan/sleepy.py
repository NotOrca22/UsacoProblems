with open("sleepy.in", "r") as f1:
    numOfCows = int(f1.readline().strip())
    cows = f1.readline().strip().split(" ")
    cows = [int(cow) for cow in cows]

    cows = list(reversed(cows))
    # print(cows)
    cowsToMove = 0
    for i in range(numOfCows-1):
        if cows[i] < cows[i+1]:
            # print(i)
            cowsToMove = numOfCows - i - 1
            break
    with open("sleepy.out", "w") as f2:
        f2.write(str(cowsToMove) + "\n")