def spiralMtrix(matrix):
    c=0
    n=len(matrix)
    m=len(matrix[0])
    rowStart=0
    rowEnd=n-1
    colStart=0
    colEnd=m-1
    ans=[]
    total=n*m

    while c<total:
        #rowStart, colStart->colEnd
        for i in range(colStart,colEnd+1):
            ans.append(matrix[rowStart][i])
            c+=1
        rowStart+=1

        if c==total:
            break

        #colEnd, rowStart->rowEnd
        for i in range(rowStart,rowEnd+1):
            ans.append(matrix[i][colEnd])
            c+=1
        colEnd-=1

        if c==total:
            break

        # rowEnd, colEnd->colStart
        for i in range(colEnd,colStart-1,-1):
            ans.append(matrix[rowEnd][i])
            c+=1
        rowEnd-=1

        if c==total:
            break

        #colStart, rowEnd->rowStart
        for i in range(rowEnd,rowStart-1,-1):
            ans.append(matrix[i][colStart])
            c+=1
        colStart+=1

        if c==total:
            break
    
    return ans

print(spiralMtrix([[6,5,8,3,2],[4,6,9,4,1],[1,3,2,3,0],[2,10,1,0,2]]))


