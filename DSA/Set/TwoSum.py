def twoSum(nums, target):
    n=len(nums)
    dict1 = {}

    for i in range(n):
        rem = target - nums[i]
        if rem in dict1:
            return [dict1[rem],i]
        dict1[nums[i]] = i


print(twoSum([1,5,48,3,25,21,4],46))
