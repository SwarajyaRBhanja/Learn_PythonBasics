
fruits= ["banana", "apple", "orange", "grapes"]

#while loop
i=0
while i<(len(fruits)):
    #print(fruits[i])
    i=i+1

#for loop
#for item in fruits:
    #print(item)

#for i in range(8):
    #print(i)   

#for i in range(1,8):
    #print(i)  

#for i in range(1,8,2): #start stop stepsize
    #print(i)   


#for loop with else, it is used to run a code once the loop exhausts.

for i in range(1,8):
    print(i)  
else:
    print("what the fuck !!")     


#the break statement: "break" is used to come out of the loop when encountered. it instructs the program to exit the loop, here else: will not execute if the loop is broke in between
for duck in range (0,10):
    print(duck) 
    if duck==3:
        break
else:
    ("what the duck")     

#the continue statement: continue is used to stop the current iteration of the loop and continue with the next one, it instructs the program to skip the iteration.

for i in range(10):
    if i==5:
        continue #this will ignore if i is 5, and will go to 6
    print(i)

#pass statement: pass is a null statement in python, it instructs to do nothing.

i=4
if i>0:
    pass #fuck you later
print("next fuck")
