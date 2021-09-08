
# Operators in Python can be overloaded with dunder method
# these methods are called when a given operator is used on the object.

class Number:
    def __init__(self, num):  # dunder __init__
        self.num = num

    # dunder __add__, it is defined in python doc, if you want to overload + operator you can use __add__ method.
    def __add__(self, num2):
        print("Let's add")
        # return 300 #here I said __add__ will always return 300
        return self.num + num2.num

    def __mul__(self, num2):
        print("Let's multiply")
        return self.num * num2.num

    # def __str__(self):
    #     return f"Decimal number: {self.num}"    
    #if the above line is not there print(n1) will print <__main__.Number object at 0x7fec5931ffd0>


n1 = Number(4)  # created n1 object from Number class
n2 = Number(6)  # created n2 object from Number class
sum = n1+n2  # __add__ will be called #10
multi = n1 * n2
print(sum)
print(multi)
print(n1)
