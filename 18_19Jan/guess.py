with open("guess.in", "r") as f1:
    numOfAnimals = int(f1.readline().strip())
    animalList = []
    traitSet = set()
    for i in range(numOfAnimals):
        info = f1.readline().strip().split(" ")
        name = info[0]
        traits = info[2:]
        for trait in traits:
            traitSet.add(trait)
        animalList.append(info)
    maxCommon = 0
    for i in range(numOfAnimals):
        for j in range(i+1, numOfAnimals):
            traits1 = set(animalList[i][2:])
            traits2 = set(animalList[j][2:])
            x = len(traits1.intersection(traits2))
            if x > maxCommon:
                maxCommon = x

        # if animalsWithTrait > maximum:
        #     maximum = animalsWithTrait
    # maxCommon = 0
    # uniqueCounter = {}
    # for animal in animalList:
    #     for animal2 in animalList:
    #         if animal != animal2:
    #             traits1 = animal[1:]
    #             traits2 = animal2[1:]
    #             commonTraits = 0
    #             for trait in traits1:
    #                 if trait in traits2:
    #                     commonTraits += 1
    #             if commonTraits > maxCommon:
    #                 maxCommon = commonTraits


    # for trait in traitSet:
    #     indicesWithTrait = []
    #     for i in range(numOfAnimals):
    #         if trait in animalList[i]:
    #             indicesWithTrait.append(i)
    #     if len(indicesWithTrait) == 1:
    #         try:
    #             uniqueCounter[indicesWithTrait[0]] += 1
    #         except:
    #             uniqueCounter[indicesWithTrait[0]] = 1
    with open("guess.out", "w") as f2:
        f2.write(str(maxCommon + 1) + "\n")