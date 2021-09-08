#Write a class vector representing a vector of n dimension. overload the + & * operators which calculates the sum & the dot product of them.

#Override the __len__() method on vector of above problem to display the dimension of vector

class Vector:
    def __init__(self,vec):
        self.vec= vec

    # def __str__(self):
    #     return f"{self.vec}"

    def __str__(self):
        str_1= ""
        index= 0
        for i in self.vec:
            str_1 += f" {i}a{index} +"
            index +=1
        return str_1[:-1]

    def __add__(self,vec2):
        newList= []
        for i in range(len(self.vec)):
            newList.append(self.vec[i] + vec2.vec[i])
        return Vector(newList)   
    def __mul__(self,vec2):
        sum= 0
        for i in range(len(self.vec)):
            sum +=(self.vec[i] * vec2.vec[i])
        return sum     

    def __len__(self):
        return len(self.vec)    


v1= Vector([1,4,6])
v2= Vector([2,5,6])
print(v1+v2)    
print(v1*v2)  
print(len(v1))
print(len(v2))   