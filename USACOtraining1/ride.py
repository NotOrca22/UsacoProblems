"""
ID: orcawha1
LANG: PYTHON3
TASK: ride
"""
chars = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
if __name__ == "__main__":
    with open("ride.in", "r") as f1:
        comet = f1.readline()
        group = f1.readline()
        cometNumber = 1
        groupNumber = 1
        comet = comet.replace("\n", "")
        group = group.replace("\n", "")
        for char in comet:
            cometNumber *= (chars.index(char) + 1)
        for char in group:
            groupNumber *= (chars.index(char) + 1)
        with open("ride.out", "w") as f2:
            if cometNumber % 47 != groupNumber % 47:
                f2.write("STAY")
            else:
                f2.write("GO")
            f2.write("\n")