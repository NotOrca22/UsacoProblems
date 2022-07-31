if __name__ == "__main__":
    x = int(input())
    cows = input().split(" ")
    cows = [int(cow) for cow in cows]
    # print(cows)
    evens = 0
    odds = 0
    for cow in cows:
        if cow % 2 == 0:
            evens += 1
        else:
            odds += 1
    # print(odds, evens)
    if evens == odds or evens == odds + 1:
        print(x)
    elif odds > evens:
        while odds > evens:
            odds -= 2
            evens += 1
        if evens > odds + 1:
            print(2 * odds + 1)
        else:
            print(odds + evens)
    else:
        print(2 * odds + 1)