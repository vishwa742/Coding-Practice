array = [[1950, 1961], [1960, 1971], [1970, 1981]]
dict = {}
for i in range(len(array)):
    for x in range(array[i][0], array[i][1]):
        if x in dict:
            dict[x] += 1
        else:
            dict[x] = 1
biggest = max(dict.values())
list = []
for k, v in dict.items():
    if v == biggest:
        list.append(k)
print(min(list))
