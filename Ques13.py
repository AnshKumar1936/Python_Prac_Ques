sal=int(input("Enter your Salary:"))
year=int(input("Enter total year of your Service:"))

def calc(n,m):
    bonus=n*30/100
    if(m>=5):
      print("Total net bonus of Employee",n+bonus)
    else:
       print("Employee did't work for 5 years or more...")


calc(sal,year)
