

'''
with open("/Users/swarajyabhanja/Desktop/Python/CodeWithHarry/log.txt","r") as f:
    content= f.read() #f.read().lower() will read the file in lowercase or you can do content.lower()

if "python" in content.lower():
    print("python is present in the file")
else:
    print("python is not present in the file") 
'''

content=True
i=1           
with open("/Users/swarajyabhanja/Desktop/Python/CodeWithHarry/log.txt","r") as f:
    
    while content:
        content= f.readline()
        #print(content)

        if "python" in content.lower():
            print(content)
            print("python is present in the file") 
            print(i)
        i+=1    
      


   
