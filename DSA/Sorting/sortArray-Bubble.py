#sort an array without in built method, use bubble sorting algorithm

def sortArr(arr):
    n=len(arr)

    for i in range(n):
        isSwap = False
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
                isSwap=True


        if not isSwap:
            break
    
    return arr


print(sortArr([1,5,6,8,54,62,3]))