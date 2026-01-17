# fact = 5
# # i=1

# # while i<=fact:
# #     print(i*i)
# #     i+=1

# for i in range(1,fact):
#     fact*=i
   
# print(fact)

def factorial(fact):
    if fact < 0:
        return
    if fact == 0 or fact == 1:
        return 1

    return fact * factorial(fact - 1)

print(factorial(5))