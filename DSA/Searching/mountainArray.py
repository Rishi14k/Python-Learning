# mountain array mean number goes increasing to descring order
def mountainArr(nums):
    n=len(nums)
    l=0
    r=n-1
    ans=n-2

    while l<=r:
        mid=(l+r)//2

        if nums[mid] < nums[mid+1]:
            l=mid+1
        else:
            ans=mid
            r=mid-1
    
    return ans

print(mountainArr([0,10,5,2]))