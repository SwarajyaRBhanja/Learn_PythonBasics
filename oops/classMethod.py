# CLASS METHODS: a class method is a method which is bound to the class and not the object of the class. @classmethod decorator is used to create a class method

class Employee:
    company = "Camel"
    salary = 100
    location = "Delhi"


    @classmethod
    def changeSalary(cls, sal):
        cls.salary = sal #the change of salary here will change the salary in the class too.

        '''
def changeSalary(self, sal): #this will create an instant attribute, it will not change the class attribute salary
        #self.salary = sal
        self.__class__.salary=sal
'''


e = Employee()
print(e.salary)  # 100
e.changeSalary(500)
print(e.salary)  # 500
# 100 with self.salary = sal, 500 with self.__class__.salary=sal
print(Employee.salary)
