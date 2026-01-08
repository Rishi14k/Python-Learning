# name = input("Enter the name: ")
# age = input("Enter your age: ")
# city = input("Enter your city: ")

# print(f"your name is {name}, your age {age} and you are living in {city}")

# a=float(input("Enter number: "))
# b=float(input("Enter second no: "))

# while True:
#     try:
#         print(f"sum: {a+b}")
#         print(f"minus: {a-b}")
#         print(f"multiply: {a*b}")
#         print(f"division: {a/b}")
#     except ValueError:
#         print("Invalid type for calculation")
#     except ZeroDivisionError:
#         print("Zero can't be divide")
#     except Exception as e:
#         print("Unexpected Error")


# no = float(input("Enter number to check it is even or odd: "))

# if(no%2 == 0):
#     print("Even number")
# else:
#     print("Odd number")
# 
# a=float(input("Enter number 1: "))
# b=float(input("Enter number 2: "))
# c=float(input("Enter number 3: "))

# if(a>b and a>c):
#     print(a)
# elif(b>c and b>a):
#     print(b)
# elif(c>a and c>b):
#     print(c)
# else:
#     print("Something went wrong")


# if a>0:
#     print("Positive")
# elif a<0:
#     print("negative")
# elif a==0:
#     print("Zero")

# word = input("Enter any str: ")
# vowels = "a e i o u"
# lowerWord = word.lower()
# count = 0

# for w in lowerWord:
#     if w in vowels:
#         count+=1

# print("count of vowels: ", count)

# str = "Rishi"
# arr =list(str)
# arr.reverse()
# result = ''.join(arr)
# print(result)

# no = int(input("Enter number for table: "))

# for i in range(1,11):
#     print(no * i)

# lst = [5,10,20]
# sum = 0

# for i in lst:
#     sum+=i

# print(sum)

# lst = [5,105,54,10,6,1]
# minm = lst[0]
# maxm = lst[0]

# for i in lst[1:]:
#     if i < minm:
#         minm = i
#     if i > maxm:
#         maxm = i
    
# print(minm, maxm)

# str = "Prince".lower()
# vowels = "a e i o u"
# new_str = ""

# for i in str:
#     if i in vowels:
#         i="*"
#     print(i)

# str="rishi@123"
# strCount = 0 
# digitCount = 0 
# specialChar = 0

# for i in str:
#     if i.isalpha():
#         strCount+=1
#     elif i.isdigit():
#         digitCount+=1
#     else:
#         specialChar +=1

# print(strCount, digitCount, specialChar)

# n = int(input("Enter number"))
# a,b=0,1
# serise = []

# for _ in range(0,n+1):
#     serise.append(a)
#     a,b=b,a+b


# print(serise)

# n=int(input("Enter the no: "))

# noStr = str(n)
# revStr = noStr[::-1]

# if noStr == revStr:
#     print("Number is palindrom")
# else:
#     print("Number is not palindrom")

# student = {
#     "Rishi":{
#         "Math":10,
#         "Eng":5,
#         "Guj":20
#     },
#     "Mahek":{
#         "Math":10,
#         "Eng":5,
#         "Guj":20
#     },
#     "Rohit":{
#         "Math":10,
#         "Eng":5,
#         "Guj":20
#     },
#     "Meet":{
#         "Math":10,
#         "Eng":5,
#         "Guj":20
#     }
# }

# print(student.keys())
# print(student.values())
# print(student)

# lst = [1,58,"Risi","Risi",20,10,10,10]
# print(set(lst))

# def cTof(num):
#     f=num*(9/5)+32
#     return f

# Fahrenheit = cTof(20)
# print(f"{Fahrenheit}f")

# lst = [1,2,5,1,3]
# ct = 0
# dictr = {}
# for i in lst:
#     ct = lst.count(i)

#     print(f"{i} = {ct}")

# for i in lst:
#     if i in dictr:
#         dictr[i]+=1
#     else:
#         dictr[i]=1

# print(dictr)

# def isPrime(n):
#     if n<=1:
#         return False
#     for i in range(2,int(n**0.5)+1):
#         if n %i==0:
#             return False
        
#     return True

# num = isPrime(10)
# print(num)

# for i in range(1,101):
#     if i%2!=0:
#         continue
#     print(i)


# def leftRotationList(lst, k):
#     n= len(lst)
#     k = k%n
#     print(k)
#     lst_rotation = lst[k:] + lst[:k]
#     return lst_rotation

# def rightListRotation(lst, k):
#     n= len(lst)
#     k=k%n
#     return lst[-k:] + lst[:-k]

# # rotation = leftRotationList([1,2,3,4,5],7)
# # print(rotation)

# rotation = rightListRotation([1,2,3,4,5],1)
# print(rotation)


# def sortAndMerge(
# lst1, lst2):
#     result =[]
#     i,j=0,0

#     while i<len(lst1) and j<len(lst2):
#         if lst1[i] <= lst2[j]:
#             result.append(lst1[i])
#             i+=1
#         else:
#             result.append(lst2[j])
#             j+=1
#     result.extend(lst1[i:])     
#     result.extend(lst2[j:])

#     return result

# data = sortAndMerge([1,2,3],[11,2,3])
# print(data)


# def selection_sort(arr):
#     """Sorts a list in-place using the Selection Sort algorithm."""
#     n = len(arr)
#     for i in range(n):
#         # Find the minimum element in the remaining unsorted array
#         min_idx = i
#         for j in range(i + 1, n):
#             if arr[j] < arr[min_idx]:
#                 min_idx = j
        
#         # Swap the found minimum element with the element at position i
#         arr[i], arr[min_idx] = arr[min_idx], arr[i]
#     return arr

# def merge_and_sort_unsorted(list1, list2):
#     # 1. Merge the two lists
#     merged_list = list1 + list2
    
#     # 2. Sort the merged list using the manual Selection Sort function
#     sorted_list = selection_sort(merged_list)
    
#     return sorted_list

# # Example Usage
# list_a = [9, 4, 1, 6]
# list_b = [18, 2, 7, 5]

# final_result = merge_and_sort_unsorted(list_a, list_b)
# print(f"List A: {list_a}")
# print(f"List B: {list_b}")
# print(f"Merged and Sorted Result: {final_result}")
# # Output: [1, 2, 4, 5, 6, 7, 8, 9]

# lst1= [1,2,3,4]
# lst2= [11,12,13,4]

# s1 = set(lst1)
# s2 = set(lst2)
# common = s1.intersection(s2)
# print(list(common))

# lst=[1,2,3,3,4]
# minimum=min(lst)
# maximum=max(lst)
# secondMax = lst[0]

# for i in lst:
#     if i<maximum and i>minimum:
#         secondMax=i
    

# print(secondMax)
# lst.insert(secondMax-1,0)
# lst.remove(3)
# print(lst)

# def secondSmall(tupleData):
#     if len(tupleData) < 3:
#         return "Error: required more than 2"

#     if tupleData[0] > tupleData[1]:
#         smallest = tupleData[1]
#         secondSmallVal = tupleData[0]
#     else:
#         smallest = tupleData[0]
#         secondSmallVal = tupleData[1]

#     for i in tupleData[2:]:
#         if i < smallest:
#             secondSmallVal = smallest
#             smallest = i
#         elif i < secondSmallVal and i != smallest:
#             secondSmallVal = i
        

#     if smallest == secondSmallVal:
#         return secondSmallVal
    
#     return secondSmallVal

# result = secondSmall((1,2,3))
# print(result)

# def zeroShift(lst):
#     for i in lst:
#         if i == 0:
#             lst.remove(i)
#             lst.append(i)
#     return lst

# def zeroShift(lst):
#     non_zero = [x for x in lst if x!=0]
#     all_zero = [x for x in lst if x==0]

#     return non_zero + all_zero

# res = zeroShift([1,0,2,5,0,1,0,5,2])
# print(res)

# def removeDuplicate(str):
#     seti = set(str)

#     return ",".join(seti)

# def removeDuplicate(str):
#     setVal = set()
#     res = []

#     for i in str:
#         if i not in setVal:
#             res.append(i)
#             setVal.add(i)
        
#     return "".join(res)

# print(removeDuplicate("Rishi"))


# def checkAnagram(str, str2):
#     if len(str) != len(str2):
#         return False
    
#     a_sorted = sorted(str.lower())
#     b_sorted = sorted(str2.lower())

#     return a_sorted == b_sorted

# print(checkAnagram("Rishi", "IshiR"))

# def longword(str):
#     word = str.split(" ")
#     if not word:
#         return "no words given"
    
#     max_len = max(word, key=len)
#     return max_len

# def lonwordStr(str):
#     words = str.split(" ")
#     max_word = words[0]

#     for i in words:
#         if len(i) > len(max_word):
#             max_word = i

#     return max_word 

# print(lonwordStr("Hi I am Rishi"))

# str2 = "Rishi j kon che"
# print(str2.title())

