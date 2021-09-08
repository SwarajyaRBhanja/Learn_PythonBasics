with open("/Users/swarajyabhanja/Desktop/Python/CodeWithHarry/log.txt") as f:
    content= f.read()
with open("/Users/swarajyabhanja/Desktop/Python/CodeWithHarry/log1.txt","w") as f:
    f.write(content) 

f1= "/Users/swarajyabhanja/Desktop/Python/CodeWithHarry/log.txt"
f2= "/Users/swarajyabhanja/Desktop/Python/CodeWithHarry/log1.txt"

with open(f1) as f:
    file1= f.read()
with open(f2) as f:
    file2= f.read()

if file1==file2:
    print("The two logs are identical")
else:
    print("The two logs are not identical")            

with open(f2,"w") as f:
    file2= f.write("")