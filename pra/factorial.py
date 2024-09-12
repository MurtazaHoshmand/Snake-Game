# 
# def fact(number):
#     num = number -1
#     for _ in range(number):
#         if num > 0:
#             number *= num
#             num -= 1
#             
#     return number
# 
# print(fact(5))
#     
    
def fact(number):
    fnum = 1
    for num in range(1, number+1):
        fnum *= num
         
    print(f"The factorial of {number} is {fnum}")
    go_ahead = input("Do you wan to check another number?yes/no: ")
    
    if go_ahead == 'yes':
        number = int(input("Please enter the number: "))
        fact(number)
number = int(input("Please enter the number: "))
fact(number)