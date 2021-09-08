

#the best way to open & close the file automatically is the with statement.

with open("/Users/swarajyabhanja/Desktop/Python/CodeWithHarry/sampleFileW.txt", "r") as f:
    a= f.read()

    #you don't need to write f.close() as it is done automatically.

with open("/Users/swarajyabhanja/Desktop/Python/CodeWithHarry/sampleFileW.txt", "w") as f:
    a= f.write("me")

with open("/Users/swarajyabhanja/Desktop/Python/CodeWithHarry/sampleFileW.txt", "r") as f:    
    a=f.read()
print(a)       