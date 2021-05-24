costs = [7, 3, 3, 6, 6, 6, 10, 5, 9, 2]

coins = 56
tot = 0
costs.sort()
for i in costs:
    if coins > 0 and i <= coins:
        coins -= i
        tot += 1
print(tot)
