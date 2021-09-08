#PROJECT 1: SNAKE, WATER, GUN GAME
#Write a python program to allow the user play this game.

import random

def gameWin(comp,me):
    if comp=='s':
        if me=='w':
            return False
        elif me=='g':
            return True    
    elif comp==me:
        return None
    elif comp=='w':
        if me=='s':
            return True
        elif me=='g':
            return False
    elif comp=='g':
        if me=='s':
            return False
        elif me=='w':
            return True 

print(input("Computer turn: Snake(s) Water(w) or Gun(g) ?"))
randNo= random.randint(1,3) #if I print it will either show 1 or 2
if randNo==1:
    comp= 's'
elif randNo==2:
    comp= 'w'
else:
    comp= 'g'    

me= input("My turn: Snake(1) Water(2) or Gun(3) ?")  
print(f"Computer choose: {comp}")

x= gameWin(comp,me)
if x==None:
    print("This game is a tie")
elif x==True:
    print("I win")  
else:
    print("I lost")      
       

           


            
    