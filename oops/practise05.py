
#write __str__() method to print the vector as follows.
#7i + 8j+ 10k
#assume vector of dimesion 3 for this problem.

class Vector:
    def __init__(self,vec):
        self.vec= vec

    def __str__(self):

        for m in range(len(self.vec)):           
            return f"{self.vec[m]}i+{self.vec[m+1]}j+{self.vec[-1]}k"

v1= Vector([1,4,6])
print(v1)    
        