def oneDigit(num):
    return ((num >= 0) and
            (num < 10))
def isPalUtil(num, dupNum):
    if oneDigit(num):
        return (num == (dupNum[0]) % 10)
    if not isPalUtil(num // 10, dupNum):
        return False
    dupNum[0] = dupNum[0] // 10
    return (num % 10 == (dupNum[0]) % 10)
def isPal(num):
    if (num < 0):
        num = (-num)
    dupNum = [num]
    return isPalUtil(num, dupNum)
n = 12321
if isPal(n):
    print("Yes")
else:
    print("No")