# def pattern(number):
#     if number==1:
#         return 1
#     else:
#         return pattern(number-1)+3
# i=1
# while i<10:
#     print(pattern(i)) 
#     i=i+1  
    
    
# import datetime

# x = datetime.datetime.now()
# print(x) 


# def print_factors(x):
#     for i in range(1, x + 1):
#         if x % i == 0:
#            print(i)
# num = int(input("enter the number"))
# print_factors(num)



def factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""

    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))


num = 3
print("The factorial of", num, "is", factorial(num))

# def a(x):
#     if x==1:
#         return 1
#     else:
#         return (x*1)
    
    
    