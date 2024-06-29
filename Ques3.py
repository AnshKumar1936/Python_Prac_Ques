num=int(input("Enter the number:"))

#using while loop
fact=1
i=1
while(i<=num):
    fact=fact*i
    i+=1
print("Factorial is:", fact)

# using for loop
fact=1
i=1

for i in range(1,num+1):
    fact=fact*i
    i+=1
print("Factorial is:", fact)
