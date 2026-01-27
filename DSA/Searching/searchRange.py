def lowerBound(nums,target):
    n=len(nums)
    l=0
    r=n-1
    ans=n

    while l<=r:
        mid = (l+r)//2

        if nums[mid] >= target:
            ans=mid
            r=mid-1
        else:
            l=mid+1
    
    return ans

def upperBound(nums,target):
    n=len(nums)
    l=0
    r=n-1
    ans=n

    while l<=r:
        mid = (l+r)//2

        if nums[mid] > target:
            ans=mid
            r=mid-1
        else:
            l=mid+1
    
    return ans

def searchRange(nums,target):
    lb=lowerBound(nums,target)
    ub=upperBound(nums,target)
    print(lb)
    print(ub)

    if lb==ub:
        return [-1,-1]
    else:
        return [lb,ub-1]

print(searchRange([1,1,2,2,2,3,3,5,5,5,6,9,9,10],2))