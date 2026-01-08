# num1 = float(input("Enter number one"))
# num2 = float(input("Enter number two"))

# choice = input("Enter sign ")

# if(choice == "+"):
#     print(num1+num2)
# elif(choice == "-"):
#     print(num1-num2)
# elif(choice == "*"):
#     print(num1*num2)
# elif(choice == "/"):
#     print(num1/num2)
# elif(choice == "//"):
#     print(num1//num2)
# elif(choice == "**"):
#     print(num1**num2)
# else:
#     print("Enter valid sign ")

# i = 10
# while i<=20:
#     print(i)
#     i+=2

# lst = [1,2,3]
# for i in lst:
#     print(i)
#     print(lst)
# for i in range(1,11):
#     if i%2==0:
#         print(i)


# start = int(input("Enter start point number "))
# stop = int(input("Enter end point number "))


# if(start > stop):
#     print("Bhai majak q kar raha haooi!!")


# skip= int(input("Enter skip number "))


# for i in range(start, stop+1):
#     if i == skip:
#         continue
#     print(i)

# str = "Rishi"
# print(str[::-1])


# lst=[1,2,3,8,10,99,]
# lst2=[3,4,5]
# print(lst+lst2)
# lst.extend(lst2)
# print(lst)
# # lst.sort()

# s1=set(lst)
# s2=set(lst2)
# s3=s1.intersection(s2)
# print(list(s3))

# squre = {x:x*x for x in range(5,15)}
# print(squre)

# def my_deco(func):
#     def wrapper():
#         print("Before")
#         func()
#         print("After")
#     return wrapper

# @my_deco
# def say_hello():
#     return print("KEm bhai aa gaya svad!!")

# print(say_hello())
# my_deco() ##In valid argument
# say_hello()
# my_deco(say_hello())



# class Car():
#     def start( brand, engine):
#         brand = brand
#         engine = engine
#         print(f"{brand} Car is starting with {engine}...")
#     def stop(slef):
#         print("Car is stopping...")

# car1 = Car()
# car2 = Car()
# car1.start("BMW")
# car2.start("Pagani")
# car1.stop()
# car2.stop()


# class Student:
#     def __init__(self, name="Rishi", age=19):
#         self.name = name 
#         self.age = age
#     def course(self, c_name):
#         self.c_name = c_name
#         print(f"Course name: {c_name}")

# s1 = Student()
# print(s1.name, s1.age)
# s1.course("BSc")


# class BankAccount():
#     def __init__(self, ac, balance):
#         self.ac = ac
#         self.__balace = balance

#     def deposite(self,amount):
#         self.__balace += amount
#         print(f"Deposited amount {amount}.. and current balance {self.__balace}")

    
# b1 = BankAccount(1324, 6000)
# b1.deposite(6500)
# print(b1.__balace) # this give error 

file = open("./rishi1.txt", "w")
content = file.write("I am writing for testing the file creation")
print(content)
file.close()