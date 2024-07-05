multiply = lambda a,b : a*b

num = int(input("Enter the value of num:"))
print("The Table of", num)
for i in range(1,11):
    print(num , "x" , i , "is :", multiply(num,i))