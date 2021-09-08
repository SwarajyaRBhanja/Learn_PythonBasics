
import datetime
#Sometimes we need a method that doesn't use the self parameter.we can define a static method like this.
'''
@staticmethod #decorator to mark greet as static method.
def greet():
    print("Hello User !!")
'''

class Letter:
    @staticmethod
    def greet():
        print("Good Morning, Swarajya!")

    def subject(self,line):
        print(f"{datetime.datetime.now()} Wishing you a great Python Programming Journey {line}.")

let= Letter()
let.greet()
let.subject("Mr.Bhanja")        

#here let.greet() will not be converted to Letter.greet(let) when I use static method
#Now if I add self, I will get error TypeError: greet() missing 1 required positional argument: 'self'

