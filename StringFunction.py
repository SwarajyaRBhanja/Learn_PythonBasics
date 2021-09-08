from ast import Index
from typing import Counter


tale= "Once upon a time there was a guy named Swarajya, who had tried to learn Python from Youtube"

print(tale.endswith('Aliens')) #False
print(tale.endswith('Youtube')) #True
print(len(tale)) #91
print(tale.count('Swarajya')) #counts total number of occurrence of GIVEN character/phrase/word
print(tale.count('a')) #9

print("************************************************************************************************")
#finding out indexes of a. 
print("While Loop Approach")
n=0
while n<=(len(tale)-1):
    if tale[n]=='a':
        print(n, end =" ")
    n=n+1

print("")
print("For Loop Approach")
for k in range(len(tale)-1):
    if tale[k]=='a':
        print(k, end =" ")
    k=k+1    
print("")

#str.find will find the character only at first occurrence
print(tale.find('Swarajya')) #39
print(tale.find('Bhanja')) #-1

print(tale.replace('Swarajya','Swarajya Bhanja')) #Once upon a time there was a guy named Swarajya Bhanja, who had tried to learn Python from Youtube
#str.replace will replace all the occurrence of a given word with new word


#ESCAPE SEQUENCE
'''
    \n,     \t, \',    \\
    newline,tab,single quote,backslash

'''


story_1= "Swarajya is a good boy. Everybody knows that."
story_2= "Swarajya is a good boy. \nEverybody \tknows th\\at."
print(story_1)
#Swarajya is a good boy. Everybody knows that.
print(story_2)
#Swarajya is a good boy. 
#Everybody knows that.




    


