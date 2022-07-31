def swap():
    with open("swap.in", "r") as f1:
        n, k = f1.readline().strip().split(" ")
        n, k = int(n), int(k)
        cows = []
        for cow in range(1, n + 1):
            cows.append(str(cow))
        config = cows
        a1, a2 = f1.readline().strip().split(" ")
        b1, b2 = f1.readline().strip().split(" ")
        a1, a2, b1, b2 = int(a1), int(a2), int(b1), int(b2)
        cycleLen = 0
        for i in range(k):
            cows = cows[:a1-1] + list(reversed(cows[a1-1:a2])) + cows[a2:]
            cows = cows[:b1 - 1] + list(reversed(cows[b1 - 1:b2])) + cows[b2:]
            cycleLen += 1
            if cows == config:
                break

        print(cycleLen)
        for _ in range(k%cycleLen):
            cows = cows[:a1 - 1] + list(reversed(cows[a1 - 1:a2])) + cows[a2:]
            cows = cows[:b1 - 1] + list(reversed(cows[b1 - 1:b2])) + cows[b2:]
        with open("swap.out", "w") as f2:
            for cow in cows:
                f2.write(cow + "\n")
            # print(c[(k+1)%len(c)])

                    # cycle.append(a2 - distanceFromA1)


        # print(len(configs))
        # output = configs[(k-1) % len(configs)]
        # with open("swap.out", "w") as f2:
        #     # cows2 = []
        #     # for cow in cows:
        #     #     cows2.append(str(cow))
        #     f2.write("\n".join(output))
if __name__ == "__main__":
    swap()
