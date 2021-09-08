
f_words= ["motherfucker","asshole"]

with open("/Users/swarajyabhanja/Desktop/Python/CodeWithHarry/censored.txt","r") as f:
    content= f.read() #f.read().lower() will read the file in lowercase or you can do content.lower()
content= content.replace("asshole","$@#@#@#$")     

for word in f_words:
    content= content.replace(word,"$@#@#@#$")

with open("/Users/swarajyabhanja/Desktop/Python/CodeWithHarry/censored.txt","w") as f:
    f.write(content)