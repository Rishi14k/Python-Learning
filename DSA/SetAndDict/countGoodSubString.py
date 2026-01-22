def countGoodSubString(str1):
    n=len(str1)
    ans=0

    for i in range(0,n-2):
        if str1[i]!=str1[i+1] and str1[i+1]!=str1[i+2] and str1[i+2]!=str1[i]:
            ans+=1
    return ans

print(countGoodSubString("aababcabc"))