length = int(input("Enter the length of rectangle:"))
breadth = int(input("Enter the breadth of rectangle:"))


result = length*breadth
print("The area of rectangle is :" , result)
if(length == breadth):
    print("Its a Square...")
else:
    print("Its not a Square...")