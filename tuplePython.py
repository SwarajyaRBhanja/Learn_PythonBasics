
#A tuple is an immutable datatype in python

t= (1,4,6,3,6) 
print(t) 
print(t[0]) 

#t[0]= 1 
#print(t) #TypeError: 'tuple' object does not support item assignment
a0=() #empty tuple
print(a0)
a1=(1,)#tuple with 1 element needs a comma
print(a1)


x= (3,5,3,4,2,5,2,1,6)
print(x.count(3)) #2, this tells me how many 3's are there
print(x.index(3)) #3, it will give the index of element at it's 1st position
