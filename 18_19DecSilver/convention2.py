from queue import PriorityQueue
if __name__ == "__main__":
    with open("convention2.in", "r") as f1:
        n = int(f1.readline().strip())
        cows = PriorityQueue()
        arrivalTimes = []
        for i in range(n):
            a, b = f1.readline().strip().split(" ")
            a, b = int(a), int(b)
            arrivalTimes.append(a)
            cows.put((i, a, b))
        while cows:
            print(cows.get())