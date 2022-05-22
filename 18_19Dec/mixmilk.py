
def pourMilk(contains_pour, capacity_receive, contains_receive):
    canAdd = capacity_receive - contains_receive
    if canAdd >= contains_pour:
        contains_receive += contains_pour
        contains_pour = 0
    else:
        contains_receive += canAdd
        contains_pour -= canAdd
    return(contains_pour, capacity_receive, contains_receive)
if __name__ == "__main__":
    with open("mixmilk.in", "r") as f1:
        capacity_1, contains_1 = f1.readline().strip().split(" ")
        capacity_2, contains_2 = f1.readline().strip().split(" ")
        capacity_3, contains_3 = f1.readline().strip().split(" ")
        capacity_1, contains_1, capacity_2, contains_2, capacity_3, contains_3 = int(capacity_1), int(contains_1), int(
            capacity_2), int(contains_2), int(capacity_3), int(contains_3)
        for i in range(100):
            if i % 3 == 0:
                x = pourMilk(contains_1, capacity_2, contains_2)
                contains_1 = x[0]
                contains_2 = x[2]
            elif i % 3 == 1:
                x = pourMilk(contains_2, capacity_3, contains_3)
                contains_2 = x[0]
                contains_3 = x[2]
            else:
                x = pourMilk(contains_3, capacity_1, contains_1)
                contains_3 = x[0]
                contains_1 = x[2]

        with open("mixmilk.out", "w") as f2:
            f2.write(str(contains_1) + '\n')
            f2.write(str(contains_2) + "\n")
            f2.write(str(contains_3) + "\n")