def linearSearch(n,target):

    for i in range(len(n)):
        if n[i] == target:
            return i
        
    return -1

print(linearSearch([1,5,6,1,20,50,20],1))