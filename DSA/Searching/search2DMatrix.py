def search2D(matrix,target):
    row=len(matrix)
    col=len(matrix[0])

    l=0
    r=(row*col) - 1

    while l<=r:
        mid=(l+r)//2

        if matrix[mid//col][mid%col] == target:
            return True
        elif matrix[mid//col][mid%col] > target:
            r=mid-1
        else:
            l=mid+1
    
    return False

print(search2D([[1,3,5,7],[10,11,16,20],[23,30,34,60]],61))