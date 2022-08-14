def possible(maxWait):
    # maxWait = 4
    # maxWait = 6
    firstIndex = 0
    cnt = 0
    cars = 0
    for j in range(n):
        # if maxWait == 6:
        #     print(cows[i])
        # cnt += 1
        if int(cows[j]) - int(cows[firstIndex]) > maxWait or j + 1 - firstIndex > c:
            cars += 1
            # print(cows[i])
            cnt = 1
            firstIndex = j
    if cnt > 0:
        cars += 1
    # print(cars)
    return cars <= m
# def
def findCorrect():
    print(possible(3))
    # return 3
    low = 0
    high = pow(10, 9)
    possibleValues = []
    while True:
        if low == high:
            # done = True
            if possible(low):
                possibleValues.append(low)
            else:
                possibleValues.append(low + 1)
            break
        # elif low + 1 == high:
        #
        #     # done = True
        #     if possible(low):
        #         possibleValues.append(low)
        #         break
        #     else:
        #         possibleValues.append(high)
        #         break
        mid = (low + high) // 2
        if possible(mid):
            high = mid - 1
            possibleValues.append(mid)
        else:
            low = mid + 1
            if low == 3:
                print(245432523)
                print(high)
    print(possibleValues)
    return min(possibleValues)
if __name__ == "__main__":
    with open("convention.in", "r") as f1:
        n, m, c = f1.readline().strip().split(" ")
        n,m,c = int(n), int(m), int(c)
        print(n,m,c)
        cows = f1.readline().strip().split(" ")
        cows = sorted([int(cow) for cow in cows])
        print(cows)
        if m * c == n:
            maxWait = 0
            for i in range(0, n, c):
                latestCow = i + c - 1
                earliestCow = i
                a = cows[latestCow] - cows[earliestCow]
                if a > maxWait:
                    maxWait = a
            print(maxWait)
            with open("convention.out", "w") as f2:
                f2.write(str(maxWait))

        else:
            x = findCorrect()
            with open("convention.out", "w") as f2:
                f2.write(str(x))

    # print(maxWait)
