#in_1= input("Enter Your Name: ")
greet= "Good Afternoon"
#print(greet+" "+in_1+"!")


#1.Program to fill in a letter template given below with the name & date#
letter= '''Dear <|Name|>,
You are selected!

Date: <|Date|>'''

#part_name= input("Enter your name:\n")
#part_date= input("Enter date:\n")
#letter= letter.replace("<|Name|>",part_name)
#letter= letter.replace("<|Date|>",part_date)
#print(letter)

#2.Write a Program to check double spaces in a string
s1= "Cimpress is in mass-customization  business."
s1.find("  ")
#print(s1.find("  ")) #33

#print(s1.replace("  "," ")) #Cimpress is in mass-customization business.

#3.Write a program to format the string using escape sequence character
letter1= "Dear Swarajya, This python course is nice! Thanks! "
formatted_letter1= "Dear Swarajya, \n\tThis python course is nice! \nThanks! "
print(formatted_letter1)
