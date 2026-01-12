def maxCandies(candies,extraCandies):
    maxCandies = max(candies)
    ans=[]
    for i in candies:
        if (i+extraCandies >= maxCandies):
            ans.append(True)
        else:
            ans.append(False)
    return ans

print(maxCandies([2,3,5,1,3],3)) 