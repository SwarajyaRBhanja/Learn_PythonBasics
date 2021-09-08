


class Employee:
    company= "Google"
    def getSalary(self):
        print("Salary is 100K")
        print(f"Salary is {self.salary}")
        print(f"Salary of this employee working in {self.company} company is {self.salary}")

#without (self) output---->getSalary() takes 0 positional arguments but 1 was given
swarajya= Employee()
#swarajya.getSalary()
#Employee.getSalary(swarajya) # internally swarajya.getSalary() gets converted to Employee.getSalary(swarajya), when you remove self the compiler tells you you have passed a parameter inEmployee.getSalary(swarajya) but your method is not taking any.
#if you call any function through an object self gets passed automatically 
'''
Modelling a problem in OOPS
We identify the following in our problem

Noun-->Class-->Employee
Adjective-->Attribute-->name, age, salary
Verb-->Method-->getSalary(),increment()

Class Attributes:
An attribute that belong to the class rather than a particular object

company= "Google": specific to class
swarajya= Employee(): object instantiation
Employee.company: changing class attributes

Instance Attributes:
An attribute that belongs to the instance(Object)
Assuming the class from the previous example: 
swarajya.name= "Swarajya"
swarajya.salary= "100k" -->adding instance attributes

Note: Instance attributes take preference over class attributes during assignment & retrieval.
'''

#with self you can use both instance attribute & class attribute
swarajya.salary= 100000 
swarajya.getSalary() #the object on which you are running this method it will print the salary of that object. Employee.getSalary(swarajya)



