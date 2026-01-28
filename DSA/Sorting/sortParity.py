# even in start and odd in end

def paritySort(nums):
    start = 0

    for i in range(len(nums)):
        if nums[i]%2==0:
            temp = nums[i]
            nums[i] = nums[start]
            nums[start] = temp
            start+=1
    
    return nums

print(paritySort([4,5,8,6,7,9]))