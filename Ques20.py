class table:
    def __init__(self):
        pass

    def result(self,a):
        for i in range(1,11):
            print("The table of ", a , "X" , i ," is:", i*a )

t = table()
num=int(input("Enter the value of num:"))
t.result(num)