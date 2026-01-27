# in array only 0,1,2 avalibale 

## using counting sort 
def sortColor(nums):
    n=len(nums)
    mx=max(nums)
    freq = [0] * (mx+1)

    for i in nums:
        freq[i]+=1
    
    nums=[]

    for i in range(0,mx+1):
        while freq[i]>0:
            nums.append(i)
            freq[i]-=1        
    return nums

print(sortColor([1,2,1,0,2,0]))

## using diffrent method  
def sortColors(nums):
    l=0
    r=len(nums)-1
    i=0

    while i<=r:
        if nums[i] == 1:
            i+=1
        elif nums[i] == 0:
            temp = nums[i]
            nums[i] = nums[l]
            nums[l]=temp
            i+=1
            l+=1
        else:
            temp = nums[i]
            nums[i] = nums[r]
            nums[r] = temp
            r-=1

    return nums


print(sortColors([1,2,0,2,0,1,2]))