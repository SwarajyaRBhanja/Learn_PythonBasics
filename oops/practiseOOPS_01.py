class Programmers:
    company = "Microsoft"  # class attribute

    def __init__(self, name, product):
        self.name = name
        self.product = product

    def getInfo(self):
        print(f"the name of the programmer is {self.name}")
        print(f"the product of the programmer is {self.product}")


swarajya = Programmers("Swarajya Bhanja", "Python")
monalisa = Programmers("Monalisa Biswas", "ETL")
swarajya.getInfo()
monalisa.getInfo()