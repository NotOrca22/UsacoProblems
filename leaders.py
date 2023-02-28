numOfCows = int(input())
cowList = input()
listEnds = input().split()
listEnds = [int(end) for end in listEnds]
firstG = cowList.index("G") + 1
firstH = cowList.index("H") + 1
# print(firstG, firstH)
def listRightIndex(alist, value):
    return len(alist) - alist[-1::-1].index(value) -1
lastG = listRightIndex(cowList, "G") + 1
lastH = listRightIndex(cowList, "H") + 1
ans = 0
# First G is leader
if listEnds[firstG-1] >= lastG: # make sure earliest G can actually see all G's
    for i in range(firstG-1):
        if cowList[i] == "H" and listEnds[i] >= firstG and i+1 != firstH:
            ans += 1

if listEnds[firstH-1] >= lastH: # make sure earliest H can actually see all H's
    for i in range(firstH-1):
        if cowList[i] == "G" and listEnds[i] >= firstH and i+1 != firstG:
            ans += 1

if (listEnds[firstG-1] >= lastG and (listEnds[firstH-1] >= lastH or listEnds[firstH-1] >= firstG)) or (listEnds[firstH-1] >= lastH and (listEnds[firstG-1] >= lastG or listEnds[firstG-1] >= firstH)):
    ans += 1
print(ans)