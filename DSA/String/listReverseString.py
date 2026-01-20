def revStr(l):
    i=0
    j=len(l)-1

    while i<j:
        temp = l[i]
        l[i]=l[j]
        l[j]=temp
        i+=1
        j-=1
    print(l)



revStr(['r','i','s','h','i'])