# def maxof_3(a,b,c):
#     if a>=b and a>=c:
#         return a
#     elif b>=a and b>=c:
#         return b
#     else:
#         return c
# e=int(input())
# f=int(input())
# g=int(input())
# d=maxof_3(e,f,g)
# print(d)


# def limit(u,l,n):
#     if n>=l and n<=u:
#         return True
#     else:
#         return False
# a=int(input())
# b=int(input())
# c=int(input())
# d=limit(a,b,c)
# print(d)

# def factorial(a):
#     i=1
#     fac=1
#     while i<=a:
#         fac=fac*i
#         i+=1
#     return fac
# b=int(input())
# print(factorial(b))


# def string(a): 
#     b=" "
#     for i in a:
#         b=i+b
#     return b
# b=(input())
# c=string(b)
# print(c)



# def prime(a):
#     count=0
#     i=1
#     while i<=a:
#         if a%i==0:
#             count=count+1
#             i+=1
#         else:
#             i+=1
#     if count==2:
#         return True
#     else:
#         return False
# b=int(input())
# c=prime(b)
# print(c)


# def perfect(a):
#     sum=0
#     i=1
#     while i<a:
#         if a%i==0:
#             sum=sum+i
#         i+=1
#     if sum==a:
#         return True
#     else:
#         return False
# b=int(input())
# c=perfect(b)
# print(c)


# i=1
# sum=0
# while i<1000:
#     if i%3==0 or i%5==0:
#         sum+=i
#     i+=1
# print(sum)

# i=1
# sum=0
# while i<=10:
#     sum+=i*i
#     i+=1
#     print(sum)
# n=int(input())
# x=0
# y=1
# z=0
# while z<=n:
#     print(z)
#     x=y
#     y=z
#     z=x+y


# def sum(a):
#     for i in range(a):
#         sum=sum+a[i]
#         return sum
# b=int(input())
# c=sum(b)
# print(c)

# a=[1,2,3,4,5,6,7,8,9]
# for i in a:
#     if i%2==0:
#         print(i)

# a=(input())
# c=0
# cs=0
# i=0
# while i<len(a):
#     if a[i]>="A" and a[i]<="Z":
#         c+=1
#     elif a[i]>="a" and a[i]<="z":
#         cs+=1
#     i+=1
# print(c,cs)

# def unique(a):
#     b=[0]*(max(a)+1)
#     for i in a:
#         b[i]+=1
#     for i in range(max(a)+1):
#         if b[i]>=1:
#             print(i)
# a=[1,2,3,4,5,4,3,2]
# unique(a)

# def  pangram(a):
#     b="abcdefghijklmnopqrstuvwxyz"
#     c=0
#     i=0
#     while i<len(b):
#         if b[i] in a:
#              c+=1
#              i+=1
#     if c==len(b):
#         print("yes")
#     else:
#         print("not")
# a="adgrtqwertuioplkjhgfdsazxcvbnm"
# pangram(a)


# i=1
# while i<=5:
#     j=1
#     fac=0
#     while j<=i:
#          fac=fac(i!)/fac(j!)fac(i-j)
#           print(fac,end=" ")
#           j+=1
#     print()
#     i+=1



# def fac(n):
#     res=1
#     for i in range(n):
#         res*=i+1
#         return res
# def pascal(n):
#     for i in range(n):
#         for j in range(i+1):
#             icj=fac(i)/fac(j)*fac(i-j)
#             print(icj,end=" ")
#         print()


# def unique(a):
#     b=[0]*(max(a)+1)
#     for i in a:
#         b[i]+=1
#     for i in range(max(a)+1):
#         if b[i]>=1:
#          print(i)
# a=[1,3,2,1,3,2,4,3,5,4]
# unique(a)

# a=int(input())
# i=2
# while i<=a:
#     if a%i==0:
#         a=a//i
#         print(i)
#     else:
#         i+=1


# a=int(input())
# i=0
# while i<=a:
#     max_produt=0
#     for j in range (i,a):
#         product=i*j
#         if product<max_product:
#             break
#     number=product
#     reverse=0


# i=1
# while i<=20:
#     if a%i==0:
#         print(a)
# 
#     i+=1




#   armstrong number
# a=int(input("enter the number"))
# sum=0
# count=0
# d=a
# result=d
# while a>0:
#   a=a//10
#   count+=1
# while d>0:
#   b=d%10
#   sum=sum+(b**count)
#   d=d//10
# if result==sum:
#   print("Yes")
# else:
#   print("No")


# n=int(input())
# i=1
# b=1
# while i<=n:
#     a=b
#     c=0
#     while a>0:
#         a=a//10
#         c=c+1
#     d=b
#     s=0
#     while d>0:
#         t=d%10
#         s=s+t**c
#         d=d//10
#     if s==b:
#         print(b)
#     i+=1
#     b+=1
  


# a=[3,8,9,6,2,7]
# n=len(a)
# for i in range(1,n):
#     key=a[i]
#     j=i-1
#     while j>=0 and key<a[j]:
#         a[j+1]=a[j]
#         j-=1
#     a[j+1]=key

# print(a)



# sum of the squar and difference
# i=1
# sum=0
# sum1=0
# while i<=100:
#     sum+=i**2
#     i+=1
# a=sum
# for i in range(101):
#     sum1+=i
#     d=sum1**2
# print(d-a)


# i=1
# while i<=5:
#     j=i
#     while j<=6-1:
#             print(j)
#             j-=1
#     print()
#     i+=1

# a=int(input())
# i=0
# b=[0]*a
# while i<a:
#     b[i]=i+1
#     i=i+1
# print(b)


# a=int(input())
# i=0
# c=[0]*a
# while i<a:
#     b=(input())
# i+=1
# print(b)

# n=list(map(int,input().split()))
# for i in range(n):
#     n.sort()
# print(n)


# n=int(input())
# m=int(input())
# a=list(map(int,input().split()))
# q=int(input())
# count=0
# for i in range(1,q):
#     query=list(map(int,input())
#     if query[0]=="1":
#         a[i]=v
#     else:
#         for j in range(q):
#             if a[j]%m==x:
#                 count+=1
#     print(count)

# n=int(input())
# i=1
# a=1
# count=0
# while i<=n:
#     while i<=a:

#         if a%i==0:
#             count+=1
#         a+=1
#     i+=1
# if count==2:
#     print("prime")
# else:
#     print("not")



# n=int(input())
# i=1
# count=0
# m=0
# while i<=n//2:
#     if n%i==0:
#         count+=1
#     i+=1
# if count==1:
#     m+=1
# if m==n:
#     print(n)

#     print("yes")
# else:
#     print("not")
#     a=count
# for i in range(a):
#     if count==n:
# #         print(i)



# count prime number
# def prime (num):
#     j=2
#     count=0
#     while j<=num:
#         if num%j==0:
#             count+=1
#         j+=1
#     if count==1:
#         return True
#     else:
#         return False
# i=2
# count=0
# n=int(input("Enter a number: "))
# while count<n:
#     if prime(i):
#         count+=1
#         a=i
#     i+=1
# print(a)
    
# import time
# start=time.time()
# i=0
# n=10**7
# while i<n:
#     i+=1
# end=time.time()
# print(end-start)



# for i in range(10):
#     num=random.randint(1,11)
#     l[i]=num
# import random
# l=[0]*10
















