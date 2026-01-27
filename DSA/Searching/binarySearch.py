def binarySearch(n,target):
    l=0
    r=len(n)-1

    while l<=r:
        mid=(l+r)//2

        if target == n[mid]:
            return mid
        elif target > n[mid]:
            l=mid+1
        else:
            r=mid-1
    

print(binarySearch([2,5,6,8,10,15,65],1))