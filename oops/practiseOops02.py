#Create a class employee & add salary and increment properties to it.
#Write a method SalaryAfterIncrement, with a property decorator with a setter which changes the value of increment based on the salary

class Employee:
    salary= 50000
    increment= 1.5

    @property
    def salaryAfterIncrement(self):
        return self.salary*self.increment

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, salary_after_increment):
        self.increment= salary_after_increment/self.salary

e= Employee()
print(e.salaryAfterIncrement)  
print(e.increment)   
e.salaryAfterIncrement= 30000
print(e.salaryAfterIncrement)  
print(e.increment) 



