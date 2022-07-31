if __name__ == "__main__":
    cowphabet = list(input())
    string = list(input())
    # print(cowphabet)
    numString = [27]
    for char in string:
        numString.append(cowphabet.index(char))
    # print(numString)
    cnt = 0
    for i in range(len(numString)-1):
        if numString[i] >= numString[i+1]:
            cnt += 1
    print(cnt)