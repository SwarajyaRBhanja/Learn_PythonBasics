
#write a program to create a dictionary and allow the user to look it up
chords= {"major":(1,3,5),"minor":(1,'b3',5),"suspended 4th":(1,4,5),"suspended 2nd":(1,2,5),"augmented":(1,3,"#4")}
#print(chords)

#print("The chord workbook: " +str(chords.keys()))
#user_enters= input("Please enter chord you want to see: ")

#print("the chord formation will consist of notes: "+str(chords.get(user_enters)))

s= (6, "6")
print(s)

#program to create a dict to allow my friends to enter their fav languages

fav_lan= {}

enter_lang= input("Enter your favourite language Satish: ")
fav_lan["Satish: "]= enter_lang
enter_lang= input("Enter your favourite language Akash: ")
fav_lan["Akash: "]= enter_lang
enter_lang= input("Enter your favourite language Arnab: ")
fav_lan["Arnab: "]= enter_lang
enter_lang= input("Enter your favourite language Anurag: ")
fav_lan["Anurag: "]= enter_lang
print(fav_lan)
