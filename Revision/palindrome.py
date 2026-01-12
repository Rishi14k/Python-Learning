def checkPalindrome(num):
    temp=num
    ans=0
    while temp > 0:
        r=temp%10
        temp//=10
        ans = (ans*10+r)
    
    if num == ans:
        return True
    else:
        return False

print("ans",checkPalindrome(-151))