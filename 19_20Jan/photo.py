def allPositive(arr):
    for item in arr:
        if item <= 0:
            return False
    return True
with open("photo.in", "r") as f1:
    numOfCows = int(f1.readline().strip())
    sums = f1.readline().strip().split(" ")
    sums = [int(x) for x in sums]
    workingPerms = []
    for i in range(1, numOfCows+1):
        currentPerm = [i]
        for s in sums:
            currentPerm.append(s - currentPerm[-1])
        if len(list(set(currentPerm))) == len(currentPerm) and allPositive(currentPerm):
            workingPerms.append(currentPerm)
        print(currentPerm)
    print(workingPerms)
    with open("photo.out", "w") as f2:
        l = workingPerms[0]
        l = [str(item) for item in l]
        f2.write(" ".join(l))