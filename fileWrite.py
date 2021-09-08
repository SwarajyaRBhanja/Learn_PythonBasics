
'''
In order to write to a file, we first open the file in write or appened mode after which we use the python's f.write() method to write to the file
'''

f= open("/Users/swarajyabhanja/Desktop/Python/CodeWithHarry/sampleFileW.txt","w")
f.write("Please write something to the fie as an evident that Python is smart enough to fuck with a text file")
f.close()

f= open("/Users/swarajyabhanja/Desktop/Python/CodeWithHarry/sampleFileW.txt","a")
f.write(" this is the appending line in the file for sure")
f.close()

