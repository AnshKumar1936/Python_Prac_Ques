num=int(input("Enter the number: "))  
sum=0  
for i in range(1,num):  
    if (num%i==0):  
        sum=sum+i  
if(sum==num):  
    print("This is a perfect number")  
else:  
    print("This is not a perfect number")  