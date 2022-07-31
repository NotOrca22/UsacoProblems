def breedFlip():
    with open("breedflip.in", "r") as f1:
        x = int(f1.readline().strip())
        s1 = f1.readline().strip()
        s2 = f1.readline().strip()
        wrongPlacements = []
        currentIndex = -420
        for i in range(x):
            if s1[i] != s2[i]:
                wrongPlacements.append(i)
        usesNeeded = 0
        if len(wrongPlacements) == 0:
            return 0
        else:
            for i in range(1, len(wrongPlacements)):
                if wrongPlacements[i] - wrongPlacements[i-1] > 1:
                    usesNeeded += 1
        return usesNeeded+1
if __name__ == "__main__":
    x = breedFlip()
    with open("breedflip.out", "w") as f2:
        f2.write(str(x))
