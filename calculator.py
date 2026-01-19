class Calculator:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        print(self.num1+self.num2)

    def sub(self):
        print(self.num1-self.num2)

    def mul(self):
        print(self.num1*self.num2)

    def div(self):
        if self.num2 == 0:
            print('Cannot divide by zero')
        else:
            print(self.num1/self.num2)
a = Calculator(10,2)
a.add()
a.div()
a.mul()
a.sub()

