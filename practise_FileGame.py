'''
n1= int(input("Please enter 1st number: "))
n2= int(input("Please enter 2nd number: "))

def game(n1,n2):
    return n1+n2

x=game(n1,n2)

f1= open("/Users/swarajyabhanja/Desktop/Python/CodeWithHarry/highScore.txt","r")
data_1= f1.read()
print("previos high score was: "+data_1)
 
if(data_1== ""):
    f2= open("/Users/swarajyabhanja/Desktop/Python/CodeWithHarry/highScore.txt","w")
    data_2= f2.write(str(x))
    print("writing highest score to file")
    f2.close()
elif str(data_1)<str(x):
    f3= open("/Users/swarajyabhanja/Desktop/Python/CodeWithHarry/highScore.txt","w")
    data_3= f3.write(str(x))
    print(f"Congratualtion! You have got the new highest score {x}") 
    f3.close()   
else:
    print(f"Sorry!! your score is {x} and you couldn't beat the highest score " +data_1) 

'''


      
  

  


    