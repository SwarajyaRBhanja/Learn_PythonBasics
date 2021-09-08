
#create a class c-2d vector and use it to create another class representing a 3-d vector.

class C2dVect:
    def __init__(self,i,j):
        self.icap= i
        self.jcap= j

    def __str__(self):
        return f"{self.icap}i + {self.jcap}j"    

class C3dVector(C2dVect):
    def __init__(self,i,j,k):
        #self.icap= i
        #self.jcap= j 
        #let's don't do the above shit and call the parent class constructor by super method
        super().__init__(i,j) 
        self.kcap= k  

    def __str__(self):
        return f"{self.icap}i + {self.jcap}j + {self.kcap}k"      

v2D= C2dVect(3,2)
v3D= C3dVector(2,6,8)
print(v2D)
print(v3D)

