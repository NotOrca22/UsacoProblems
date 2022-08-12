# def possible(maxWait):
#     maxWait = 4
#     # maxWait = 6
#     firstIndex = 0
#     cnt = 0
#     cars = 0
#     for j in range(n):
#         # if maxWait == 6:
#         #     print(cows[i])
#         # cnt += 1
#         if int(cows[j]) - int(cows[firstIndex]) > maxWait or j + 1 - firstIndex > c:
#             cars += 1
#             # print(cows[i])
#             # cnt = 1
#             firstIndex = j
#     # if cnt > 1:
#     #     cars += 1
#     # print(cars)
#     return cars <= c
# def
# def findCorrect():
#     print(possible(0))
#     return 3
    # low = 0
    # high = pow(10, 9)
    # possibleValues = []
    # while True:
    #     if low == high:
    #         # done = True
    #         possibleValues.append(low)
    #         break
    #     elif low + 1 == high:
    #         # done = True
    #         if possible(low):
    #             possibleValues.append(low)
    #             break
    #         else:
    #             possibleValues.append(high)
    #             break
    #     mid = (low + high) // 2
    #     if possible(mid):
    #         high = mid - 1
    #         possibleValues.append(mid)
    #     else:
    #         low = mid + 1
    # return min(possibleValues)
def getLargestGap(arr, indicesToIgnore): # returns index of element before gap, arr MUST be sorted!!!
    largestIndex = None
    largestGap = 0
    for i in range(0, len(arr) - 1):
        if i not in indicesToIgnore:
            g = arr[i+1] - arr[i]
            if g > largestGap:
                largestGap = g
                largestIndex = i
    return largestIndex
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
        else:
            splitIndices = []
            brackets = [(0, n-1)]
            for i in range(c - 1):
                overFilledBrackets = []
                for bracket in brackets:
                    if bracket[1] - bracket[0] + 1 >
                indexToSplit = getLargestGap(cows, splitIndices)
                splitIndices.append(indexToSplit)
            print(splitIndices)
            # print(findCorrect())

    # print(maxWait)
