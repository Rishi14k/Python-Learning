def maximumWealth(accounts):
    ans=0
    for acc in accounts:
        ans = max(ans,sum(acc))
    return ans

print(maximumWealth([[1,2,3],[5,8,4],[12,8,10]]))