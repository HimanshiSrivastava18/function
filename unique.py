def unique(a):
    b=[0]*(max(a)+1)
    for i in a:
        b[i]+=1
    for i in range(max(a)+1):
        if b[i]>=1:
            print(i)
a=[1,2,3,4,5,4,3,2]
unique(a)







def unique(a):
    b=[0]*(max(a)+1)
    for i in a:
        b[i]+=1
    for i in range(max(a)+1):
        if b[i]>=1:
         print(i)
a=[1,3,2,1,3,2,4,3,5,4]
unique(a)