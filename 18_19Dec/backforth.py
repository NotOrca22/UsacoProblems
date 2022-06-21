if __name__ == "__main__":
    with open("backforth.in", "r") as f1:
        room1 = f1.readline().strip().split(" ")
        room2 = f1.readline().strip().split(" ")
        b1 = [int(x) for x in room1]
        b2 = [int(x) for x in room2]
        milk = 1000
        results = set()
        for i1 in set(b1):
            b11 = b1.copy()
            b11.remove(i1)
            b21 = b2.copy()
            b21.append(i1)
            for i2 in set(b21):
                b22 = b21.copy()
                b22.remove(i2)
                b12 = b11.copy()
                b12.append(i2)
                for i3 in set(b12):
                    b13 = b12.copy()
                    b13.remove(i3)
                    b23 = b22.copy()
                    b23.append(i3)
                    for i4 in set(b23):
                        results.add(milk-i1+i2-i3+i4)
        with open("backforth.out", "w") as f2:
            f2.write(str(len(results)))