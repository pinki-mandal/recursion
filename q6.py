def pallindrome(string):
    if string==" ":
        return True
    
    
    
i=0
string=" "
size=int(input("enter the number"))
while i<size:
    num=input("enter the number")
    string+=(num) 
    i=i+1  
print(pallindrome(string)) 

