def lastWordLen(s):
    s=s.strip()
    n=len(s)
    i= -1

    while i>=(1*-n) and s[i]!=" ":
        i-=1
    i+=1
    i*=-1

    return i

print(lastWordLen("  This   is  my  desk   "))