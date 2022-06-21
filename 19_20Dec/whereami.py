print(len(list(set(['BLORRRSW', 'BFLORRSW', 'FLORRSSW', 'FORRSSWW', 'FORRSSWW', 'FORRSSWW', 'FORRSSWW', 'FORRSSWW', 'FORRSSWW', 'FORRSSWW', 'FORRSSWW', 'AFORRSSW', 'ADFORSSW']))))
def getOccurences(arr, elem):
    ans = 0
    for item in arr:
        if item == elem:
            ans += 1
    return ans
with open("whereami.in", "r") as f1:
    l = int(f1.readline().strip())
    s = f1.readline().strip()
    listOfSubs = []
    ans = 0
    for i in range(1, l+1):
        subStrings = []
        for j in range(l+1-i):
            subStrings.append("".join(sorted(s[j:i+j])))
        print(subStrings)
        listOfSubs.append(subStrings)
    # print(len(list(set(listOfSubs[3]))))
    for x in range(len(listOfSubs)):
        print(listOfSubs[x])
        good = True
        for t in set(listOfSubs[x]):
            print(t)
            if getOccurences(listOfSubs[x], t) >= 2:
                good = False
                break
        if good:
            ans = x+1
            break
        # subStrings.append
    with open("whereami.out", "w") as f2:
        f2.write(str(ans))