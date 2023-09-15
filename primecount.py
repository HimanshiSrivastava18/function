def prime(a):
    count=0
    i=1
    while i<=a:
        if a%i==0:
            count=count+1
            i+=1
        else:
            i+=1
    if count==2:
        return True
    else:
        return False
b=int(input())
c=prime(b)
print(c)