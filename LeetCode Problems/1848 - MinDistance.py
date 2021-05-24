nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
target = 1
start = 0

dict = {}
for i in range(len(nums)):
    if nums[i] == target:
        if nums[i] in dict:
            dict[nums[i]+i] = abs(i-start)
        else:
            dict[nums[i]] = abs(i-start)

smallest = min(dict.values())
print(smallest)
