def evenStart(nums):
    n = len(nums)
    start = 0

    for i in range(0,n):
        if nums[i]%2==0:
            temp = nums[i]
            nums[i] = nums[start]
            nums[start] = temp
            start+=1

        
    return nums

print(evenStart([1,2,3,5,4,2]))