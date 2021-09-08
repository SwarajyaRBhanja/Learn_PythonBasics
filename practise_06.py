
#n= int(input("Please enter a number Swarajya: "))
#i=1
#for i in range(1,11):
    #print(str(n)+"x"+str(i)+"="+str(n*i))
   # print(f"{n}X{i}={n*i}") #add f before string, I will put variable inside curly braces  

#Program to greet all the person names stored in a list "l1" and which starts with "s"

l= ["Anurag", "Swarajya", "Swastic", "Akash", "Satish", "Sonali", "Srilekha"]  
'''
i=0
for i in range(len(l)):
    if (l[i][0]=="S"):
        print(l[i], "Congratulations!! You are in the leage of 'S' group")
    else:
        print(l[i], "Sorry to say that, you are not eligible to join the 'S' group")   

'''

for name in l:
     if name.startswith("S"):
         print(str(name))
