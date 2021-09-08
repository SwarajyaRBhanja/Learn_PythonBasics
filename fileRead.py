'''
This is Swarajya
Working File I/O Operation
'''

#USE OPEN FUNCTION TO READ THE CONTENT OF A FILE#
f= open("/Users/swarajyabhanja/Desktop/Python/sampleFile.txt", "r") #and by default the mode is r
'''

data= f.read() 
print(data)
f.close()
#open is built-in function
#("x","y") : x= file name, y= mode of opening(read mode)
'''
########################################################
'''
data= f.read(7) #This will read first 7 characters 
print(data) #"This is"
'''

#WORKING ON READLINE function
data= f.readline() #it will read the first line of the file
print(data)  #This is Swarajya
data= f.readline() #doing again, it will read the second line of the file and so on
print(data) #Working File I/O Operation

'''
Modes of opening a file
r= open for reading
w= open for writing
a= open for appending
t= open for updating
rb will open for read in binary mode
rt will open for read in txt mode

'''





