numbers = input().split(" ")
numbers = [int(x) for x in numbers]
abc = max(numbers)
a = min(numbers)
bc = abc - a
for d in numbers:
    for e in numbers:
        if d + e == bc:
            if d <= e:
                b = d
                c = e
            else:
                b = e
                c = d
print(a,b,c)