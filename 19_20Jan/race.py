import math


def race(l, k, x):
    if l == x:
        return x
    elif l < x:
        return l
    else:
        secondsElapsed = 0
        m = math.sqrt((pow(x,2)+2*k-x)/2)
        m2 = int(m)
        if m == int(m):
            return 2*m-x
        else:
            if m2 != x:
                secondsElapsed = 2*m2-x
                a = int(m2*(m2+1)/2)
                b = k-int((m2+x-1)*(m2-x)/2)
                nextSpeed = m2 + 1
                if a >= b:
                    return secondsElapsed + 1
                else:
                    while True:
                        a += nextSpeed
                        secondsElapsed += 1
                        if a > b:
                            break
                        b -= nextSpeed
                        secondsElapsed += 1
                        if a > b:
                            break
                        nextSpeed += 1
                    return secondsElapsed
            else:
                return 2*m2-1
    # else: # BALANCE VERSION
    #     secondsElapsed = x
    #     k2 = k - int((x-1)*x/2)
    #     m = (-(2*x+1) + math.sqrt(pow((2*x+1), 2) - 4 * (2*x-k2)))/2
    #     m2 = int(m)
    #     if m == int(m):
    #         return x+2*(m2+1)-1
    #     else:
    #         secondsElapsed = x + 2*(m2 + 1)
    #         a = (m2+1) * (2*x+m2)/2 + int((x-1)*x/2)
    #         b = k - (m2+1) * (2*x+m2)/2
    #         nextSpeed = x + m + 1
    #         if a >= b:
    #             return secondsElapsed + 1
    #         else:
    #             while True:
    #                 a += nextSpeed
    #                 secondsElapsed += 1
    #                 if a >= b:
    #                     break
    #                 b -= nextSpeed
    #                 secondsElapsed += 1
    #                 if a >= b:
    #                     break
    #                 nextSpeed += 1
    #             return secondsElapsed-1
        # a = int((x - 1) * x / 2)
        # b = k
        # for speed in range(x, k):
        #     a += speed
        #     secondsElapsed += 1
        #     if a >= b:
        #         break
        #     b -= speed
        #     secondsElapsed += 1
        #     if a >= b:
        #         break

        return secondsElapsed - 1


if __name__ == '__main__':
    with open("race.in", "r") as f1:
        k, n = map(lambda x: int(x), f1.readline().strip().split(" "))
        endingSpeeds = []
        for _ in range(n):
            endingSpeeds.append(int(f1.readline().strip()))
        l = math.ceil((math.sqrt((8 * k) + 1) - 1) / 2)
        with open("race.out", "w") as f2:
            for x in endingSpeeds:
                ans = race(l, k, x)
                f2.write(f"{ans}\n")
