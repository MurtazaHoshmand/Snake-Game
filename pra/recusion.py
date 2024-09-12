def fact(num): # it is a recursion function that calls itself
    
    if num == 0:
        return 1
    
    return num * fact(num - 1)
    
result = fact(4)
print(result)