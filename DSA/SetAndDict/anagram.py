def anagram(str1,str2):
    str1 = str1.lower()
    str2=str2.lower()
    lst1=list(str1)
    lst2=list(str2)
    lst1.sort()
    lst2.sort()
    s1e = "".join(lst1)
    s2e = "".join(lst2)

    return s1e == s2e
    

print(anagram("Rishi","iRshi"))