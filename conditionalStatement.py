a= int(input("Please enter your age: "))

if(a>21 and a<60):
    print("You can work with us")
else:
    print("You are not eligible to work with us") 
print("Thanks for applying")       

a= None

if(a is None): #Yes. will check for object reference
    print("Yes")
else:
    print("No")    

if(a==None): #Will check for object value
    print("Yes")
else:
    print("No")       

x= [5,6,7]
print(6 in x) #True