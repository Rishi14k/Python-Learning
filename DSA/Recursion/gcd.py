def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)

def lcm(a,b):
    return (a*b) // gcd(a,b)

print(gcd(15,50))
print(lcm(15,50))
