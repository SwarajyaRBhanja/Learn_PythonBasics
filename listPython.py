
#python lists are containers to store a set of values of any datatype.
#created with variable= []

l= [69, "Grey", 'Shades', True, 50.0]
print(l) #[69, 'Grey', 'Shades', True, 50.0] #values in lists stay in a pearticular order.
l[4]= 100 #changing value at index 4 position.
print(l) #[69, 'Grey', 'Shades', True, 100].

#list slicing works same as string

l0= [3,7,7,4,2,6,3,6,8]
l0.sort() #l0 sorts itself
print(l0) #[2, 3, 3, 4, 6, 6, 7, 7, 8]
l0.reverse()
print(l0) #[8, 7, 7, 6, 6, 4, 3, 3, 2]
l0.append(99) #adds 99 at the end [8, 7, 7, 6, 6, 4, 3, 3, 2, 99]
print(l0)
l0.insert(3,88) #[8, 7, 7, 88, 6, 6, 4, 3, 3, 2, 99]
print(l0)
l0.pop(3)
print(l0) #[8, 7, 7, 6, 6, 4, 3, 3, 2, 99]
l0.remove(7) #it will remove first 7 from the list
print(l0) #[8, 7, 6, 6, 4, 3, 3, 2, 99]
print(l0[0])
print(len(l0))