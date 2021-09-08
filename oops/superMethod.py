
# SUPER METHOD: super method is used to access the methods of a super class in the derived class.

'''
super().__init__() #calls constructor of the base class
'''



class tag:
    def __init__(self):
        print("Fucking Tag Con")

    def fuck(self):
        print("Fucking fuck tag parent")


class dag(tag):

    def __init__(self):
        super().__init__()
        print("Fucking Dag Con")

    def fuck(self):
        print("Fucking fuck dag")
        super().fuck()  # this will call tag class method second


class gag(dag):

    def __init__(self):
        super().__init__()
        print("Fucking Gag Con")

    def fuck(self):
        super().fuck()  # this will call dag method first
        print("Gang gag")  # this will run on third


g = gag()
g.fuck()

'''
Fucking Tag Con
Fucking Dag Con
Fucking Gag Con
Fucking fuck dag
Fucking fuck tag parent
Gang gag
'''