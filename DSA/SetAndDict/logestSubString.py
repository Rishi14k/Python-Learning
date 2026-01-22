def logestSubString(s):
    n=len(s)
    ans=1
    set1 = set({})
    set1.add(s[0])
    if n==0:
        return 0

    i=0
    j=1

    while j<n:
        while s[j] in set1:
            set1.discard(s[i])
            i+=1
        set1.add(s[j])
        j+=1
        ans = max(ans,(j-i))

    return ans

print(logestSubString("abcabcbb"))