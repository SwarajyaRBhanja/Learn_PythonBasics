class Employee():
    company = "Cimpress"
    salary = 10000
    salary_bonus = 1500
    #totalSalary= 11500

    @property
    # this is not a function, this is a property which will act as a function
    def totalSalary(self):
        return self.salary+self.salary_bonus

    @totalSalary.setter
    def totalSalary(self, val):
        self.salary_bonus = val - self.salary

        #check below getter method
    @totalSalary.getter
    def totalSalary(self):
        return self.salary

e = Employee()
e.totalSalary
print(e.totalSalary)
e.totalSalary = 15000
print(e.salary_bonus)
