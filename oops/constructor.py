
#__init__() : this is a special method which is first run asa the object is created.
#it takes self argument and can also take further argument.

class Chess:
    def frontman(self):
        print("Even if I am frontman, I will come after my king the Constructor, only when you call me")
    def __init__(self):
        print("I am the fuc'king' constructor, Your object doesn't need to call me, I will come first if you create any object")
    '''def __init__(self,name,fame):
        self.name=name
        self.fame= fame
        print(f"I am random shit inside your second constructor {name}, {fame}")'''
    def queen(self):
        print("I am the Queen, unless you call me I won't entertain you")    
d= Chess()
#c= Chess("Swarajya","Bhanja's") #object can be instantiated using constructor like this
d.frontman()
d.queen()
'''
I am the fuc'king' constructor, Your object doesn't need to call me, I will come first if you create any object
Even if I am frontman, I will come after my king the Constructor, only when you call me
I am the Queen, unless you call me I won't entertain you
'''
