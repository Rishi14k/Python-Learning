def maxProfit(nums):
    min_price = nums[0]
    profit = 0

    for i in range(1,len(nums)):
        curr_profit = nums[i] - min_price
        if curr_profit > profit:
            profit = curr_profit
        min_price = min(min_price,nums[i])
    
    return profit

print(maxProfit([7,1,5,3,4,6]))