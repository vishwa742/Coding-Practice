nums = [1, 1, 1, 1]

dict = {}
list = []
tot = 0
for i, v in enumerate(nums):
    if v in dict:
        dict[v] += 1
    else:
        dict[v] = 1

for k, v in dict.items():
    for x in range(v):
        tot += x
print(tot)
