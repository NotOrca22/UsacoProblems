with open("shell.in", "r") as f1:
    i = int(f1.readline().strip())
    commands = []
    for x in range(i):
        commands.append(f1.readline().strip().split(" "))
    guess1 = 0
    guess2 = 0
    guess3 = 0
    pebbleSlot = 1
    for command in commands: # pebble in 1
        # pebbleSlot = 1
        slot1, slot2 = int(command[0]), int(command[1])
        guess = int(command[2])
        if pebbleSlot == slot1:
            pebbleSlot = slot2
        elif pebbleSlot == slot2:
            pebbleSlot = slot1
        if guess == pebbleSlot:
            guess1 += 1
    pebbleSlot = 2
    for command in commands: # pebble in 2
        slot1, slot2 = int(command[0]), int(command[1])
        guess = int(command[2])
        # print(slot1, slot2, guess)
        # print(command)
        if pebbleSlot == slot1:
            pebbleSlot = slot2
            # print(pebbleSlot)
        elif pebbleSlot == slot2:
            pebbleSlot = slot1
            # print(pebbleSlot)
        # print(pebbleSlot)
        if guess == pebbleSlot:
            # print(command)
            guess2 += 1
    pebbleSlot = 3
    for command in commands: # pebble in 3
        # pebbleSlot = 3
        slot1, slot2 = int(command[0]), int(command[1])
        guess = int(command[2])
        if pebbleSlot == slot1:
            pebbleSlot = slot2
        elif pebbleSlot == slot2:
            pebbleSlot = slot1
        if guess == pebbleSlot:
            guess3 += 1
    # print(guess1, guess2, guess3)
    with open("shell.out", "w") as f2:
        f2.write(str(max(guess1, guess2, guess3)) + "\n")