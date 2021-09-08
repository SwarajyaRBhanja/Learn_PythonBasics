name= "swarajya"

'''
 s  w  a  r  a  j  y  a
 0  1  2  3  4  5  6  7
-8 -7 -6 -5 -4 -3 -2 -1

#to access/know the last element in the string we can use name[-1]
'''
print(name[0:3]) #swa
#Here in [0:3] the python will print 0 1 2 position, it will not consider 3. this thing applies to list also
print(name[2:5]) # ara
print(name[-8:-6]) #sw will be printed as it will not consider -6 position
print(name[:4]) #swar
print(name[1:]) #warajya

#String slicing with skip value
print(name[1:5:2]) #wr, it will skip every second character ie 1:5=wara will become wr, [starting index:ending index:skip value]

print(name[2::3]) #aj

