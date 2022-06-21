isWorking = True
with open("evolution.in", "r")  as f1:
    i = int(f1.readline().strip())
    cowTraits = dict()
    traits = set()
    for _ in range(i):
        info = f1.readline().strip().split(" ")
        cowTraits[_] = info[1:]
        for trait in info[1:]:
            traits.add(trait)
    print(traits)
    traits = list(traits)
    for a in range(len(traits)):
        for b in range(a, len(traits)):
            A = 0
            B = 0
            AB = 0
            traitA = traits[a]
            traitB = traits[b]
            for val in cowTraits.values():
                if traitA in val:
                    if traitB in val:
                        AB += 1
                    else:
                        A += 1
                elif traitB in val:
                    B += 1
            # if traitA == 'spots' and traitB == "flying":
            #     print(A, B, AB)
            if A > 0 and B > 0 and AB > 0:
                isWorking = False
    with open("evolution.out", "w") as f2:
        if isWorking:
            f2.write("yes")
        else:
            f2.write("no")