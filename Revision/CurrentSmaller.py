nums=[8,1,2,2,3]

arr=[]
for i in nums:
    count=0
    for j in nums:
        if j<i:
            count+=1
    arr.append(count)

print(arr)