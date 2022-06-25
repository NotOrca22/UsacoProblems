import itertools
from itertools import permutations
with open("lineup.in", "r") as f1:
    i = int(f1.readline().strip())
    conditions = []
    for _ in range(i):
        conditions.append(f1.readline().strip().split(" "))
    cows = ['Bessie','Buttercup','Beatrice','Sue','Bella','Blue','Betsy','Belinda']
    perms = itertools.permutations(cows)
    workingPerms = []
    for perm in perms:
        print(perm)
        permWorks = True
        for condition in conditions:
            cowA = condition[0]
            cowB = condition[-1]
            if abs(perm.index(cowA) - perm.index(cowB)) != 1:
                permWorks = False
                break
        if permWorks:
            workingPerms.append(perm)
    with open("lineup.out", "w") as f2:
        f2.write("\n".join(sorted(workingPerms)[0]))