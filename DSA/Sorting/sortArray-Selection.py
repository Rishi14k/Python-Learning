def sortArr(nums):
    n=len(nums)

    for i in range(n):
        mn = nums[i]
        idx = i
        for j in range(i+1,n):
            if nums[j]<mn:
                mn=nums[j]
                idx=j
        temp = nums[i]
        nums[i] = nums[idx]
        nums[idx] = temp
    return nums


print(sortArr([2,5,165,11,310,63130,56,12,0]))