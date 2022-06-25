import math


def race(l, k, x):
    if l == x:
        return x
    elif l < x:
        return l
    else:
        secondsElapsed = x

        a = int((x - 1) * x / 2)
        b = k
        for speed in range(x, k):
            a += speed
            secondsElapsed += 1
            if a >= b:
                break
            b -= speed
            secondsElapsed += 1
            if a >= b:
                break

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
