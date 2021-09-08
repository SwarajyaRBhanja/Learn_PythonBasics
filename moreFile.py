import os

oldName= "/Users/swarajyabhanja/Desktop/Python/CodeWithHarry/log1.txt"
newName= "/Users/swarajyabhanja/Desktop/Python/CodeWithHarry/new1log1.txt"

with open (oldName) as f:
    con= f.read()

with open (newName,"w") as f:
    f.write(con)   

os.remove("/Users/swarajyabhanja/Desktop/Python/CodeWithHarry/newlog1.txt")