# merge arr without any extra space

def mergeArr(num1,m,num2,n):
    i=m-1
    j=n-1
    k=m+n-1

    while j>=0:
        if i<0 or num2[j]>num1[i]:
            num1[k] = num2[j]
            j-=1
            k-=1
        else:
            num1[k] = num1[i]
            k-=1
            i-=1
    
    return num1

print(mergeArr([1,2,3,0,0,0],3,[2,5,6],3))
