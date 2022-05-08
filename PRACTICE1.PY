# # a=[5,6,8,9]
# # i=0
# # sum=0
# # while i<len(a):
# #     sum=sum+a[i]
# #     i=i+1
# # print(sum)   

  
    
# # a=[5,6,[9,8],6]
# # i=0
# # sum=0
# # b=[]
# # while i<len(a):
# #     if type(a[i])==list:
# #         pass
# #     else:
# #         b.append(a)
# #         sum=sum+a[i]
# #     i=i+1    
# # print(sum)       
        
        
# # a=[5,6,[9,8],6]
# # i=0
# # sum=0
# # b=[]
# # while i<len(a):
# #     j=0
# #     while j<len(a):
# #         if type(a[i])==list:
# #             pass
# #         else:
# #             b.append(a)
# #             sum=sum+a[i]
# #         j=j+1    
# #     i=i+1    
# # print(sum)  



# # a=[5,6,[9,8],6]
# # i=0
# # while i<len(a):
# #     if type(a[i])==list:
# #         j=0
# #         sum=0
# #         while j<len(a[i]):
# #             sum=sum+a[i][j]
# #             j+=1
# #     i+=1
# # print(sum)



# # a=[[2,3,4],[6,7,8],[1,2,3]]
# # i=0
# # sum=0
# # while i<len(a):
# #     j=0
# #     while j<len(a[i]):
# #         sum=sum+a[i][j]
# #         j=j+1
# #     i=i+1
# # print(sum)    
        
        
        
        
# a=[3,4,[5],[6,7,8],[7],8,9]
# i=0
# sum=0
# while i<len(a):
#     if type(a[i])==list:
#         j=0
#         while j<len(a[i]):
#             sum=sum+a[i][j]
#             j=j+1
#     else:
#         sum=sum+a[i]
#     i=i+1
# print(sum)    
        
        
# a=[3,4,[5],[6,7,8],[7],8,9]
# i=0
# n=[]
# while i<len(a):
#     if type(a[i])==list:
#         j=0
#         while j<len(a[i]):
#             j=j+1
#     else:
#         i=i+1
#         n.append(a)
# print(n)    
  





      
# a=[5,6,7,[4,5,[6,7,8]]]        
# i=0
# sum=0
# while i<len(a):
#     if type(a[i])==list:
#         j=0
#         while j<len(a[i]):
#             sum=sum+a[i][j]
#             j=j+1
#     else:
#         sum=sum+a[i]
#     i=i+1
# print(sum) 





# # a=[9,7,8]
# # pro=1
# # i=0
# # while i<len(a):
# #     if a*2:
# #         pro=pro*a[i]
# #     i=i+1
# # print(pro)        

# a=[9,0,7,6,8]
# max=0
# i=0
# while i<len(a):
#     if max<a[i]:
#         max=a[i]
#     i=i+1
# print(max)
# i=0
# max1=0
# while i<len(a):
#     if max1<a[i]:
#         if max!=a[i]: 
#             max1=a[i] 
#     i=i+1
# print(max1)  
# i=0
# max3=0
# while i<len(a[i]):
#     if max3<a[i]:
#         if max1!=a[i]:
#             if max!=a[i]:
#                 max3=a[i] 
#     i=i+1
# print(max3)                
                       
        
# # i=0
# # min=a[i] 
# # while i<len(a):
# #     if min>a[i]:
# #         min=a[i]  
# #     i=i+1
# # print(min)  
# # i=0
# # min1=a[i]
# # while i<len(a):
# #     if min1>a[i]:
# #         if a[i]!=min:
# #             min1=a[i]  
# #     i=i+1
# # print(min1)                  

# # a=[5,6,7,8,3,2]
# # i=0
# # while i<len(a):
# #     j=0
# #     while j<len(a)-1:
# #         if a[i]<a[j]:
# #             c=a[i]
# #             a[i]=a[j]
# #             a[j]=c
# #         j=j+1
# #     i=i+1
# # print(a)            
        
        
# # a=[5,6,7,8,94,1]  
# # i=0
# # while i<len(a):
# #     j=0
# #     while j<len(a)-1:
# #         if a[i]>a[i]:
# #             c=a[i]
# #             a[i]=a[j] 
# #             a[j]=c
# #         j=j+1
# #     i=i+1
# # print(a)     



# # a="pinki is a good girl" 
# # i=0
# # while i<len(a[i]):
# #     print(a[-1::-1]) 
# #     i=i+1            

# a=[6,7,8,[5,6,[6,7,7]]]
# b=[]
# i=0
# sum=0
# sum1=0
# while i<len(a):
#     if type(a[i])==list:
#         j=0
#         while j<len(a[i]):
#             b.append(a[i][j])
#             # j+=1
#             if type(a[i][j])==list:
#                 k=0
#                 while k<len(a[i][j]):
#                     b.append(a[i][j][k])
#                     k+=1
#             #
#             j+=1
#     else:
#         b.append(a[i])
#         # sum1+=a[i]
#     i+=1
# print(b)
# print(sum+sum1)

# a=[6,7,8,[5,6,[6,7,7]]]
# i=0
# b=[]
# c=[]
# sum=0
# while i<len(a):
#     if type(a[i])==list:
#         j=0
#         sum=0
#         while j<len(a[i]):
#             b.append(a[i][j])
#             sum=sum+a[i][j]
#             j+=1
#     else:
#         c.append(a[i])
#     i+=1
# print(b)
# print(c) 
# print(sum)

# a=[5,6,7,[8,2,3,[4,5]]]
# i=0
# b=[]
# while i<len(a):
#     if type(a[i])==list:
#         j=0
#         while j<len(a[i]):
#             b.append(a[i][j])
#             j=j+1
#     else:
#         b.append(a[i])
#     i=i+1
# print(b) 
# print(sum)       
# i=0
# c=[] 
# sum=0
# sum1=0
# while i<len(b):
#     if type(b[i])==list:
#         j=0
#         while j<len(b[i]):
#             c.append(b[i][j]) 
#             sum=sum+b[i][j]
#             j=j+1
#     else:
#         c.append(b[i])
#         sum1=sum1+b[i]
#     i=i+1
# print(c) 
# print(sum+sum1)                     


a=[5,6,7,[8,2,3,[4,5]]]
i=0
b=[]
while i<len(a):
    if type(a[i])==list:
        j=0
        while j<len(a[i]):
            b.append(a[i][j])
            j=j+1
    else:
        b.append(a[i])
    i=i+1
print(b)        
i=0
c=[] 
sum=0
sum1=0
while i<len(b):
    if type(b[i])==list:
        j=0
        while j<len(b[i]):
            c.append(b[i][j]) 
            j=j+1
    else:
        c.append(b[i])
    i=i+1
print(c)         
