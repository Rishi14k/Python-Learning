def wordRev(s):
    s=s.strip()
    s=s.split()
    s.reverse()

    return " ".join(s)

# print(wordRev("My name is Rishi"))

# name="My name Rishi"
# print(name.split())

def wordREV(s):
    s=s.strip()
    s=s.split()
    i=0
    j=len(s)-1

    while i<j:
        temp=s[i]
        s[i]=s[j]
        s[j]=temp
        i+=1
        j-=1
    print(" ".join(s))

wordREV("    My   name is    Rishi    ")