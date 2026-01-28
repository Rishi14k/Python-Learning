def getHours(piles,mid):
    ans = 0

    for p in piles:
        ans+=(p+mid-1)//mid
    
    return ans

def koko(piles,h):
    l=1
    r=max(piles)
    k=r
    while l<=r:
        mid = (l+r)//2

        if getHours(piles,mid) > h:
            l=mid+1
        else:
            k=mid
            r=mid-1
    
    return k

print(koko([3,6,7,11],8))