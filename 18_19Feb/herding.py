with open("herding.in", "r") as f1:
    spaces = f1.readline().strip().split(" ")
    spaces = [int(x) for x in spaces]
    minimum = 0
    if spaces[2] - spaces[1] == spaces[1] - spaces[0] == 1:
        minimum = 0
    elif spaces[1] - spaces[0] == 2 or spaces[2] - spaces[1] == 2:
        minimum = 1
    else:
        minimum = 2
    maximum = max(spaces[2]-spaces[1], spaces[1]-spaces[0])
    with open("herding.out", "w") as f2:
        f2.write(str(minimum) + "\n")
        f2.write(str(maximum-1) + "\n")
