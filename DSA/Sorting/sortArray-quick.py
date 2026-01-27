def partision(nums,l,r):
    key=nums[r]
    start=l

    for i in range(l,r+1):
        if nums[i]<=key:
            temp=nums[i]
            nums[i]=nums[start]
            nums[start]=temp
            start+=1
    
    return start-1

def quickSort(nums,l,r):
    if l>=r:
        return 
    partPoint = partision(nums,l,r)

    quickSort(nums,l,partPoint-1)
    quickSort(nums,partPoint+1,r)



def sortArray(nums):
    n=len(nums)
    quickSort(nums,0,n-1)

    return nums

print(sortArray([0,3,1,2,6,8,4]))
