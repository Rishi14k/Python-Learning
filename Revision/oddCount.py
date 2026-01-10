low = int(input("Enter the lower limit: "))
high = int(input("Enter the upper limit: "))

count=0

for i in range(low,high+1):
    if i%2!=0:
        count+=1

print(count)