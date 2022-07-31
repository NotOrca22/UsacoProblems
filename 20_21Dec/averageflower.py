def hasAverageFlower(photo):
    average = sum(photo)/len(photo)
    for flower in photo:
        if float(flower) == average:
            return True
    return False
x = int(input())
petals = input().split(" ")
petals = [int(x) for x in petals]
count = 0
for i in range(x):
    for j in range(i+1,x+1):
        photo = petals[i:j]
        if hasAverageFlower(photo):
            count += 1
print(count)