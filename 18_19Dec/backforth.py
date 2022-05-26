if __name__ == "__main__":
    with open("backforth.in", "r") as f1:
        room1 = f1.readline().strip().split(" ")
        room2 = f1.readline().strip().split(" ")
        room1 = [int(x) for x in room1]
        room2 = [int(x) for x in room2]
        possibleValues = []
        milk = 1000
        for bucket1 in room1:
            room10 = room1
            room20 = room2
            room10.pop(room10.index(bucket1))
            room20.append(bucket1)
            for bucket2 in room20:
                print(len(room20))
                room200 = room20
                room100 = room10
                room200.pop(room200.index(bucket2))
                room100.append(bucket2)
                for bucket3 in room100:
                    room2000 = room200
                    room1000 = room100
                    room1000.pop(room1000.index(bucket3))
                    room2000.append(bucket3)
                    for bucket4 in room2000:
                        room10000 = room1000
                        room20000 = room2000
                        room20000.pop(room20000.index(bucket4))
                        room10000.append(bucket4)
                        possibleValues.append(milk+bucket1-bucket2+bucket3-bucket4)
        print(list(set(possibleValues)))
        with open("backforth.out", "w") as f2:
            f2.write(str(len(list(set(possibleValues)))))