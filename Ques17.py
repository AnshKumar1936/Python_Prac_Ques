x = int(input("Enter 1st side of triangle."))
y = int(input("Enter 2nd side of triangle."))
z = int(input("Enter 3rd side of triangle."))

result = x*y*z
print("Equilateral Triangle is:",result)
if(x==y==z):
    print("Its is Equilateral triangle.")
else:
    print("Its is not an Equilateral triangle.")