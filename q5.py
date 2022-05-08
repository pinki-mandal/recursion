def sum(number):
    if number==[]:
        return 0
    else:
        return number[0]+sum(number[1:])
    
    
    
i=0
number=[]
size=int(input("enter the number"))
while i<size:
    num=int(input("enter the number"))
    number.append(num) 
    i=i+1  
print(sum(number)) 