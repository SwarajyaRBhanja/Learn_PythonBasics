
from os import read

file= open("/Users/swarajyabhanja/Desktop/Python/CodeWithHarry/houseIsRed.txt","r")

data= file.read()
print(data)
print("")

if "sex" in data:
    print("sex is there in Poem")
elif "laugh" in data:
    print("laugh is there in Poem")    
else:
    print("hahahahhahaha")    