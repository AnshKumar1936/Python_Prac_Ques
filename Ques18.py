class addition:
    def __init__(self):
        self.a = float(input("Enter the value of a:"))
        self.b = float(input("Enter the value of b:"))

    def res(self):
        return self.a+self.b

class subtract:
    def __init__(self):
        self.a = float(input("Enter the value of a:"))
        self.b = float(input("Enter the value of b:"))

    def res(self):
        return self.a-self.b
    
class multiplication:
    def __init__(self):
        self.a = float(input("Enter the value of a:"))
        self.b = float(input("Enter the value of b:"))

    def res(self):
        return self.a*self.b
    
class divide:
    def __init__(self):
        self.a = float(input("Enter the value of a:"))
        self.b = float(input("Enter the value of b:"))

    def res(self):
        return self.a/self.b
    

add = addition()
print("Addition:",add.res())

sub = subtract()
print("Subtraction:",sub.res())

mul = multiplication()
print("Multiplication:",mul.res())

div = divide()
print("Division:",div.res())
    
