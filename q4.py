def factorial(number):
    if number==1:
        return 1
    else:
        return(number*factorial(number-1))
i=1
while i<=7:
    print(factorial(i))
    i=i+1
        
        
