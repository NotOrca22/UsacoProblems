if __name__ == "__main__":
    with open("gymnastics.in", "r") as f1:
        a,b = f1.readline().strip().split(" ")
        a,b = int(a), int(b)
        l = []
        stuff = []
        pairs = 0
        for i in range(a):
            x = f1.readline().strip().split(" ")
            x = [int(z) for z in x]
            l.append(x)
        print(l)
        for i in range(1, b+1):
            for j in range(i+1, b+1):
                betterI = 0
                for competition in l:
                    if competition.index(i) < competition.index(j):
                        betterI += 1
                if betterI == 0 or betterI == a:
                    pairs += 1

        # ct = 0
        # for i in range(b):
        #     for j in range(i+1, b):
        #         ct += 1
        #         allBigger = True
        #         allSmaller = True
        #         for k in range(a):
        #             print(k)
        #             print(stuff[i][k], stuff[j][k])
        #             if stuff[i][k] > stuff[j][k]:
        #                 allSmaller = False
        #             if stuff[i][k] < stuff[j][k]:
        #                 allBigger = False
        #         print(allBigger, allSmaller)
        #         if allBigger or allSmaller:
        #             pairs += 1
        # print(ct)
        with open("gymnastics.out", "w") as f2:
            f2.write(str(int(pairs)))