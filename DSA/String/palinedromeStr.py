def palindromeSTR(sentance):
    rev = sentance[::-1]
    if sentance.lower()==rev.lower():
        return True
    else:
        return False
    

# def isAlphaNumeric(s):
#     x=ord(s)

#     if 97<=x<=122 or 65<=x<=90 or 48<=x<=57:
#         return True
#     return False

def palindromeSTRNF(s):
    s=s.lower()
    i=0
    j=len(s)-1

    while i<j:
        if not s[i].isalnum():
            i+=1
        elif not s[j].isalnum():
            j-=1
        elif s[i]==s[j]:
            i+=1
            j-=1
        else:
            return False
    return True


    

print(palindromeSTR("Nayan"))
print(palindromeSTRNF("Nayan nayan"))
