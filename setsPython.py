
# set is a collection of non-repetative elements
#sets are unordered
#sets are unindexed
#you can't change items in sets
#sets can't contain duplicate values
#so, set is a datatype containing unique values

s1= {1,4,6,7,9,3,2,6} 
print(s1) #{1, 2, 3, 4, 6, 7, 9}
print(type(s1)) #<class 'set'>

s2= {}
print(s2) #{}
print(type(s2)) #<class 'dict'>

#empty set can be created using below syntax
s3= set()
print(type(s3)) #<class 'set'>
s3.add(4)
print(s3) #{4}
s3.add(5)
s3.add(4)
print(s3) #{4, 5}

s3.add((2,3,5))
print(s3) #can add tuple
#s3.add([3,9,1])
print(s3) #can't add list, TypeError: unhashable type: 'list'
#you can't add dict to a set too
 #if any object which is not hashable, like list and dict can't be added to set

s4= {1,2,4,6,7,7,4,6,4,6}
print(len(s4)) #5, will not consider the repeated values
s4.remove(7)
print(s4) #{1, 2, 4, 6}

s5= {(4,6,7),4,7,8}
print(len(s5)) #4
s5.remove(7)
print(s5) #{8, (4, 6, 7), 4}
s5.remove((4))
print(s5) #{8, (4, 6, 7)}
s5.remove((4,6,7))
print(s5) #{8}
print(s5.pop()) #8
print(s5) #set()

s6= {6,5,8,3,(5,8,8)}
print(s6.pop()) #3, removes random value from the set
s6.clear() #it will clear set
print(s6) #set()


