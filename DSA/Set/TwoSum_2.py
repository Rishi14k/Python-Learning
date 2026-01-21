def twoSum(nums,target):
    left = 0
    right = len(nums) - 1

    while left<right:
        sum1 = nums[left] + nums[right]
        if sum1==target:
            return [left,right]
        elif sum1 > target:
            right-=1
        else:
            left+=1

print(twoSum([2,7,11,15],9))