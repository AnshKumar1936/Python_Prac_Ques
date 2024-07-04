amt=int(input("Enter the amount:"))

def calc(n):
    if(n>=1000):
      print("Total cost on User",n-10/100)
    else:
       print("Purchase is less than 1000")


calc(amt)
