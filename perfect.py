def perfect(a):
    sum=0
    i=1
    while i<a:
        if a%i==0:
            sum=sum+i
        i+=1
    if sum==a:
        return True
    else:
        return False
b=int(input())
c=perfect(b)
print(c)