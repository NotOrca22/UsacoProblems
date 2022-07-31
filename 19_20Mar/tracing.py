with open("tracing.in", "r") as f1:
    a = f1.readline().strip()
    n, t = a.split(" ")
    n, t = int(n), int(t)
    cowStates = f1.readline().strip()
    contacts = []
    for _ in range(t):
        contact = f1.readline().strip().split(" ")
        contact = [int(cont) for cont in contact]
        contacts.append(contact)
    contacts = (sorted(contacts, key=lambda x:x[0]))
    cowStates = list(cowStates)
    print(cowStates)
    realCowStates = [0] # 0 for indexing purposes
    for state in cowStates:
        realCowStates.append(int(state))
    print(realCowStates)
    infectedIndices = []
    for i in range(1, n+1):
        if realCowStates[i] == 1:
            infectedIndices.append(i)
    print(infectedIndices)
    possibleZero = []
    possibleK = []
    for i in range(1, n + 1):
        if realCowStates[i] == 1: # infected (un-infected cows can't be patient 0)
            for pK in range(t+1): # all values of k
                if realCowStates.count(1) == 1 and pK == 0:
                    possibleZero.append(i)
                    possibleK.append(0)
                else:
                    cowShakes = dict()
                    for cow in range(1, n+1):
                        if cow != i:
                            cowShakes[cow] = [0, False]
                        else:
                            cowShakes[cow] = [0, True]
                    for cont in contacts:
                        cow1, cow2 = cont[1], cont[2]
                        # if cow1 == 1 and cow2 == 2:

                        # cow1, cow2 = 1, 2
                        if cowShakes[cow1][1] and cowShakes[cow1][0] < pK or (cowShakes[cow2][1] and cowShakes[cow2][0] < pK):
                            a = cowShakes[cow1][0]
                            # print(a)
                            b = cowShakes[cow2][0]
                            # print(b)
                            if cowShakes[cow1][1]:
                                cowShakes[cow1] = [a+1, True]
                            else:
                                cowShakes[cow1] = [a, True]
                            if cowShakes[cow2][1]:
                                cowShakes[cow2] = [b+1, True]
                            else:
                                cowShakes[cow2] = [b, True]
                    infectedCows = []
                    for j in range(1, n+1):
                        if cowShakes[j][1]:
                            infectedCows.append(j)
                    if infectedCows == infectedIndices:
                        possibleZero.append(i)
                        if pK == t:
                            possibleK.append(69420)
                        else:
                            possibleK.append(pK)
                    print(infectedCows)
    print(possibleK)
    print(possibleZero)
    if len(possibleK) > 0:
        minK = min(possibleK)
        if max(possibleK) == 69420:
            maxK = "Infinity"
        else:
            maxK = max(possibleK)
    else:
        minK, maxK = 1, 1
    output = str(len(list(set(possibleZero)))) + " " + str(minK) + " " + str(maxK)
    with open("tracing.out", "w") as f2:
        f2.write(output)