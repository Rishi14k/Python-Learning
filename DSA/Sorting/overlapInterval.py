def overLapInterval(nums):
    nums.sort(key = lambda x:x[1])
    n=len(nums)

    prev = 0
    count = 1

    for i in range(1,n):
        if nums[i][0] >= nums[prev][1]:
            count+=1
            prev=i
        
    return n-count

print(overLapInterval([[1,2],[2,3],[3,4],[1,3]]))