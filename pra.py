# def even_odd(a):
#     i=0
#     count=0
#     sum=0
#     b=[]
#     c=[]
#     while i<len(a):
#         if a[i]%2==0:
#             print(a[i],"even number")
#             b.append(a[i])
#             sum=sum+a[i]
#             count=count+1
#             i=i+1
#         else:
#             print(a[i],"odd number") 
#             c.append(a[i])
#             count=count+1
#             sum=sum+a[i] 
#         i=i+1
#     print(b)  
#     print(c) 
# even_odd([3,4,5,6,7,8])     
             
             
# def my_fun(a):
#     i=len(a)-1
#     while i>0:
#         i=i+1
#     print(i) 
# my_fun(["kirtee", "kishor" ,"patil"])                    



def my_fun(a):
    i=0
    string=" "
    while i<len(a)+1:
        if string==a[-i]:
            i=i+1
    print(string)  
my_fun(["kirtee  kishor patil"])      



a=["kirtee kishor patil"]
b=a.split()
print(b)