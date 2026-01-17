def powerThree(num):
    if num <=0:
        return False
    if num == 1:
        return True
    if num%3!=0:
        return False
        
    return powerThree(num//3)

print(powerThree(81))