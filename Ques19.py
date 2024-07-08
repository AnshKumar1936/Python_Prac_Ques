class Ques19:
    def __init__(self):
        self.even = []
        self.odd = []

    def collect(self):
        for i in range(0,101,2):
            self.even.append(i)
        for i in range(1,101,2):
            self.odd.append(i)


    def result(self):
        print("Even Numbers:", self.even)
        print("Odd Numbers:", self.odd)


calc = Ques19()
calc.collect()
calc.result()
            