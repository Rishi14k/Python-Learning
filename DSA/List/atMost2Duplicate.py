def atMosatTwoRemoveDuplicate(nums):
    n = len(nums)
    if n <=2:
        return n
    start = 1

    for i in range(2,n):
        if nums[i] != nums[start - 1]:
            start+=1
            nums[start] = nums[i]
    
    return start+1

print(atMosatTwoRemoveDuplicate([1,1,1,2]))