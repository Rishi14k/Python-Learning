def subProductSum(num):
    temp = num
    sum_=0
    product=1

    while temp > 0:
        r=temp%10
        print(r)
        temp//=10
        print(temp)
        sum_+=r
        product*=r
    return product - sum_

print(subProductSum(4421))