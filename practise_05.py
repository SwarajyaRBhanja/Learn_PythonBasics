#mark1= int(input("marks of the student in physics: "))
#mark2= int(input("marks of the student in chemestry: "))
#mark3= int(input("marks of the student in maths: "))

'''if(mark1>=33 and mark2>=33 and mark3>=33 and (mark1+mark2+mark3)/3>=40):
    print("The student has passed the exam")
else:
    print("the student has failed")  '''

'''
if(mark1<33 or mark2<3 or mark3<33):
    print("You have failed in the exam")
elif((mark1+mark2+mark3)/3<40):
    print("you have failed in exam as you couldn't score 40 in total")   
else:
    print("Congratulation!! You have passed.") 
'''

check_spam= ["make a lot of money","buy now","subscribe this","click this"]

mail=input("")

sex=0
for sex in range (len(check_spam)):
    if(check_spam[sex] in mail):
        print("the mail should be considered as spam due to presence of the phrase: "+check_spam[sex])
        sex= sex+1


  
