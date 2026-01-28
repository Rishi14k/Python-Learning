def sqrt(nums):
    l=1
    r=nums
    ans=1
    while l<=r:
        mid=(l+r)//2
        midSquare = mid*mid
        if midSquare > nums:
            r=mid-1
        else:
            ans=mid
            l=mid+1
    
    return ans

print(sqrt(27))