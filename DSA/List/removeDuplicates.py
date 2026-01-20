def removeDuplicates(nums):
    n = len(nums)
    start = 0

    for i in range(1,n):
        if nums[i] != nums[start]:
            start+=1
            nums[start] = nums[i]
        
    return start+1

print(removeDuplicates([3,3,5,5,7,7,7,9,9,12,12])) # output = 5