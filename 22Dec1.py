n = int(input())
money = input().split()
priceCounts = {}
tuitions = []
optimal = 0
optimalPrice = 99999999999
for m in money:
    tuitions.append(int(m))
tuitions = sorted(tuitions)
for t in tuitions:
    if t in priceCounts.keys():
        priceCounts[t] += 1
    else:
        priceCounts[t] = 1
for i in range(len(priceCounts.keys())):
    price = list(priceCounts.keys())[i]
    totalPrice = price * sum(list(priceCounts.values())[i:])
    if totalPrice > optimal:
        optimal = totalPrice
        optimalPrice = price
print(optimal, optimalPrice)
# pricesToCheck = (list(set(tuitions)))
# pricesChecked = []
# for price in pricesToCheck:
#     # if price not in pricesChecked:
#         pricesChecked.append(price)
#         affordable = 0
#         for t in tuitions:
#             if t >= price:
#                 affordable += 1
#         if price*affordable > optimal:
#             optimal = price*affordable
#             optimalPrice = price
#         elif price*affordable == optimal:
#             if optimalPrice > price:
#                 optimalPrice = price
# print(optimal, optimalPrice)
