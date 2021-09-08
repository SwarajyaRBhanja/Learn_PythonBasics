'''
a= int(input("Please enter first number: "))
b= int(input("Please enter second number: "))
c= int(input("Please enter third number: "))

def findGreatest(a,b,c):
    if (a>b and a>c):
        print(f"{a} is the greatest")
    elif(b>c and b>a):
        print(f"{b} is the greatest")
    else:
        print(f"{c} is the greatest")

findGreatest(a,b,c) 
'''
##################
'''
x= int(input("Please enter a number: "))

def sum_of_series(x):
    if x==0:
        return 0
    return x+sum_of_series(x-1)

sum= sum_of_series(x)
print(f"The sum of series of first natural numbers till {x} is: {sum}") 
'''
#################
'''
  s= input("Please enter a string: ")
word= input("Please enter the word you want to remove: ")

def split_and_remove(s,word):
    news= s.replace(word, "")
    return news.strip()

d=split_and_remove(s,word)
print(d)
  ''' 
####################
a= int(input("Please enter the number: "))

def multiplication_table(a):
    for i in range(0,10):
        print(f"{a}X{i+1} = {a*(i+1)}")
multiplication_table(a)        