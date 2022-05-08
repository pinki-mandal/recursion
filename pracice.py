# def second_max(a):
#     i=0
#     max=0
#     while i<len(a):
#         if max<a[i]:
#             max=a[i]
#         i=i+1
#     print(max)  
#     i=0
#     max1=0
#     while i<len(a):
#         if max1<a[i]:
#             if a[i]!=max:
#                 max1=a[i]
#         i=i+1
#     print(max1)    
# second_max([5,6,7,9,3,55])          




# a=[4,4] 
# pro=1
# i=0
# while i<len(a):
#     if a*2:
#         pro=pro*a[i]
#     i=i+1
# print(pro)    




# def prime():
#     num=int(input("enter the number"))
#     i=2
#     while i<num:
#         if num%1==0:
#             print("not prime number")
#         break    
#     else:
#         print("prime number")  
#     i=i+1
# prime()  


# a=["pinki","is","a","good","girl"]
# i=len(a)-1
# while i>=0: 
#         print(i,a[i])
#         i=i-1


     
def pallindrome(a):
    i=1
    string=" "
    while i<len(a)+1:
        string+=a[-i]
        i=i+1
    if string==a:
        print(" not pallindrome",string)
    else:
        print("pallindrome",string)
pallindrome("252")        
      
      
 
   
# def fac():
#     i=int(input("enter the number"))
#     fac=1
#     while i>0:
#         fac=fac*i
#         i=i-1
#     print(fac)    
# fac()        



# def fab():
#     a=int(input("enter the number"))
#     while a<=10:
#         if a==0:
#             print(0)
#         elif a==1:
#             print(1)
#         else:
#             print((a-1)+(a-2))
#         a+=1
# fab()    
  
  

        
        
def perfect_no(num):
      i=1
      sum=0
      while num>i:
            if num%i==0:
                  sum+=i
            i+=1
      print(sum)
      if sum==num:
            print("perfect number.")
      else:
            print("not a perfect number.")
perfect_no(18)
              





      #decending#
      
# def reversesort(a):     
#     i=0
#     while i<len(a):
#         j=0
#         while j<len(a)-1:
#             if a[i]>a[j]:
#                 c=a[i]
#                 a[i]=a[j]
#                 a[j]=c
#             j=j+1
#         i=i+1
#     print(a)  
# reversesort([2,3,4,5,6,7])          


          #ascending#
# def sort(a) :  
#     i=0
#     while i<len(a):
#         j=0
#         while j<len(a)-1:
#             if a[i]<a[j]:
#                 c=a[i] 
#                 a[i]=a[j]
#                 a[j]=c
#             j=j+1
#         i=i+1
#     print(a)  
# sort([2,3,4,5,6,7] )    









# i=int(input("enter the number"))
# fac=1
# while i>0:
#     fac=fac*i
#     i=i-1
# print(fac)    
    
    
    
    
# def fab():    
#     num=int(input("enter the number"))
#     while num<=10:
#         if num==0:
#             print("0")
#         elif num==1:
#             print("1") 
#         else:
#             print(num-1) +(num-2)    
#     num+=1        
# fab()    



# l=[1,2,3,4,5,6,9,7,6]
# i=0
# l1=[]
# j=4
# while i<len(l):
#       if i==j:
#             l1.append(20)
#             j+=4
#       l1.append(l[i])
#       i+=1
# print(l1)
            
          


