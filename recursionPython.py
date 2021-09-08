
#recursion is a function which calls itself, it is used to directly use a mathematical formula as a function.

def factorial_iter(n):
    fact=1
    for i in range(n):
        fact=fact*(i+1)
    return fact

def factorial_recursive(m):
    if m==1 or m==0: #base condition which doesn't call the function anymore
        return 1
    else:    
        return m*factorial_recursive(m-1) #function calling itself    

#print(factorial_iter(5))
print(factorial_recursive(6))
       

