cows = [1,2,3,4,5,6,7]
a1=2
a2=5
b1=3
b2=7
cows = cows[:a1-1] + list(reversed(cows[a1-1:a2])) + cows[a2:]
print(cows)
cows = cows[:b1 - 1] + list(reversed(cows[b1 - 1:b2])) + cows[b2:]
print(cows)
cows = cows[:a1-1] + list(reversed(cows[a1-1:a2])) + cows[a2:]
cows = cows[:b1 - 1] + list(reversed(cows[b1 - 1:b2])) + cows[b2:]
print(cows)