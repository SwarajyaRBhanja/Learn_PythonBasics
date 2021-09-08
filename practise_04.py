#finding the largest number
x= 1
l=[]
for x in range (4):
    _in= int(input("User enters number: "))
    l.append(_in)
print(l)  
k=0
max= l[0]
for k in range(len(l)):
    if(l[k]>l[0]):
        max= l[k]
print("the largest number is", max)  
            
        
        