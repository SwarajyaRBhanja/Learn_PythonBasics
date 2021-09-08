'''
n= int(input("Please enter a number to check: "))
prime= True
for i in range(2, n):
    if(n%i==0):
       prime=False
       break
if prime:
    print("This number is prime")
else:
    print("This number is not Prime")           

'''

'''
n= int(input("Please enter a number to check: "))
for i in range(1,n):  
    n=n*i    
print(n)  
'''

#Printing * patterns
x=4
for i in range(4):
    print("*" *(i+1))


############################################

y=3
for j in range(3):
    print(" "*(y-j-1),end="")
    print("*"*(2*j+1),end="")
    print(" "*(y-j-1),end="")
    print("")

print("##############################")
z=3
for k in range(3):
    print("*"*(z-2*k),end="")
    print(" "*(k),end="")
    print("*"*(k),end="")
    print("")

    #work on the above

#Print multiplication table in reverse order.
    

      
      
   



            
